. "$HOME\Documents\PowerShell\aliases.ps1"

Invoke-Expression (&starship init powershell --print-full-init | Out-String)
Invoke-Expression (&zoxide init powershell | Out-String)
