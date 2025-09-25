import subprocess

from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

from settings.constants import colors, powerline, pterm


def powerline_sep(
    prev_bg: str, next_bg: str, direction: str = "left", end: bool = False
) -> widget.TextBox:
    """Return a powerline separator TextBox with correct colors."""
    chars = {
        ("left", False): "",
        ("left", True): "",
        ("right", False): "",
        ("right", True): "",
    }
    char = chars.get((direction, end), "")
    return widget.TextBox(char, foreground=next_bg, background=prev_bg, **powerline)


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
                padding_x=8,
                padding_y=4,
                hide_unused=True,
                background=colors["purple"],
            ),
            powerline_sep(
                colors["background"], colors["purple"], direction="right", end=True
            ),
            widget.Spacer(),
            powerline_sep(
                colors["background"],
                colors["yellow"],
                direction="left",
                end=True,
            ),
            widget.Clock(
                format="󰥔 %B %d %H:%M",
                background=colors["yellow"],
                mouse_callbacks={"Button1": lazy.spawn("gsimplecal")},
                padding=10,
            ),
            powerline_sep(colors["yellow"], colors["purple"]),
            widget.CheckUpdates(
                distro="Arch_checkupdates",
                display_format="󰏔 {updates}",
                no_update_string="󰏔 0",
                update_interval=1800,
                background=colors["purple"],
                colour_have_updates=colors["foreground"],
                colour_no_updates=colors["foreground"],
                mouse_callbacks={
                    "Button1": lazy.spawn(f"{pterm} --class pacman -e sudo pacman -Syu")
                },
            ),
            powerline_sep(colors["purple"], colors["blue"]),
            widget.Volume(
                fmt="󰕾 {}",
                background=colors["blue"],
                get_volume_command="wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk '{print int($2 * 100) \"%\"}'",
                padding=8,
            ),
            powerline_sep(colors["blue"], colors["aqua"]),
            widget.Wlan(
                interface="wlan0",
                format="󰤨  {essid}",
                disconnected_message="󰖪",
                background=colors["aqua"],
                padding=8,
                mouse_callbacks={"Button1": lazy.spawn("iwgtk")},
            ),
            powerline_sep(colors["aqua"], colors["green"]),
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
                    "Button1": lazy.spawn(f"{pterm} --class btop -e btop")
                },
            ),
            powerline_sep(colors["green"], colors["orange"]),
            widget.Systray(background=colors["orange"], icon_size=20, padding=6),
        ],
        26,
        background=colors["background"],
        margin=[8, 8, 0, 8],
    )


# --- Dynamic Screen Logic ---
# Use xrandr to get the number of connected monitors
command: str = "xrandr --query | rg ' connected' | wc -l"
try:
    num_monitors = len(
        [
            m
            for m in subprocess.check_output("xrandr --query", shell=True)
            .decode()
            .splitlines()
            if " connected" in m
        ]
    )
except (subprocess.CalledProcessError, ValueError) as e:
    # Fallback to 1 monitor if the command fails
    print(f"Error getting monitor count: {e}. Defaulting to 1.")
    num_monitors: int = 1

# Create a list of Screen objects, one for each monitor
screens: list[Screen] = [Screen(top=create_bar()) for _ in range(num_monitors)]
