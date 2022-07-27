import ast

from flask import Request


class ControllerHelper:
    """
    A helper class for controllers
    """

    @staticmethod
    def get_dict_from_request(request: Request) -> dict:
        # converts request headers into a python dictionary
        return ast.literal_eval(request.data.decode("UTF-8"))
