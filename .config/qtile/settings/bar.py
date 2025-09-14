import subprocess

from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

from .theme import colors
from settings.keys.applications import terminal


def create_bar() -> bar.Bar:
    """Returns a configured bar object."""
    return bar.Bar(
        [
            widget.GroupBox(
                active=colors["foreground"],
                inactive=colors["gray"],
                highlight_method="block",
                this_current_screen_border=colors["purple"],
                block_highlight_text_color=colors["background"],
                padding_x=10,
                hide_unused=True,
            ),
            widget.Spacer(),
            widget.Clock(
                format="%B %d %H:%M",
                foreground=colors["orange"],
                mouse_callbacks={"Button1": lazy.spawn("gsimplecal")},
            ),
            widget.Spacer(),
            widget.Wlan(
                interface="wlan0",
                format="󰤨",
                disconnected_message="󰖪",
                foreground=colors["aqua"],
                padding=15,
                mouse_callbacks={"Button1": lazy.spawn("networkmanager_dmenu")},
            ),
            widget.Battery(
                charge_char="󰂄",
                discharge_char="󱟞",
                empty_char="󱟥",
                full_char="󰁹",
                not_charging_char="󱉞",
                unknown_char="󱟩",
                charge_controller=lambda: (0, 90),
                update_interval=10,
                notify_below=20,
                show_short_text=False,
                low_foreground=colors["red"],
                low_percentage=0.20,
                format="{char} {percent:2.0%}",
                mouse_callbacks={
                    "Button1": lazy.spawn(f"{terminal} --class btop -e btop")
                },
            ),
            widget.Systray(icon_size=15, padding=8),
        ],
        26,
        background=colors["background"],
        opacity=0.85,
    )


# --- Dynamic Screen Logic ---
# Use xrandr to get the number of connected monitors
command: str = "xrandr --query | rg ' connected' | wc -l"
try:
    # Execute the command in a shell
    num_monitors_str: str = (
        subprocess.check_output(args=command, shell=True).decode().strip()
    )
    num_monitors: int = int(num_monitors_str)
except (subprocess.CalledProcessError, ValueError) as e:
    # Fallback to 1 monitor if the command fails
    print(f"Error getting monitor count: {e}. Defaulting to 1.")
    num_monitors: int = 1

# Create a list of Screen objects, one for each monitor
screens: list[Screen] = [Screen(top=create_bar()) for _ in range(num_monitors)]
