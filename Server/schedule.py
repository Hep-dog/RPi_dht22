#!/usr/bin/python
# Run the DHT22 sensor temperature and humidity reading 30 time per minute

import os, time

cmd = 'sudo python /home/jiyizi/Work/Coding/Raspberry/RPi_dht22/Server/Display.py"
for t in range(1, 60, 30):
    os.system(cmd)
    time.sleep(30)
