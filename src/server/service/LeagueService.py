import os

from leeger import ESPNLeagueLoader, SleeperLeagueLoader, YahooLeagueLoader

from src.server.enum.FantasySite import FantasySite
from src.server.exception.BadRequestException import BadRequestException
from src.server.model.LeegerRequest import LeegerRequest


class LeagueService:

    @classmethod
    def save_excel_stats(cls, leeger_request: LeegerRequest, directory_path: str) -> None:
        league = None
        # get League object
        if leeger_request.fantasy_site == FantasySite.ESPN:
            # need ints for league ID and years
            try:
                espn_league_id = int(leeger_request.league_id)
            except ValueError as e:
                raise BadRequestException("ESPN League ID must be an int.")
            league = ESPNLeagueLoader.loadLeague(espn_league_id, leeger_request.years)
        elif leeger_request.fantasy_site == FantasySite.SLEEPER:
            league = SleeperLeagueLoader.loadLeague(leeger_request.league_id)
        elif leeger_request.fantasy_site == FantasySite.YAHOO:
            # need ints for league ID and years
            try:
                yahoo_league_id = int(leeger_request.league_id)
            except ValueError as e:
                raise BadRequestException("Yahoo League ID must be an int.")
            league = YahooLeagueLoader.loadLeague(yahoo_league_id, leeger_request.years)

        # save excel file locally
        file_path = cls.get_full_file_path_for_league(leeger_request, directory_path)
        league.toExcel(filePath=file_path)

    @staticmethod
    def get_full_file_path_for_league(leeger_request: LeegerRequest, directory_path: str) -> str:
        file_name = f"{leeger_request.fantasy_site.name}_{leeger_request.league_id}"
        for year in leeger_request.years:
            file_name += f"_{year}"

        numbered_file_name = file_name
        number = 2
        full_path = os.path.join(directory_path, f"{numbered_file_name}.xlsx")
        while os.path.exists(full_path):
            numbered_file_name = f"{file_name}({number})"
            number += 1
            full_path = os.path.join(directory_path, f"{numbered_file_name}.xlsx")
        return full_path
