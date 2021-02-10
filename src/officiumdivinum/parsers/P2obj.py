"""Parse Divinumofficium's psalm files into Psalm objects."""

import re
from pathlib import Path

from ..api.translations import invariants
from ..objects import Psalm
from ..objects import Verse


def parse_file(fn: Path, lang: str):
    """Parse a Divinumofficium psalm file."""

    verses = []
    with fn.open() as f:
        for line in f.readlines():
            try:
                chapter, verseno, verse = re.search(
                    r"([0-9]+):([0-9]+) (.*)", line
                ).groups()
                verse = Verse(verseno, chapter, "Psalm", verse)
                verses.append(verse)
            except AttributeError:
                verses.append(line.strip())

    return Psalm(verses, fn.stem, invariants[lang.lower()]["gloria"])
