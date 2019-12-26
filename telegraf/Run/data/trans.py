#!/bin/python

import os

cmd = "rsync -az -e  'ssh -p 26700' --progress /home/pi/Work/DHT22/Run/data/Temp_Humi_DHT22_1.log root@95.169.9.61:/root/Work/data/Humi_Tempt/DHT22_1"

os.system(cmd)
