import os
import subprocess

from libqtile import hook

from settings.bar import screens  # noqa: F401
from settings.constants import font_params as widget_defaults  # noqa: F401
from settings.constants import mod  # noqa: F401
from settings.groups import groups  # noqa: F401
from settings.keys import keys  # noqa: F401
from settings.layouts import floating_layout, layouts  # noqa: F401

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
@hook.subscribe.startup_once  # pyright: ignore[reportUnknownMemberType]
def autostart() -> None:
    home: str = os.path.expanduser(path="~/.config/qtile/scripts/autostart.sh")
    subprocess.run(args=[home])
