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

        if page:
            print(len(data))
            if len(data) == 2:
                content, translation = data
                content = content.html()
                translation = translation.html()
            else:
                content = " ".join([x.html() for x in data])
                translation = None
            page = {}
            page["title"] = data[0].name
            page["liturgical_day"] = data[0].liturgical_day
            page["calendar_day"] = data[0].calendar_day
            return render_template(
                "html/page.html", content=content, translation=translation, page=page
            )
        else:
            content = " ".join([x.html() for x in data])
            return content
