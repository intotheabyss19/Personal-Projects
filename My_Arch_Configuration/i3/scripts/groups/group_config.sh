#!/bin/bash
# Stores current group (e.g., a, b, c)
echo "$1" >"${XDG_CACHE_HOME:-$HOME/.cache}/i3_current_group"
