# Gruvbox Dark color scheme
colors: dict[str, str] = {
    "background": "#282828",
    "background-alt": "#3c3836",
    "foreground": "#ebdbb2",
    "black": "#282828",
    "gray": "#928374",
    "red": "#cc241d",
    "green": "#98971a",
    "yellow": "#d79921",
    "blue": "#458588",
    "purple": "#b16286",
    "aqua": "#689d6a",
    "orange": "#d65d0e",
    "white": "#a89984",
}

# Font settings
font_params: dict[str, str | int] = {"font": "JetBrainsMono Nerd Font", "fontsize": 14}
powerline = {"fontsize": 26, "padding": 0}

# Layout settings
layout_theme: dict[str, str | int] = {
    "border_width": 1,
    "margin": 8,
    "border_focus": colors["foreground"],
    "border_normal": colors["background-alt"],
}

mod = "mod4"
pterm = "alacritty"  # Primary Terminal
sterm = "kitty"  # Secondary Terminal
