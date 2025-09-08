# ░███    ░██              ░██████   ░██                   ░██ ░██ 
# ░████   ░██             ░██   ░██  ░██                   ░██ ░██ 
# ░██░██  ░██ ░██    ░██ ░██         ░████████   ░███████  ░██ ░██ 
# ░██ ░██ ░██ ░██    ░██  ░████████  ░██    ░██ ░██    ░██ ░██ ░██ 
# ░██  ░██░██ ░██    ░██         ░██ ░██    ░██ ░█████████ ░██ ░██ 
# ░██   ░████ ░██   ░███  ░██   ░██  ░██    ░██ ░██        ░██ ░██ 
# ░██    ░███  ░█████░██   ░██████   ░██    ░██  ░███████  ░██ ░██ 
                                                                 
# ================================
# |         Core Config          |
# ================================
# Set Nushell's internal behavior.
$env.config = {
    buffer_editor: "nvim"
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
# |       External Tools         |
# ================================
# Initialize external tools by sourcing their config files.

source aliases.nu
source modules/zoxide.nu
source modules/starship.nu
