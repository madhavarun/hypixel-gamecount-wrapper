#!/bin/bash
rootdir=$HOME/.config/bspwm/polybar/quakecraftAddiction
lockfile=$HOME/.cache/quakelock
qcplayercount=$(python $rootdir/fetch_count.py LEGACY QUAKECRAFT)
output=$qcplayercount
mincount=2
muted=false

# Mute notifications
if [ -e $lockfile ]; then
	muted=true
	output="$qcplayercount 󰖁"
fi

# If player count is greater than mincount and not muted, send notification
if [[ "$qcplayercount" -ge "$mincount" && "$muted" == false ]]; then
    notify-send "QUAKECRAFT QUEUE POP" "$qcplayercount PLAYERS ON QUAKE"
fi

echo $output
