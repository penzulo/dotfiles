export EDITOR="helix"
export VISUAL="HELIX"

custom_paths=(
  "$HOME/.cargo/bin",
  "$HOME/.bun/bin",
  "$HOME/.local/bin",
  "$HOME/.local/scripts",
)
for path in "${custom_paths[@]}"; do
    if [[ ":$PATH:" != *":$path:"* ]]; then
        PATH="$path:$PATH"
    fi
done

export PATH
export LEDGER_FILE=~/Documents/Ledger/main.journal
export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)

# --- Aliases ---
alias ..='cd ..'
alias ...='cd ../..'

# Listing files (assuming eza is installed)
alias ls='eza --icons'
alias la='eza -a --icons'
alias ll='eza -l --icons'
alias lla='eza -la --icons'
alias lt='eza --tree --level=2'

# Git
alias g='git'
alias ga='git add'
alias gc='git commit -m'
alias gs='git status'
alias gp='git push'
alias gl='git pull'

# Editors
alias vi=nvim
alias vim=nvim
alias hx=helix

# --- External Tools ---
eval "$(starship init bash)"
eval "$(zoxide init bash)"

# --- Shell Behaviour ---
set -o vi
