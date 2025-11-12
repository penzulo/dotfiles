#!/usr/bin/env bash
set -euo pipefail

WALLPAPER_DIR="/usr/share/backgrounds"
INTERVAL=600  # 10 minutes
MODE="fill"

# Build a shuffled wallpaper list once
mapfile -t WALLPAPERS < <(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) | shuf)

index=0
pid=""

set_wallpaper() {
  local file="$1"
  echo "Setting wallpaper: $file"
  swaybg -m "$MODE" -i "$file" &
  new_pid=$!

  # Give swaybg time to start before killing old one
  sleep 1
  if [[ -n "$pid" ]]; then
    kill "$pid" 2>/dev/null || true
  fi
  pid=$new_pid
}

# Handle Ctrl+C cleanly
trap '[[ -n "$pid" ]] && kill "$pid"; exit 0' SIGINT SIGTERM

# Start loop
while true; do
  set_wallpaper "${WALLPAPERS[index]}"
  ((index=(index+1)%${#WALLPAPERS[@]}))
  sleep "$INTERVAL"
done
