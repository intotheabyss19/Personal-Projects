#!/bin/bash

group=$(cat ~/.cache/i3_current_group)
workspace="${group}:$1"
i3-msg "workspace \"$workspace\""
