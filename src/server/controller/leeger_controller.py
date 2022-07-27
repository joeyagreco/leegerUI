from app import app
from flask import request, redirect, url_for

from src.server.model.LeegerRequest import LeegerRequest
from src.server.util.ControllerHelper import ControllerHelper


@app.route("/leeger", methods=["POST"])
def leeger():
    data = ControllerHelper.get_dict_from_request(request)
    leeger_request = LeegerRequest.from_json(data)
    return redirect(url_for("index"))
