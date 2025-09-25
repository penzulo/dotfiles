#!/bin/bash

# Create a temporary file to store the selection
TMP_FILE=$(mktemp)

# Run Yazi, telling it to output the selected file path to our temp file
# Note: We need to redirect stderr to /dev/null to prevent Yazi's UI rendering
# from interfering with Helix's UI when it exits.
kitty --class 'yazi-float' yazi --chooser-file="$TMP_FILE" 2>/dev/null

# If a file was selected, output its path
if [ -s "$TMP_FILE" ]; then
    cat "$TMP_FILE"
fi

# Clean up the temporary file
rm -f "$TMP_FILE"
