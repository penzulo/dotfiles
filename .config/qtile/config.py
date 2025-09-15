import os
import subprocess
from typing import Any

from libqtile import hook

from settings.bar import screens
from settings.groups import groups
from settings.keys import keys
from settings.keys.system import mod
from settings.layouts import floating_layout, layouts
from settings.theme import font_params as widget_defaults

# --- Standard Qtile config variables ---
dgroups_key_binder: None = None
dgroups_app_rules: list[Any] = []
follow_mouse_focus: bool = True
bring_front_click: bool = False
cursor_warp: bool = False
auto_fullscreen: bool = True
focus_on_window_activation: str = "smart"
reconfigure_screens: bool = True
auto_minimize: bool = True
wmname: str = "LG3D"  # Required for some Java applications


# --- Autostart Hook ---
@hook.subscribe.startup_once
def autostart() -> None:
    home: str = os.path.expanduser(path="~/.config/qtile/scripts/autostart.sh")
    subprocess.run(args=[home])
