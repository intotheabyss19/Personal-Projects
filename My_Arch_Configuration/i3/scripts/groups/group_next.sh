#!/bin/bash

group=$(cat "${XDG_CACHE_HOME:-$HOME/.cache}/i3_current_group" 2>/dev/null)
[[ -z "$group" ]] && exit 1

current=$(i3-msg -t get_workspaces | jq -r '.[] | select(.focused==true).name')

workspaces=($(i3-msg -t get_workspaces | jq -r '.[].name' | grep "^${group}\." | sort))

for i in "${!workspaces[@]}"; do
  if [[ "${workspaces[$i]}" == "$current" ]]; then
    next_index=$(((i + 1) % ${#workspaces[@]}))
    i3-msg workspace "${workspaces[$next_index]}"
    exit
  fi
done
