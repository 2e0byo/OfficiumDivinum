"""
Endpoint to serve complete offices.

This endpoint serves complete offices, and any legitimate bits of
them.  Queries may be either in json or as html queries.  The response
is negotiated according to the `Accept:` header of the request, and
currently supports either `application/json` (for serialised objects)
or `text/html` (for rendered objects).

Note that requesting parts of an office automatically suppresses
requesting a page.
"""
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

    things = database.get_office(office, calendar, date, language, translation)

    parts = args.getlist("part")
    if not parts:
        return things

    else:
        disjointed_members = []
        for part in parts:
            for thing in things:
                disjointed_members.append(getattr(thing, part))
        return disjointed_members
