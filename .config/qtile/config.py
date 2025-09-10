import os
import subprocess

from libqtile import hook

from settings.bar import screens
from settings.groups import groups
from settings.keys import keys
from settings.keys.system import mod
from settings.layouts import floating_layout, layouts

# --- Standard Qtile config variables ---
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"  # Required for some Java applications


# --- Autostart Hook ---
@hook.subscribe.startup_once
def autostart() -> None:
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])
