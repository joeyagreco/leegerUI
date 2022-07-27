from app import app
from flask import render_template, url_for, redirect, request


@app.route('/favicon.ico')
def favicon():
    """
    This is for the browser icon.
    """
    return redirect(url_for('static', filename='icon/football.ico'))


@app.route("/")
def index():
    error_message = request.args.get("error_message")
    return render_template("index.html", error_message=error_message)
