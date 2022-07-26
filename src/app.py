import os

from flask import Flask

from server.util.EnvironmentReader import EnvironmentReader

# set directories

templateDir = os.path.join(os.path.dirname(__file__), EnvironmentReader.get("TEMPLATE_DIR_RELATIVE_PATH"))
staticDir = os.path.join(os.path.dirname(__file__), EnvironmentReader.get("STATIC_DIR_RELATIVE_PATH"))
app = Flask(__name__, template_folder=templateDir, static_folder=staticDir)

if __name__ == "__main__":
    from server.controller.index_controller import *  # noqa

    if EnvironmentReader.get("TEST_ENVIRONMENT") == "True":
        app.run(debug=True)
    else:
        app.run(host="0.0.0.0", port=80)
