import os
import subprocess

from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

from settings.keys.applications import terminal
from settings.theme import colors, powerline


def create_bar() -> bar.Bar:
    """Returns a configured bar object."""
    return bar.Bar(
        [
            widget.GroupBox(
                active=colors["foreground"],
                inactive=colors["gray"],
                highlight_method="text",
                this_current_screen_border=colors["background-alt"],
                block_highlight_text_color=colors["foreground"],
                padding_x=10,
                hide_unused=True,
                background=colors["purple"],
            ),
            widget.TextBox(
                "",
                foreground=colors["purple"],
                **powerline,
            ),
            widget.Spacer(),
            widget.TextBox(
                "",
                foreground=colors["background"],
                **powerline,
            ),
            widget.Clock(
                format="󰥔 %B %d %H:%M",
                background=colors["background"],
                mouse_callbacks={"Button1": lazy.spawn("gsimplecal")},
            ),
            widget.TextBox(
                "",
                foreground=colors["purple"],
                background=colors["background"],
                **powerline,
            ),
            widget.CheckUpdates(
                distr="Arch",
                display_format="󰏔 {updates}",
                no_update_string="󰏔 0",
                background=colors["purple"],
                colour_have_updates=colors["foreground"],
                colour_no_updates=colors["foreground"],
            ),
            widget.TextBox(
                "", foreground=colors["blue"], background=colors["purple"], **powerline
            ),
            widget.Volume(
                fmt="󰕾 {}",
                background=colors["blue"],
                get_volume_command=os.path.expanduser(
                    path="~/.config/qtile/scripts/volume.sh"
                ),
            ),
            widget.TextBox(
                "", foreground=colors["aqua"], background=colors["blue"], **powerline
            ),
            widget.Wlan(
                interface="wlan0",
                format="󰤨  {essid}",
                disconnected_message="󰖪",
                background=colors["aqua"],
                padding=15,
                mouse_callbacks={"Button1": lazy.spawn("iwgtk")},
            ),
            widget.TextBox(
                "", foreground=colors["green"], background=colors["aqua"], **powerline
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
                background=colors["green"],
                low_foreground=colors["red"],
                low_percentage=0.20,
                format="{char} {percent:2.0%}",
                mouse_callbacks={
                    "Button1": lazy.spawn(f"{terminal} --class btop -e btop")
                },
            ),
            widget.TextBox(
                "",
                foreground=colors["orange"],
                background=colors["green"],
                **powerline,
            ),
            widget.Systray(background=colors["orange"], icon_size=20, padding=10),
        ],
        26,
    )


# --- Dynamic Screen Logic ---
# Use xrandr to get the number of connected monitors
command: str = "xrandr --query | rg ' connected' | wc -l"
try:
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
