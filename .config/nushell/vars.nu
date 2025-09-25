$env.SSH_AUTH_SOCK = (gpgconf  --list-dirs agent-ssh-socket | str trim)
$env.LEDGER_FILE = ($env.HOME | path join "Ledger" "main.journal")
$env.EDITOR = "helix"
$env.DOCKER_HOST = "unix:///var/run/docker.sock"
