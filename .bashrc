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
export EDITOR="hx"
# export VISUAL="HELIX"
export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)
export DOCKER_HOST="unix:///var/run/docker.sock"
export GPG_TTY=$(tty)
export PAGER="most"
export GROFF_NO_SGR=1

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
alias dot='git --git-dir "$HOME/.dotfiles" --work-tree $HOME'

# Editors
alias vi=nvim
alias vim=nvim
# alias hx=helix not needed on debian

# Zellij
alias zj=zellij

# --- External Tools ---
eval "$(starship init bash)"
eval "$(zoxide init bash)"

# --- Shell Behaviour ---
set -o vi
