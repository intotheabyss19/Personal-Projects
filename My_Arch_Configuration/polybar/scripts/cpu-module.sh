#!/bin/bash

# Extract CPU temperature using sensors
TEMP=$(sensors | grep -m 1 'Package id 0:' | awk '{print $4}' | tr -d '+')

# Fallback if 'Package id 0' not found (e.g., on AMD or other layout)
if [ -z "$TEMP" ]; then
  TEMP=$(sensors | grep -m 1 'Tdie:' | awk '{print $2}' | tr -d '+')
fi

# If still not found, pick first temperature
if [ -z "$TEMP" ]; then
  TEMP=$(sensors | grep -m 1 'temp1:' | awk '{print $2}' | tr -d '+')
fi

echo " ${TEMP}"
echo " ${TEMP}"
echo "#FFFFFF"
echo "CPU Temperature: ${TEMP}"
