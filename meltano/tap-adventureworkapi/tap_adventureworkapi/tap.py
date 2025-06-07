"""AdventureWorkAPI tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_adventureworkapi import streams


class TapAdventureWorkAPI(Tap):
    """AdventureWorkAPI tap class."""

    name = "tap-adventureworkapi"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "username",
            th.StringType,
            required=True,
            description="The username to use for authentication with the AdventureWorkAPI",
        ),
        th.Property(
            "password",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The password to use for authentication with the AdventureWorkAPI",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync. Defaults to 2010-01-01T00:00:00Z.",
            default="2010-01-01T00:00:00Z",
        ),
        th.Property(
            "api_url",
            th.StringType,
            required=True,  # Although it has a default, making it required ensures it's always considered.
            description="The base URL for the AdventureWorkAPI service",
            default="http://18.209.218.63:8080",
        ),
        # th.Property(
        #     "user_agent",
        #     th.StringType,
        #     description=(
        #         "A custom User-Agent header to send with each request. Default is "
        #         "'<tap_name>/<tap_version>'"
        #     ),
        # ),
    ).to_dict()

    def discover_streams(self) -> list[streams.AdventureWorkAPIStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.PurchaseOrderDetailStream(self),
            streams.SalesOrderHeaderStream(self),
            streams.SalesOrderDetailStream(self),
            streams.PurchaseOrderHeaderStream(self),
            # streams.UsersStream(self),
        ]


if __name__ == "__main__":
    TapAdventureWorkAPI.cli()
