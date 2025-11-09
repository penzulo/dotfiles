$env.SSH_AUTH_SOCK = (gpgconf  --list-dirs agent-ssh-socket | str trim)
$env.EDITOR = "helix"
$env.DOCKER_HOST = "unix:///var/run/docker.sock"
$env.GPG_TTY = (tty)
$env.DISPLAY = "Wayland"
