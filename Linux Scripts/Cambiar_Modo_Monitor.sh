#!/bin/bash

iwconfig

echo "Especifique la wlan quieres cambiar de modo monitor"

read wlan

sudo ip link set $wlan down

sudo iw $wlan set type managed

sudo ip link set $wlan up

sudo service NetworkManager start

iwconfig
