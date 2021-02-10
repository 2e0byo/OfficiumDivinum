"""Endpoint to serve complete offices."""
from datetime import datetime

from flask import abort
from flask import request
from flask_api.decorators import set_renderers
from flask_api.renderers import JSONRenderer

from . import database
from .api import api
from .renderers import objectHTMLRenderer


@api.route("/office", methods=["GET"])
@set_renderers(JSONRenderer, objectHTMLRenderer)
def get_office():
    args = request.args

    try:
        office = args["office"]
    except KeyError:
        abort(400)

    if not office == "prime":
        abort(404)  # for now
    language = args["lang"] if "lang" in args.keys() else "latin"
    translation = args["trans"] if "lang" in args.keys() else None
    date = args["date"] if "date" in args.keys() else str(datetime.now().date())
    calendar = args["calendar"] if "calendar" in args.keys() else "1962"
    if not calendar == "1962":
        abort(404)

    return database.get_office(office, calendar, date, language, translation)
