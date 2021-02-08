from jinja2 import Environment
from jinja2 import PackageLoader

env = Environment(loader=PackageLoader("officiumdivinum.objects", "templates/"))

verse_template = env.get_template("verse.html")
