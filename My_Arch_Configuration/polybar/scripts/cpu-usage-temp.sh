#!/bin/bash

# Overall CPU usage (from top)
OVERALL=$(top -bn1 | grep "Cpu(s)" | awk '{print int($2)}')

# Get raw temperature string (e.g., +47.5°C)
TEMP_RAW=$(sensors | grep -m 1 'Package id 0:' | awk '{print $4}' | tr -d '+°C')

# Fallbacks for AMD or other sensors
if [ -z "$TEMP_RAW" ]; then
  TEMP_RAW=$(sensors | grep -m 1 'Tdie:' | awk '{print $2}' | tr -d '+°C')
fi

if [ -z "$TEMP_RAW" ]; then
  TEMP_RAW=$(sensors | grep -m 1 'temp1:' | awk '{print $2}' | tr -d '+°C')
fi

# Round temperature to nearest integer
TEMP_INT=$(printf "%.0f" "$TEMP_RAW")

# Output for polybar or statusbar
echo " ${OVERALL}%| ${TEMP_INT}°C"
echo "#FFFFFF"
echo "CPU: ${OVERALL}% | Temp: ${TEMP_INT}°C"
