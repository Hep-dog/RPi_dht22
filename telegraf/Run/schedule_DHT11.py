#!/usr/bin/python
# Run the DHT22 sensor temperature and humidity reading 30 time per minute

import os, time

cmd = 'python /home/pi/Work/dht22/Run/run_DHT11.py'
for t in range(1, 60, 30):
    #print(t)
    os.system(cmd)
    time.sleep(30)
