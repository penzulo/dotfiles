from typing import Literal

from libqtile.config import Key
from libqtile.lazy import lazy

from settings.cheatsheet import show_keybindings

mod: Literal["mod4"] = "mod4"

# A list of system-related keybindings
keys: list[Key] = [
    # --- Qtile / Config ---
    Key([mod], "c", lazy.function(show_keybindings), desc="Show keybinding cheatsheet"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # --- Screenshots ---
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Take a screenshot"),
    # --- System ---
    Key([mod, "control"], "l", lazy.spawn("betterlockscreen -l"), desc="Lock screen"),
    Key(
        [mod],
        "x",
        lazy.spawn('sh -c "~/.config/qtile/scripts/powermenu.sh"'),
        desc="Show power menu",
    ),
    # --- Audio ---
    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle"), desc="Play/Pause music"),
    Key([], "XF86AudioNext", lazy.spawn("mpc next"), desc="Next track"),
    Key([], "XF86AudioPrev", lazy.spawn("mpc prev"), desc="Previous track"),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+"),
        desc="Increase volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"),
        desc="Decrease volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),
        desc="Mute volume",
    ),
    # --- Brightness ---
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5%"),
        desc="Increase brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),
        desc="Decrease brightness",
    ),
]
