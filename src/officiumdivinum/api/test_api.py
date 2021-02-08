from pathlib import Path

from .api import api

testpage = Path(api.root_path) / "static/test.html"


@api.route("/")
def test_api_page():
    with testpage.open() as f:
        data = f.read()
    return data
