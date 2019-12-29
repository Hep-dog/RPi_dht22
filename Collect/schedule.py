#!/usr/bin/python
# Run the DHT22 sensor temperature and humidity reading 30 time per minute

import os, time

#cmd = 'sudo python /home/pi/Work/RPi_dht22/Collect/Three_dht11.py'
cmd = 'sudo python /home/pi/Work/RPi_dht22/Collect/run.py'
for t in range(1, 60, 30):
    os.system(cmd)
    time.sleep(30)
