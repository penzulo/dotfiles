import subprocess

from libqtile.config import Key
from libqtile.core.manager import Qtile

MODIFIER_MAP = {
    "mod4": "Super",
    "mod1": "Alt",
    "shift": "Shift",
    "control": "Ctrl",
}
KEY_COLUMN_WIDTH = 30


def _format_key(key: Key) -> str:
    """Formats a single Key object into a readable string."""
    modifiers = [MODIFIER_MAP.get(mod, mod) for mod in key.modifiers]
    key_name = str(key.key).upper()
    full_key_str = " + ".join([*modifiers, key_name])
    return f"{full_key_str:<{KEY_COLUMN_WIDTH}} -> {key.desc}"


def show_keybindings(qtile: Qtile) -> None:
    """Generates and displays a searchable list of keybindings in rofi."""
    # ...and accesses the final key list directly from the config attribute.
    keys = qtile.config.keys

    rofi_input = "\n".join(_format_key(key) for key in keys if key.desc)

    command = [
        "rofi",
        "-dmenu",
        "-i",
        "-p",
        "Keybindings",
        "-no-show-icons",
    ]

    subprocess.run(command, input=rofi_input, text=True)
