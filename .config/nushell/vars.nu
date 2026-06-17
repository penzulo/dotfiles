# $env.SSH_AUTH_SOCK = (gpgconf  --list-dirs agent-ssh-socket | str trim)
$env.EDITOR = "helix"
$env.LEDGER_FILE = "~/finances/2026.journal"
$env.DOCKER_HOST = "unix:///var/run/docker.sock"
# $env.GPG_TTY = (tty)
# $env.DISPLAY = "Wayland"
$env.PAGER = "most"
$env.GROFF_NO_SGR = 1
