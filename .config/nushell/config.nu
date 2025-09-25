# ================================
# |         Core Config          |
# ================================
use std/util "path add"
$env.config = {
    buffer_editor: "helix"
    show_banner: false
    ls: {
        use_ls_colors: true
    }
    history: {
        file_format: "sqlite"
        max_size: 100_000
        sync_on_enter: true
        isolation: true
    }
    completions: {
        quick: true
        partial: true
        algorithm: "fuzzy"
    }
}

# ================================
# |     Path Manipulation        |
# ================================
path add $"($nu.home-path)/.bun/bin"
path add $"($nu.home-path)/.cargo/bin"
path add $"($nu.home-path)/.local/bin"


# ================================
# |       External Tools         |
# ================================
# Initialize external tools by sourcing their config files.

source aliases.nu
source vars.nu
source modules/zoxide.nu
source modules/starship.nu
