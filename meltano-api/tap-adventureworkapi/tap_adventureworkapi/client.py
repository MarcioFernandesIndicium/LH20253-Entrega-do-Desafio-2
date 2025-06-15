"""REST client handling, including AdventureWorkAPIStream base class."""

from __future__ import annotations

import decimal
import typing as t
from importlib import resources
import json

from requests.auth import HTTPBasicAuth
from singer_sdk.helpers.jsonpath import extract_jsonpath

from singer_sdk.pagination import BaseOffsetPaginator  # noqa: TC002
from singer_sdk.streams import RESTStream

from tap_adventureworkapi.pagination import AdventureWorkOffsetPaginator

if t.TYPE_CHECKING:
    import requests
    from singer_sdk.helpers.types import Context


# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = resources.files(__package__) / "schemas"


class AdventureWorkAPIStream(RESTStream):
    """AdventureWorkAPI stream class."""

    MAX_PARALLEL_REQUESTS = 1
    timeout = 10 # seconds
    

    # Update this value if necessary or override `parse_response`.
    records_jsonpath = "$.data[*]"

    def get_new_paginator(self):

        limit = self.config.get("limit", 10000)
        return AdventureWorkOffsetPaginator(
            start_value=0,
            page_size=limit,
        )

    # Update this value if necessary or override `get_new_paginator`.
    # next_page_token_jsonpath = "$.next_page"  # noqa: S105

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        # TODO: hardcode a value here, or retrieve it from self.config
        if "api_url" not in self.config:
            self.logger.critical("Configuration setting 'api_url' is missing.")
            raise ValueError("The 'api_url' configuration value is required.")
        return self.config["api_url"]

    @property
    def authenticator(self) -> HTTPBasicAuth:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return HTTPBasicAuth(
            username=self.config["username"],
            password=self.config["password"],
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")  # noqa: ERA001
        return {}

    def get_url_params(
        self,
        context: Context | None,  # noqa: ARG002
        next_page_token: int | None,  # noqa: ANN401
    ) -> dict[str, t.Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {
            "limit": self.config.get("limit", 10000),
            "offset": next_page_token or 0,
        }
        return params

    def prepare_request_payload(
        self,
        context: Context | None,  # noqa: ARG002
        next_page_token: t.Any | None,  # noqa: ARG002, ANN401
    ) -> dict | None:

        # TODO: Delete this method if no payload is required. (Most REST APIs.)
        return None

    def parse_response(self, response: requests.Response) -> t.Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        try:

            resp_json = response.json(parse_float=decimal.Decimal)
        except json.JSONDecodeError:
            self.logger.error(
                f"Não foi possível decodificar a resposta JSON: {response.text}"
            )
            return

        yield from extract_jsonpath(self.records_jsonpath, input=resp_json)

    def post_process(
        self,
        row: dict,
        context: Context | None = None,  # noqa: ARG002
    ) -> dict | None:
        """As needed, append or transform raw data to match expected structure.

        Args:
            row: An individual record from the stream.
            context: The stream context.

        Returns:
            The updated record dictionary, or ``None`` to skip the record.
        """
        # TODO: Delete this method if not needed.
        return row
