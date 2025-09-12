# -- Dotfiles --
alias dotgit = git --git-dir $"($env.HOME)/.dotfiles" --work-tree $env.HOME

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

# -- Helix --
alias hx = helix
