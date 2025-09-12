import subprocess

from libqtile import bar, widget
from libqtile.config import Screen

from .theme import colors, font_params


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
                **font_params,
            ),
            widget.Prompt(),
            widget.Spacer(),
            widget.WindowName(
                foreground=colors["aqua"], width=bar.CALCULATED, **font_params
            ),
            widget.Spacer(),
            widget.Systray(icon_size=20, padding=8),
            widget.Clock(
                format="%Y-%m-%d %a %I:%M %p",
                foreground=colors["orange"],
                **font_params,
            ),
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
    num_monitors_str = (
        subprocess.check_output(args=command, shell=True).decode().strip()
    )
    num_monitors = int(num_monitors_str)
except (subprocess.CalledProcessError, ValueError) as e:
    # Fallback to 1 monitor if the command fails
    print(f"Error getting monitor count: {e}. Defaulting to 1.")
    num_monitors = 1

# Create a list of Screen objects, one for each monitor
screens: list[Screen] = [Screen(top=create_bar()) for _ in range(num_monitors)]
