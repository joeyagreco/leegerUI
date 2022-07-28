from app import app
from flask import request, redirect, url_for

from src.server.enum.FantasySite import FantasySite
from src.server.exception.BadRequestException import BadRequestException
from src.server.model.LeegerRequest import LeegerRequest
from src.server.util.ControllerHelper import ControllerHelper


@app.route("/leeger", methods=["GET", "POST"])
def leeger():
    data = ControllerHelper.get_dict_from_request(request)
    error_message = None
    try:
        leeger_request = LeegerRequest.from_json(data)
        if leeger_request.fantasy_site == FantasySite.ESPN:
            # need ints for league ID and years
            try:
                espn_league_id = int(leeger_request.league_id)
            except ValueError as e:
                raise BadRequestException("ESPN League ID must be an int.")
        elif leeger_request.fantasy_site == FantasySite.SLEEPER:
            ...
        elif leeger_request.fantasy_site == FantasySite.YAHOO:
            # need ints for league ID and years
            try:
                yahoo_league_id = int(leeger_request.league_id)
            except ValueError as e:
                raise BadRequestException("Yahoo League ID must be an int.")
    except BadRequestException as e:
        error_message = str(e)
    return redirect(url_for("index", error_message=error_message))
