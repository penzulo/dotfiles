#!/usr/bin/env bash

# Array of "label|icon-name" pairs
entries=(
  "Logout|system-log-out"
  "Suspend|system-suspend"
  "Reboot|system-reboot"
  "Shutdown|system-shutdown"
  "Lock|system-lock-screen"
)

# Build the rofi input with icons
options=""
for entry in "${entries[@]}"; do
  label="${entry%%|*}"
  icon="${entry##*|}"
  options+="$label\0icon\x1f$icon\n"
done

# Run rofi with icons enabled
choice=$(echo -en "$options" | rofi -dmenu -p "Power Menu" -i -show-icons)

case "$choice" in
  Logout)   loginctl terminate-session "${XDG_SESSION_ID-}" ;;
  Suspend)  systemctl suspend ;;
  Reboot)   systemctl reboot ;;
  Shutdown) systemctl poweroff ;;
  Lock)     betterlockscreen -l ;;
esac
