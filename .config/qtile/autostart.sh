#!/bin/bash

# Restore wallpaper
nitrogen --restore &

# Start compositor
picom &

# Start network manager applet
# nm-applet &

# Start the notification daemon
dunst &

# Start the music player daemon
mpd &
