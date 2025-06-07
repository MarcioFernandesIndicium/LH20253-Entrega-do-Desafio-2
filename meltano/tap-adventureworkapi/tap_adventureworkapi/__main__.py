"""AdventureWorkAPI entry point."""

from __future__ import annotations

from tap_adventureworkapi.tap import TapAdventureWorkAPI

TapAdventureWorkAPI.cli()
