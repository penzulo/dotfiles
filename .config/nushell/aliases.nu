# Alias for dotfiles management
alias dot = git --git-dir $"($env.HOME)/.dotfiles" --work-tree $env.HOME

# Get git status of CWD and format neatly
def gstat [] {
  git s | from json 
}

# Get git status of the dotfiles repo
def dstat [] {
  dot s | from json
}

# -- Editors --
alias vi = nvim
alias vim = nvim
# alias hx = helix not needed on debian

# -- Zellij --
alias zj = zellij

# Get IPv4 Address of network interface
def get-ipv4 [] {
  sys net | where name == "wlan0" | get ip.0 | where protocol == "ipv4"
}

# File copy using cURL for progress
def fcopy [source: path, destdir: path] {
    let src = ($source | path expand)
    let dir = ($destdir | path expand)
    let name = ($src | path basename)
    let dst = $"($dir)/($name)"

    curl -o $dst $"file://($src)"
}

# Pacman packages cleanup
def cleanup-packages [] {
  let packages = (pacman -Qdtq | lines)

  if ($packages | is-empty) {
    print "No orphaned packages found."
  } else {
    sudo pacman  -Rcns ...$packages    
  }
}

# Generate secret of `n` length
def gensec [len: int] {
  random binary $len | encode base64 
}

