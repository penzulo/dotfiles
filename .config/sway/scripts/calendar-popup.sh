#!/usr/bin/env bash

# Get current mouse position
eval "$(swaymsg -t get_seats | jq -r '.[] | .devices[] | select(.type=="pointer") | "X=\(.pointer.x)\nY=\(.pointer.y)"')"

# Set popup dimensions
WIDTH=300
HEIGHT=250

# Offset slightly upward and left of the cursor
XPOS=$((X - WIDTH / 2))
YPOS=$((Y - HEIGHT - 20))

# Show calendar near cursor
yad --calendar \
    --no-buttons \
    --title="Calendar" \
    --undecorated \
    --skip-taskbar \
    --on-top \
    --geometry="${WIDTH}x${HEIGHT}+${XPOS}+${YPOS}" \
    --close-on-unfocus &

