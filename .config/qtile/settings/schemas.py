from typing import NotRequired, TypedDict

from libqtile.config import Match


class GroupProperties(TypedDict):
    """A TypedDict to enfore the structure of group properties"""

    name: str
    key: str
    label: NotRequired[str]
    layout: NotRequired[str]
    matches: NotRequired[list[Match]]
