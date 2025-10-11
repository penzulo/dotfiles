from libqtile.config import Match
from libqtile.layout import Floating

FLOATING_RULES = [
    *Floating.default_float_rules,
    # Generic dialogs
    Match(role="GtkFileChooserDialog"),
    Match(title="branchdialog"),
    # Git utilities
    Match(wm_class="confirmreset"),
    Match(wm_class="makebranch"),
    Match(wm_class="maketag"),
    # Auth & password prompts
    Match(wm_class="ssh-askpass"),
    Match(wm_class="Pinentry-gtk"),
    # Tools & utilities
    Match(wm_class="qalculate-gtk"),
    Match(wm_class="iwgtk"),
    Match(wm_class="yazi-float"),
]
