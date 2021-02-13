from pathlib import Path

from .api import app

testpage = Path(app.root_path) / "static/test.html"


@app.route("/")
def test_api_page():
    with testpage.open() as f:
        data = f.read()
    return data
