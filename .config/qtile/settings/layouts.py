from libqtile.config import Match
from libqtile.layout import Floating, Max, MonadTall, Stack, TreeTab
from libqtile.layout.base import Layout

from .theme import colors, font_params, layout_theme

layouts: list[Layout] = [
    MonadTall(**layout_theme),
    Max(**layout_theme),
    Stack(**layout_theme),
    TreeTab(
        font=font_params.get("font", "JetBrainsMono Nerd Font"),
        fontsize=12,
        sections=["FIRST", "SECOND"],
        section_fontsize=12,
        border_width=2,
        bg_color=colors["background"],
        active_bg=colors["purple"],
        active_fg=colors["background"],
        inactive_bg=colors["gray"],
        inactive_fg=colors["foreground"],
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200,
    ),
]

floating_layout: Floating = Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(wm_class="Pinentry-gtk"),  # GPG key password entry
        Match(wm_class="iwgtk"),  # GPG key password entry
    ],
    **layout_theme,  # Apply the same border styling
)
