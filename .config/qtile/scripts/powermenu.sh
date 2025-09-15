#!/usr/bin/env bash

# Define the icons for each option using Nerd Font glyphs
# You can find more icons at https://www.nerdfonts.com/cheat-sheet
ICON_LOGOUT="󰗽"
ICON_SUSPEND="󰒲"
ICON_REBOOT="󰜙"
ICON_SHUTDOWN="󰐥"
ICON_LOCK="󰌾"

# Define the options for the power menu, including the icons
options="$ICON_LOGOUT Logout\n$ICON_SUSPEND Suspend\n$ICON_REBOOT Reboot\n$ICON_SHUTDOWN Shutdown\n$ICON_LOCK Lock"

# Show the Rofi menu and get the user's choice
# The -no-show-icons flag is added to prevent Rofi from making space for native icons
chosen=$(echo -e "$options" | rofi -dmenu -p "Power Menu" -i -no-show-icons)

# Execute the corresponding command based on the choice
# We use 'cut' to extract just the text part of the selection
case "$(echo "$chosen" | cut -d' ' -f2)" in
    "Logout")
        loginctl terminate-session ${XDG_SESSION_ID-}
        ;;
    "Suspend")
        systemctl suspend
        ;;
    "Reboot")
        systemctl reboot
        ;;
    "Shutdown")
        systemctl poweroff
        ;;
    "Lock")
        betterlockscreen -l
        ;;
esac
