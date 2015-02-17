#!/bin/bash

cd ~/Desktop/Server

bridges=$(ifconfig | grep bridge)
bridgename="$( cut -d ':' -f 1 <<< "$bridges" )"
ip="$(ifconfig $bridgename | grep inet | cut -d: -f2 | awk '{ print $2}')"

echo "URL for synced devices: http://$ip:8080"
echo "URL for remote control: http://$ip:8080/rc.html"
echo
echo "Starting Server...."
echo
python server.py
