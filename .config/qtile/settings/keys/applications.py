from typing import Literal

from libqtile.config import Key
from libqtile.lazy import lazy

from .system import mod

terminal: str = "alacritty"

keys: list[Key] = [
    # ============================
    # Core Applications
    # ============================
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod],
        "space",
        lazy.spawn("rofi -show drun"),
        desc="Launch Rofi application launcher",
    ),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Firefox web browser"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch Thunar file manager"),
    Key(
        [mod, "shift"],
        "e",
        lazy.spawn(f"{terminal} --class yazi -e yazi"),
        desc="Launch terminal file manager (Yazi)",
    ),
    # ============================
    # Development / Editors
    # ============================
    Key(
        [mod],
        "escape",
        lazy.spawn(f"{terminal} --class helix -e helix"),
        desc="Launch Helix editor",
    ),
    # ============================
    # Productivity / Utilities
    # ============================
    Key(
        [mod],
        "p",
        lazy.spawn("rofi-pass"),
        desc="Launch password manager",
    ),
    Key(
        [mod],
        "m",
        lazy.spawn(f"{terminal} --class ncmpcpp -e ncmpcpp"),
        desc="Launch ncmpcpp music player",
    ),
    Key(
        ["control", "shift"],
        "Escape",
        lazy.spawn(f"{terminal} --class btop -e btop"),
        desc="Launch btop system monitor",
    ),
    Key(
        [mod],
        "s",
        lazy.spawn(
            "sh -c 'fd . ~ | rofi -dmenu -p \"Search\" -i -no-show-icons | xargs -r xdg-open'"
        ),
        desc="Search for files in home directory",
    ),
    # ============================
    # Networking
    # ============================
    Key(
        [mod, "shift"],
        "n",
        lazy.spawn("iwgtk"),
        desc="Show Network menu",
    ),
]
