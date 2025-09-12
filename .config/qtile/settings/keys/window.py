from libqtile.config import Key
from libqtile.core.manager import Qtile
from libqtile.lazy import lazy

from settings.keys.system import mod


# --- Helper function to move window to the next/prev screen ---
def move_window_to_screen(qtile: Qtile, direction: int):
    """
    Moves a window to the next or previous screen.
    Direction: 1 for next screen, -1 for previous screen.
    """
    if not qtile.current_window:
        return

    # Get the index of the current screen
    current_screen_index = qtile.current_screen.index

    # Calculate the destination screen index, wrapping around
    destination_screen_index = (current_screen_index + direction) % len(qtile.screens)

    # Get the group (workspace) on the destination screen
    destination_group = qtile.screens[destination_screen_index].group.name

    # Move the current window to the destination group
    qtile.current_window.togroup(destination_group)


keys: list[Key] = [
    # ============================
    # Focus Control
    # ============================
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to previous monitor"),
    # ============================
    # Window Shifting / Swapping
    # ============================
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        [mod, "shift"],
        "period",
        lazy.function(move_window_to_screen, 1),
        desc="Move window to next screen",
    ),
    Key(
        [mod, "shift"],
        "comma",
        lazy.function(move_window_to_screen, -1),
        desc="Move window to previous screen",
    ),
    # ============================
    # Window Resizing (MonadTall / MonadWide)
    # ============================
    Key([mod], "i", lazy.layout.grow(), desc="Grow window"),
    Key([mod], "o", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # ============================
    # Window State
    # ============================
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
]
