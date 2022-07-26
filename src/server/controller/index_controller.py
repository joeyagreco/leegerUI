from app import app
from flask import render_template, url_for, redirect


@app.route('/favicon.ico')
def favicon():
    """
    This is for the browser icon.
    """
    return redirect(url_for('static', filename='icon/football.ico'))


@app.route("/")
def index():
    return render_template("index.html")
