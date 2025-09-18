# -- Dotfiles --
alias dot = git --git-dir $"($env.HOME)/.dotfiles" --work-tree $env.HOME

# -- Listing files (if you have eza installed, otherwise use ls) --
alias ls = eza --icons
alias la = eza -a --icons
alias ll = eza -l --icons
alias lla = eza -la --icons
alias lt = eza --tree --level=2

# -- Git --
alias g = git
alias ga = git add
alias gc = git commit -m
alias gs = git status
alias gp = git push
alias gl = git pull

# -- Editors --
alias vi = nvim
alias vim = nvim
alias hx = helix

# -- Zellij --
alias zj = zellij
