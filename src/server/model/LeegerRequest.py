from __future__ import annotations

from dataclasses import dataclass

from src.server.enum.FantasySite import FantasySite
from src.server.model.JSONDeserializable import JSONDeserializable


@dataclass(kw_only=True)
class LeegerRequest(JSONDeserializable):
    fantasy_site: FantasySite
    league_id: str | int
    years: list[str]

    @staticmethod
    def from_json(d: dict) -> LeegerRequest:
        fantasy_site = FantasySite.from_str(d["fantasy_site"])
        league_id = d["league_id"]
        years = d.get("years", list())
        return LeegerRequest(fantasy_site=fantasy_site,
                             league_id=league_id,
                             years=years)
