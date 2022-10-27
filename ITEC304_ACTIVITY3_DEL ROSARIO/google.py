from flask import flask
from datetime import datetime

app = flask (__name__)

@ app.route('/')
def hello():
    return """<html><body>
        <h1>HELLO, WORLD <h1>
        The time is (0).</body></html>""".format(
            str(datetime.now()))
