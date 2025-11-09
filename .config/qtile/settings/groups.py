from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from settings.constants import mod
from settings.keys import keys
from settings.schemas import GroupProperties

# --- GROUP CONFIGURATION ---
# The properties for each group.
# Note: Using Nerd Font icons for labels is a common practice for a clean look.
# Make sure you have a Nerd Font installed and configured in your constants.py.
group_props: list[GroupProperties] = [
    {
        "name": "DEV",
        "key": "1",
        "label": "󰆍",
        "layout": "monadtall",
        "matches": [Match(wm_class="helix")],
    },
    {
        "name": "WWW",
        "key": "2",
        "label": "",
        "layout": "monadtall",
        "matches": [Match(wm_class=m) for m in ("brave-browser", "firefox")],
    },
    {
        "name": "SYS",
        "key": "3",
        "label": "",
        "layout": "monadtall",
        "matches": [Match(wm_class=m) for m in ("pacman", "thunar", "yazi", "btop")],
    },
    {
        "name": "DOC",
        "key": "4",
        "label": "󰈙",
        "layout": "monadtall",
        "matches": [Match(wm_class="ONLYOFFICE")],
    },
    {
        "name": "MUS",
        "key": "5",
        "label": "",
        "layout": "monadtall",
        "matches": [Match(wm_class="ncmpcpp")],
    },
    {
        "name": "VID",
        "key": "6",
        "label": "",
        "layout": "monadtall",
        "matches": [Match(wm_class=m) for m in ("mpv", "vlc")],
    },
]

# --- GROUP OBJECTS AND KEYBINDINGS ---
# This section programmatically creates the Group objects and their
# corresponding keybindings based on the group_props list.
groups: list[Group] = []
for props in group_props:
    # Create a Group object for each entry in group_props
    groups.append(
        Group(
            name=props["name"],
            layout=props.get("layout", "monadtall"),
            label=props.get("label", props["name"]),
            matches=props.get("matches", []),
        )
    )

    # Add keybindings for switching to and moving windows to the group
    keys.extend(
        [
            # MOD + KEY -> Switch to group
            Key(
                [mod],
                props["key"],
                lazy.group[props["name"]].toscreen(),
                desc=f"Switch to group {props['name']}",
            ),
            # MOD + SHIFT + KEY -> Move focused window to group
            Key(
                [mod, "shift"],
                props["key"],
                lazy.window.togroup(
                    props["name"], switch_group=False
                ),  # Use switch_group=False to not follow the window
                desc=f"Move focused window to group {props['name']}",
            ),
        ]
    )
