#!/bin/bash

current=$(cat ~/.cache/i3_current_group)
next="a"

if [ "$current" = "a" ]; then
  next="b"
fi

echo "$next" >~/.cache/i3_current_group

# switch to first workspace in the new group if exists
ws=$(i3-msg -t get_workspaces | jq -r --arg g "$next" '
  map(select(.name | startswith($g + ":")))
  | sort_by(.name)
  | .[0].name
')
[ -n "$ws" ] && i3-msg workspace "$ws"
