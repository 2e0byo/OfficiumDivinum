import flask


def render_template(template, **kwargs):
    from ..api.api import api

    with api.app_context(), api.test_request_context():
        return flask.render_template(template, **kwargs)
