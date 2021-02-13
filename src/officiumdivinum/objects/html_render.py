import flask


def render_template(template, **kwargs):
    from ..api.api import app

    with app.app_context(), app.test_request_context():
        return flask.render_template(template, **kwargs)
