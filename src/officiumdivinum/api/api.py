from flask_api import FlaskAPI
from flaskext.markdown import Markdown

api = FlaskAPI(__name__)
md = Markdown(api)
