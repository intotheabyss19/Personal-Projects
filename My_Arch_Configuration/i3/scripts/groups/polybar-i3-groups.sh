#!/bin/bash

group=$(cat ~/.cache/i3_current_group)
i3-msg -t get_workspaces |
  jq -r --arg g "$group" '
    map(select(.name | startswith($g + ":")))
    | map(
        if .focused then "%{B#254267} " + (.name | split(":")[1]) + " %{B-}"
        elif .urgent then "%{F#ff5555}" + (.name | split(":")[1]) + "%{F-}"
        else " " + (.name | split(":")[1]) + " "
        end
    )
    | join(" ")
  '
