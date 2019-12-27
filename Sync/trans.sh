#!/bin/bash

/usr/bin/inotifywait -mrq -e modify,delete,create,attrib,move /home/pi/Work/RPi_dht22/Collect/data/ | while read events
do
	sudo rsync -av --delete --password-file=/etc/rsyncd.secrets /home/pi/Work/RPi_dht22/Collect/data/ pi@192.168.137.60::testsource
	sudo echo "`date +'%F %T'` have $events" >> /tmp/rsync.log 2>&1
done

