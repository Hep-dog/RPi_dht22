#!/usr/bin/python

import os, commands

cmd = 'rsync -az -e "ssh -oPort=9999" --progress /home/pi/Work/RPi_dht22/Collect/data/dht11_4.dat root@95.169.9.89:/root/Work/data/Test'
os.system(cmd)
