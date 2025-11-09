#!/bin/bash

WALLPAPER_DIR="/usr/share/backgrounds"
INTERVAL=600 # 10 mins

# Start with a random wallpaper
swaybg -i "$(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) | shuf -n1)" -m fill &
OLD_PID=$!

while true; do
    sleep $INTERVAL
    swaybg -i "$(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) | shuf -n1)" -m fill &
    NEXT_PID=$!
    sleep 2
    kill $OLD_PID
    OLD_PID=$NEXT_PID
done

