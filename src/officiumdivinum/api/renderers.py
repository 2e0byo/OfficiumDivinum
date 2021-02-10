"""Renderers for various formats."""
from flask import render_template
from flask import request
from flask_api.renderers import BaseRenderer


class objectHTMLRenderer(BaseRenderer):
    media_type = 'text/html; charset="UTF-8"'

    def render(self, data, media_type, **options):
        args = request.args

        try:
            page = True if args["page"] else False
        except KeyError:
            page = None

        content = ""
        for thing in data:
            content += thing.html()

        if page:
            return render_template("html/page.html", content=content)
        else:
            return content
