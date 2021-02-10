"""Objects to represent (and if need be render) whole offices."""
from typing import Dict

from .datastructures import Antiphon
from .datastructures import Hymn
from .datastructures import List
from .datastructures import Martyrology
from .datastructures import Psalm
from .datastructures import Reading
from .datastructures import Renderable
from .datastructures import Responsory
from .datastructures import dataclass


@dataclass
class Prime(Renderable):  # use a custom base class if need be
    """Class to represent the office of Prime."""

    name: str
    language: str
    introit: List[Responsory]
    hymn: Hymn
    antiphon: Antiphon
    psalms: List[Psalm]
    post_chapter: List[Responsory]
    martyrology: Martyrology
    chapter: Reading
    invariants: Dict
    template = "prime.html"
