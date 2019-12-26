#!/usr/bin/python

'''
This script is used to set the dynamic IP address for telegraf config file.
You should give the target file like:
    /etc/telegraf/telegraf.d/DHT11/DHT11.conf
'''

import os, commands


tempt_file  = '/home/pi/Work/dht22/Installing/Templates/DHT11.conf'
target_file = '/etc/telegraf/telegraf.d/DHT11/DHT11.conf'


# Get the old IP address in telegraf config files
#cmd = 'cat ' +target_file +  ' |grep required | awk -F \':\' {\'{system("echo " $2)}\'} | awk -F \'/\' {\'{system("echo " $3)}\'}'
#status, old_IP = commands.getstatusoutput(cmd)
old_IP = '127.0.0.1'

# Get the dynamic IP address now
cmd = 'ifconfig  |grep broadcast | awk -F \'netmask\' {\'system("echo " $1)\'} | awk -F \'inet\'  {\'system("echo " $2)\'}'
status, output = commands.getstatusoutput(cmd)
new_IP = str(output)


cmd = 'sudo cp ' + tempt_file + "   " + target_file
os.system(cmd)

cmd = 'sudo sed -i "s/' +old_IP + '/' + new_IP + '/g"   ' + target_file 
os.system(cmd)

cmd = 'sudo systemctl stop telegraf.service'
os.system(cmd)

cmd = 'sudo systemctl start telegraf.service'
os.system(cmd)

