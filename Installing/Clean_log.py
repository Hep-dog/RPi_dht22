#!/usr/bin/python

import os 

CMDs = []

CMDs.append('sudo tail -n 1000 /var/log/syslog > /tmp/temp')
CMDs.append('sudo mv /tmp/temp /var/log/syslog')
CMDs.append('sudo chmod 600 /var/log/syslog')
CMDs.append('sudo chown root:root /var/log/syslog')
CMDs.append('sudo tail -n 1000 /var/log/daemon.log > /tmp/temp')
CMDs.append('sudo mv /tmp/temp /var/log/daemon.log')
CMDs.append('sudo chmod 600 /var/log/daemon.log')
CMDs.append('sudo chown root:root /var/log/daemon.log')


for cmd in CMDs:
    #print(cmd)
    os.system(cmd)

