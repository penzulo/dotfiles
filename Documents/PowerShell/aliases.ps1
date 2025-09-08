# ===============================
# PowerShell Dotfiles & Aliases
# ===============================

# --------------
# Dotfiles Git Wrapper
# --------------

function dotgit {
    param (
        [Parameter(ValueFromRemainingArguments = $true)]
        [string[]]$Args
    )
    & git --git-dir="$HOME/.dotfiles" --work-tree="$HOME" @Args
}

# --------------
# eza File Listing Shortcuts
# --------------

function eza-ls {
    param (
        [Parameter(ValueFromRemainingArguments = $true)]
        [string[]]$Args
    )
    if (Get-Command eza -ErrorAction SilentlyContinue) {
        & eza @Args
    } else {
        Write-Warning "eza is not installed or not in PATH."
    }
}

function ll  { eza-ls -l --icons @args }
function la  { eza-ls -a --icons @args }
function lla { eza-ls -la --icons @args }
function li   { eza-ls --icons @args }

# --------------
# Git Shortcuts
# --------------

function g     { git @args }
function ga    { git add @args }
function gs    { git status @args }
function gco   { git checkout @args }
function gcm   { git commit -m @args }
function gpush { git push @args }
function gpull { git pull @args }

# ===============================
# End of Config
# ===============================
