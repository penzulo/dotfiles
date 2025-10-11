#!/bin/bash

# 1. Core System Services (Authentication, Notifications, Music)
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &
mpd &

# 2. Visual Setup (Compositor, Wallpaper)
picom &
nitrogen --set-scaled --random /usr/share/backgrounds

# 3. Session & Tray Applications (Power Management, Disk Mounting)
xfce4-power-manager &
udiskie --tray --notify &
