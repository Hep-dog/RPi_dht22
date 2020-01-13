#!/bin/bash

remote_ip=192.168.43.84

/usr/bin/inotifywait -mrq -e modify,delete,create,attrib,move /home/pi/Work/RPi_dht22/Collect/data/ | while read events
do
	sudo rsync -av --password-file=/etc/rsyncd.secrets /home/pi/Work/RPi_dht22/Collect/data/ pi@${remote_ip}::dht11
	sudo echo "`date +'%F %T'` have $events" >> /tmp/rsync.log 2>&1
done
