import os

from app import app
from flask import request, redirect, url_for

from src.server.model.LeegerRequest import LeegerRequest
from src.server.service.LeagueService import LeagueService
from src.server.util.ControllerHelper import ControllerHelper


@app.route("/leeger", methods=["POST"])
def leeger():
    data = ControllerHelper.get_dict_from_request(request)
    error_message = None
    try:
        leeger_request = LeegerRequest.from_json(data)
        directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "file_store"))
        LeagueService.save_excel_stats(leeger_request, directory_path)
    except Exception as e:
        # TODO: clean this up and parse certain exceptions for cleaner display in UI
        error_message = str(e)
    return redirect(url_for("index", error_message=error_message))
