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

    language: str
    intro: List[Responsory]
    hymn: Hymn
    antiphon: Antiphon
    psalms: List[Psalm]
    martyrology: Martyrology
    chapter: Reading
    invariants: Dict
