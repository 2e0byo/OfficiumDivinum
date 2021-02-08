from pathlib import Path

from .api import api

testpage = Path("./officiumdivinum/test.html").resolve()
if not testpage.exists():
    testpage = Path("~/OfficiumDivinum/officiumdivinum/test.html").expanduser()


@api.route("/")
def test_api_page():
    with testpage.open() as f:
        data = f.read()
    return data
