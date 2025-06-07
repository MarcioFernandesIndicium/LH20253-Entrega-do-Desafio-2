"""Stream type classes for tap-adventureworkapi."""

from __future__ import annotations

import typing as t
from importlib import resources

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_adventureworkapi.client import AdventureWorkAPIStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = resources.files(__package__) / "schemas"
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class PurchaseOrderDetailStream(AdventureWorkAPIStream):
    """Define custom stream."""

    name = "PurchaseOrderDetail"
    path = "/PurchaseOrderDetail"
    # primary_keys: t.ClassVar[list[str]] = ["id"]
    # replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "PurchaseOrderDetail.json"  # noqa: ERA001


class PurchaseOrderHeaderStream(AdventureWorkAPIStream):
    """Define custom stream."""

    name = "PurchaseOrderHeader"
    path = "/PurchaseOrderHeader"
    # primary_keys: t.ClassVar[list[str]] = ["id"]
    # replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "PurchaseOrderHeader.json"  # noqa: ERA001


class SalesOrderDetailStream(AdventureWorkAPIStream):
    """Define custom stream."""

    name = "SalesOrderDetail"
    path = "/SalesOrderDetail"
    # primary_keys: t.ClassVar[list[str]] = ["id"]
    # replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "SalesOrderDetail.json"  # noqa: ERA001


class SalesOrderHeaderStream(AdventureWorkAPIStream):
    """Define custom stream."""

    name = "SalesOrderHeader"
    path = "/SalesOrderHeader"
    # primary_keys: t.ClassVar[list[str]] = ["id"]
    # replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "SalesOrderHeader.json"  # noqa: ERA001
