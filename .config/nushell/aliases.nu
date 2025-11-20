# -- Dotfiles --
alias dot = git --git-dir $"($env.HOME)/.dotfiles" --work-tree $env.HOME

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

# Get IPv4 Address of network interface
def get-ipv4 [interface: string] {
  networkctl status $interface --json=short
  | from json
  | get Addresses
  | where Family == 2
  | get Address
  | each { str join '.' }
  | to text
}

# File copy using cURL for progress
def fcopy [source: path, destdir: path] {
    let src = ($source | path expand)
    let dir = ($destdir | path expand)
    let name = ($src | path basename)
    let dst = $"($dir)/($name)"

    curl -o $dst $"file://($src)"
}
