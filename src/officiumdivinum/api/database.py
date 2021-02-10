"""
Handle database querying.

By abstracting it here we can just use dicts for testing.
"""
from datetime import timedelta
from pathlib import Path
from typing import Union

import dateutil.parser as dp
import jsonpickle
from translations import invariants

from ..objects import Office
from ..objects import Prime
from ..objects import datastructures  # needed for unpickling.

martyrology = []


def eval_year(year, yearless):
    """

    Parameters
    ----------
    year :

    yearless :

    as_list :
        (Default value = True)

    Returns
    -------


    """
    yeared = {}
    for row in yearless:
        if not row:
            continue
        try:
            date = row.date.resolve(year)
        except AttributeError:
            print(row)
        try:
            yeared[date].append(row)
        except KeyError:
            yeared[date] = [row]

    return yeared


def load_martyrology():
    """"""
    global martyrology
    p = Path("martyrology.json")
    if not p.exists():
        from .api import api

        p = Path(api.root_path) / p
    with p.open() as f:
        raw_tables["martyrology"] = jsonpickle.decode(
            f.read(), classes=[datastructures.Date, datastructures.Martyrology]
        )


years = {}

year_tables = {"martyrology": None}
raw_tables = {}


def assemble_martyrology(candidates: list, year: int):
    """
    Assemble and resolve martyrolgy (easy, as we just stuff them together.)

    Parameters
    ----------
    candidates : list : candidates for the day.

    year : int : year.

    candidates : list :

    year : int :

    candidates: list :

    year: int :


    Returns
    -------
    """
    extra_info = []
    for candidate in candidates:
        try:
            old_date, content = candidate.render(year)
        except AttributeError:
            extra_info += candidate.content
    return old_date, extra_info + content


def raw_query(day, table):
    """
    Query table for data on day.

    Parameters
    ----------
    day :

    table :


    Returns
    -------
    """
    global raw_tables, year_tables
    year = day.year
    try:
        return year_tables[table][year][day]
    except (KeyError, TypeError):
        this_year = eval_year(year, raw_tables[table])
        try:
            year_tables[table][year] = this_year
        except (KeyError, TypeError):
            year_tables[table] = {year: this_year}
        return year_tables[table][year][day]


def martyrology_query(day, table):
    """

    Parameters
    ----------
    day :

    table :


    Returns
    -------


    """
    candidates = raw_query(day, table)
    return assemble_martyrology(candidates, day.year)


def init():
    """Start database."""
    load_martyrology()


offices = {"prime": Prime}


def get_psalm(psalm, language):
    pass


def get_office(
    office: str,
    calendar: str,
    datestr: str,
    language: str,
    translation: Union[str, None],
) -> Office:
    """
    Get a particular office by calendar date.

    Note that this currently just returns a made-up prime office.

    Parameters
    ----------
    office : str : Office name to get.

    calendar : str : Calendar to use.

    datestr : str : Date (as string, to parse with dateutils).

    language: str : Main Language.

    translation: Union[str : Second Language.

    None] : Or not


    Returns
    -------
    Office
          An object based on Office() for the relevant office.
    """
    inv = invariants[language]
    today = dp.parse(datestr).date()
    tomorrow = today + timedelta(days=1)

    office = Prime(
        language,
        [inv["Deus in adjutorium"], inv["gloria"], inv["laus tibi"]],
        inv["iam lucis"],
        datastructures.Antiphon(
            "Misericordia tua, * Domine ante oculos meos: et complacui in veritate tua."
        ),
        [get_psalm("25"), get_psalm("51"), get_psalm("52")],
        martyrology_query(tomorrow, "martyrology"),
        datastructures.Reading(
            "Lectio Brevis",
            "2 Thess 3:5"[
                "Dóminus autem dírigat corda et córpora nostra in caritáte Dei et patiéntia Christi."
            ],
        ),
        inv,
    )

    return office
