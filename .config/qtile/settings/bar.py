import subprocess

from libqtile.bar import Bar
from libqtile.config import Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from settings.constants import colors, pterm


def create_bar() -> Bar:
    """Returns a configured bar object."""
    powerline_config = {
        "decorations": [
            PowerLineDecoration(path="back_slash"),
        ]
    }
    return Bar(
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
                **powerline_config,
            ),
            widget.Spacer(),
            widget.Clock(
                format="󰥔 %B %d %H:%M",
                background=colors["yellow"],
                mouse_callbacks={"Button1": lazy.spawn("gsimplecal")},
                padding=10,
                **powerline_config,
            ),
            widget.CheckUpdates(
                distro="Arch_checkupdates",
                display_format="󰏔 {updates}",
                no_update_string="󰏔 0",
                update_interval=3600,
                background=colors["purple"],
                colour_have_updates=colors["foreground"],
                colour_no_updates=colors["foreground"],
                **powerline_config,
                mouse_callbacks={
                    "Button1": lazy.spawn(f"{pterm} --class pacman -e sudo pacman -Syu")
                },
            ),
            widget.Volume(
                fmt="󰕾 {}",
                background=colors["blue"],
                get_volume_command="wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk '{print int($2 * 100) \"%\"}'",
                padding=8,
                **powerline_config,
            ),
            widget.Wlan(
                interface="wlan0",
                format="󰤨  {essid}",
                disconnected_message="󰖪",
                background=colors["aqua"],
                padding=8,
                mouse_callbacks={"Button1": lazy.spawn("iwgtk")},
                **powerline_config,
            ),
            widget.Battery(
                charge_char="󰂄",
                discharge_char="󱟞",
                empty_char="󱟥",
                full_char="󰁹",
                not_charging_char="󱉞",
                unknown_char="󱟩",
                update_interval=30,
                show_short_text=False,
                background=colors["green"],
                low_foreground=colors["red"],
                low_percentage=0.20,
                format="{char} {percent:2.0%}",
                mouse_callbacks={
                    "Button1": lazy.spawn(f"{pterm} --class btop -e btop")
                },
                **powerline_config,
            ),
            widget.Systray(
                background=colors["orange"], icon_size=20, padding=6, **powerline_config
            ),
        ],
        26,
        background=colors["background"],
        margin=[8, 8, 0, 8],
    )


def get_num_monitors() -> int:
    """Return the number of connected monitors using xrandr."""
    try:
        output = subprocess.check_output(["xrandr", "--query"], text=True)
        return sum(" connected" in line for line in output.splitlines())
    except subprocess.SubprocessError as e:
        print(f"[Qtile] Monitor detection failed: {e}. Defaulting to 1 monitor.")
        return 1


num_monitors: int = get_num_monitors()
screens: list[Screen] = [Screen(top=create_bar()) for _ in range(num_monitors)]
