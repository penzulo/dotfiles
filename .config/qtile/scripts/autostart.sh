#!/bin/bash

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
picom &
dunst &
udiskie --tray --notify &
mpd &
nitrogen --restore &
