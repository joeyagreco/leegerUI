from app import app
from flask import request, redirect, url_for

from src.server.exception.BadRequestException import BadRequestException
from src.server.model.LeegerRequest import LeegerRequest
from src.server.util.ControllerHelper import ControllerHelper


@app.route("/leeger", methods=["GET", "POST"])
def leeger():
    data = ControllerHelper.get_dict_from_request(request)
    error_message = None
    try:
        leeger_request = LeegerRequest.from_json(data)
    except BadRequestException as e:
        error_message = str(e)
    return redirect(url_for("index", error_message=error_message))
