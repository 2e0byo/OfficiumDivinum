"""Renderers for various formats."""
from flask import render_template
from flask import request
from flask_api.renderers import BaseRenderer

from .api import api


class objectHTMLRenderer(BaseRenderer):
    media_type = 'text/html; charset="UTF-8"'

    def render(self, data, media_type, **options):
        print("Got here")
        args = request.args

        try:
            page = True if args["page"] else False
        except KeyError:
            page = None

        content = []
        for thing in data:
            content.append(thing.html())

        if page:
            page = {}
            page["title"] = data[0].name
            page["liturgical_day"] = data[0].liturgical_day
            page["calendar_day"] = data[0].calendar_day
            if len(content) == 2:
                content, translation = content
            else:
                content = content[0]
                translation = None
            return render_template(
                "html/page.html", content=content, translation=translation, page=page
            )
        else:
            return " ".join(content)
