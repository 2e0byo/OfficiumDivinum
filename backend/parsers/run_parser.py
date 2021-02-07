"""
Helper functions to run particular parsers on some or all files.

These are provided since sometimes we read a single file and sometimes
we must read many (with a glob).  Parsers only handle single files, to
aid standardisation.

These functions print their output to stdout, for redirecting to a
file.  They also return it.
"""

from pathlib import Path
from typing import List, Union

from jsonpickle import encode

from ..objects import Feast, Martyrology
from . import K2obj, M2obj, T2obj


def sanctoral_to_json(fn: Path, calendar: str) -> str:
    """

    Parameters
    ----------
    fn : Path : File to parse.

    calendar : str : Calendar to use.

    Returns
    -------
    str
       A Json str.

    """
    days = [K2obj.parse_file(fn, calendar)]
    days = encode(days, indent=2)
    print(days)
    return days


def martyrology_to_json(fn: Path) -> str:
    """

    Parameters
    ----------
    fn : Path : File to parse.



    Returns
    -------
    str
       A Json str.

    """
    day = M2obj.parse_file(fn)
    day = encode(day, indent=2)
    print(day)
    return day


def temporal_to_json(fn: Path, calendar: str) -> str:
    """

    Parameters
    ----------
    fn : Path : The file to parse.

    calendar : str : The Calendar to use.


    Returns
    -------
    str
       A Json str.

    """
    day = T2obj.parse_file(fn, calendar)
    day = encode(day, indent=2)
    print(day)
    return day


def pokemon(
    lang: str, calendar: str, root: str
) -> Union[List[Feast], List[Feast], List[Martyrology]]:
    """
    Catch them all!

    Get all the relevant data for a particular calendar from a
    supplied root (which should be a cloned divinumofficium
    repository's web directory.)

    Parameters
    ----------

    lang: str : The language, e.g. `Latin`.

    calendar: str : The calendar.

    root: str : The root, as a string.

    Returns
    -------
    List
        Lists of Feast and Martyrology objects.
    """
    root = Path(f"{root}/{lang}").expanduser()
    sanctoral = K2obj.parse_file(
        root / f"Tabulae/K{calendar}.txt",
        calendar,
    )
    temporal = []
    for f in (root / "Tempora").glob("*.txt"):
        temporal.append(T2obj.parse_file(f, calendar))

    martyrology = []
    for f in (root / "Martyrologium").glob("*.txt"):
        obj_or_objs = M2obj.parse_file(f)
        if isinstance(obj_or_objs, Martyrology):
            martyrology.append(obj_or_objs)
        else:
            martyrology += obj_or_objs
    return sanctoral, temporal, martyrology


def pokemon_to_json(lang, calendar, root):
    """
    Catch them all!  (In json.)

    Like `pokemon`, but return encoded objects.

    Parameters
    ----------

    lang: str : The language, e.g. `Latin`.

    calendar: str : The calendar.

    root: str : The root, as a string.

    Returns
    -------
    str
       Json str.
    """
    things = pokemon(lang, calendar, root)
    return (encode(i, indent=2) for i in things)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("INF", help="Input file.")
    parser.add_argument("--calendar", help="Select calendar.")
    actions = parser.add_argument_group("Actions")
    actions.add_argument("--martyrology", action="store_true")
    actions.add_argument("--sanctoral", action="store_true")
    actions.add_argument("--temporal", action="store_true")
    actions.add_argument("--pokemon", help="Get them all!  Supply lang.")

    args = parser.parse_args()
    if any([args.sanctoral, args.temporal]) and not args.calendar:
        raise Exception("Calendar needed")

    inf = Path(args.INF).expanduser()

    if args.sanctoral:
        sanctoral_to_json(inf, args.calendar)
    if args.martyrology:
        martyrology_to_json(inf)
    if args.temporal:
        temporal_to_json(inf, args.calendar)
    if args.pokemon:
        pokemon_to_json(args.pokemon, args.calendar, args.INF)
