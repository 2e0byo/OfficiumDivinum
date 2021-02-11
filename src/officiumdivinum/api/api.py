import jinja2
from flask_api import FlaskAPI
from markdown import markdown


def markdown_no_p(text):
    """Wrap text in markdown without wrapping it in paragaph tags."""

    md = markdown(text)
    p = "<p>"
    end_p = "</p>"
    if md.startswith(p) and md.endswith(end_p):
        md = md[3:-4]
    return jinja2.Markup(md)


api = FlaskAPI(__name__)
api.jinja_env.filters["markdown"] = markdown_no_p


def init():
    from . import database

    database.init()
