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
                **font_params,
            ),
            widget.Prompt(),
            widget.WindowName(foreground=colors["aqua"], **font_params),
            widget.Chord(
                chords_colors={"launch": (colors["background"], colors["red"])},
                name_transform=lambda name: name.upper(),
            ),
            widget.Systray(icon_size=20, padding=8),
            widget.Sep(linewidth=0, padding=10),
            widget.Clock(
                format="%Y-%m-%d %a %I:%M %p",
                foreground=colors["orange"],
                **font_params,
            ),
            widget.Sep(linewidth=0, padding=10),
        ],
        26,  # Bar height
        background=colors["background"],
        opacity=0.95,
    )


# --- Dynamic Screen Logic ---
# Use xrandr to get the number of connected monitors
command = "xrandr --query | grep ' connected' | wc -l"
try:
    # Execute the command in a shell
    num_monitors_str = subprocess.check_output(command, shell=True).decode().strip()
    num_monitors = int(num_monitors_str)
except (subprocess.CalledProcessError, ValueError) as e:
    # Fallback to 1 monitor if the command fails
    print(f"Error getting monitor count: {e}. Defaulting to 1.")
    num_monitors = 1

# Create a list of Screen objects, one for each monitor
screens = [Screen(top=create_bar()) for _ in range(num_monitors)]
