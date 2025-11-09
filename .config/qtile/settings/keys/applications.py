from libqtile.config import Key
from libqtile.lazy import lazy

from settings.constants import mod, pterm, sterm

keys: list[Key] = [
    # ============================
    # Core Applications
    # ============================
    Key([mod], "Return", lazy.spawn(pterm), desc="Launch terminal"),
    Key(
        [mod],
        "space",
        lazy.spawn("rofi -show drun -p Applications"),
        desc="Launch Rofi application launcher",
    ),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch Brave web browser"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch Thunar file manager"),
    Key(
        [mod, "shift"],
        "e",
        lazy.spawn(f"{sterm} --class yazi -e yazi"),
        desc="Launch terminal file manager (Yazi)",
    ),
    # ============================
    # Development / Editors
    # ============================
    Key(
        [mod],
        "escape",
        lazy.spawn(f"{pterm} --class helix -e helix"),
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
        "c",
        lazy.spawn("qalculate-gtk"),
        desc="Launch Calculator",
    ),
    Key(
        [mod],
        "m",
        lazy.spawn(f"{pterm} --class ncmpcpp -e ncmpcpp"),
        desc="Launch ncmpcpp music player",
    ),
    Key(
        ["control", "shift"],
        "Escape",
        lazy.spawn(f"{pterm} --class btop -e btop"),
        desc="Launch btop system monitor",
    ),
    Key(
        [mod, "shift"],
        "m",
        lazy.spawn(f"{pterm} --class neomutt -e neomutt"),
        desc="Launch Mail Viewer",
    ),
    Key(
        [mod],
        "s",
        lazy.spawn("rofi -show recursivebrowser"),
        desc="Search for files in home directory",
    ),
    Key(
        [mod],
        "backspace",
        lazy.spawn("rofi -show emoji -no-show-icons"),
        desc="Search for emojis",
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
