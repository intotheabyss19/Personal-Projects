#!/bin/bash

group="$1"
[[ -z "$group" ]] && exit 1

cache="${XDG_CACHE_HOME:-$HOME/.cache}/i3_current_group"
echo "$group" >"$cache"

# Jump to first workspace in the group
ws=$(i3-msg -t get_workspaces | jq -r ".[].name" | grep "^${group}\." | head -n1)

if [[ -n "$ws" ]]; then
  i3-msg workspace "$ws"
fi
