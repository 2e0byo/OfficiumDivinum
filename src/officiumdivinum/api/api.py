from pathlib import Path

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


def create_app(test_config=None):
    """Create and configure flask app."""
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.jinja_env.filters["markdown"] = markdown_no_p
    app.config.from_mapping(
        SECRET_KEY="dev",
        APP_DATABASE=Path(app.instance_path) / "officiumdivinum.sqlite",
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        Path(app.instance_path).mkdir()
    except FileExistsError:
        pass

    return app


def init():
    from . import database

    database.init()
