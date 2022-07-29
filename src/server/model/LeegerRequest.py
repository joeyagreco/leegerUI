from __future__ import annotations

from dataclasses import dataclass

from src.server.enum.FantasySite import FantasySite
from src.server.exception.BadRequestException import BadRequestException
from src.server.model.JSONDeserializable import JSONDeserializable


@dataclass(kw_only=True)
class LeegerRequest(JSONDeserializable):
    fantasy_site: FantasySite
    league_id: str | int
    years: list[int]

    @staticmethod
    def from_json(d: dict) -> LeegerRequest:
        try:
            fantasy_site = FantasySite.from_str(d["fantasy_site"])
            league_id = d["league_id"]
            years_raw = d.get("years", list())
            years = years_raw.split(",") if not isinstance(years_raw, list) else years_raw
            years = [int(year) for year in years]
            # TODO: validate this
            return LeegerRequest(fantasy_site=fantasy_site,
                                 league_id=league_id,
                                 years=years)
        except Exception as e:
            raise BadRequestException(str(e))
