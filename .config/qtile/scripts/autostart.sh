#!/bin/bash

run_once() {
  if ! pgrep -f "$1" > /dev/null; then
    "$@" &
  fi
}

# 1. Core System Services (Authentication, Notifications, Music)
run_once /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
run_once dunst
run_once mpd

# 2. Visual Setup (Compositor, Wallpaper)
run_once picom
nitrogen --set-scaled --random /usr/share/backgrounds

# 3. Session & Tray Applications (Power Management, Disk Mounting)
run_once xfce4-power-manager
run_once udiskie --tray --notify
