#!/bin/bash

# Get the volume and mute status from wpctl
STATUS=$(wpctl get-volume @DEFAULT_AUDIO_SINK@)

# Check if muted
if [[ "$STATUS" == *"[MUTED]"* ]]; then
  echo "M"
else
  # If not muted, extract the volume as a percentage
  echo "$STATUS" | awk '{print int($2 * 100) "%"}'
fi
