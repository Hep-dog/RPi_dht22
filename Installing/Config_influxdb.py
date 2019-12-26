#!/usr/bin/python

import os, commands

cmd = 'echo $DHT22_workarea'
status, work_area = commands.getstatusoutput(cmd)
print(work_area)

#  Set directories for influxdb databases: data, meta, and wal-dir
data_area = str(work_area) + 'data/data'
meta_area = str(work_area) + 'data/meta'
wald_area = str(work_area) + 'data/wal'

os.system(' mkdir -p ' + data_area)
os.system(' mkdir -p ' + meta_area)
os.system(' mkdir -p ' + wald_area)
os.system(' sudo chown -R influxdb:influxdb ' + data_area)
os.system(' sudo chown -R influxdb:influxdb ' + meta_area)
os.system(' sudo chown -R influxdb:influxdb ' + wald_area)

#  Set the influxdb config file, and copy it the /etc/influxdb/
Temp_file = str(work_area) + "Installing/Templates/temp_influxdb"
conf_file = str(work_area) + "Installing/Templates/influxdb.conf"
cmd = "cp " + Temp_file + "     " + conf_file
print(cmd)
os.system(cmd)

temp = work_area.replace( "/", r"\/")
cmd = 'sed -i "s/Workarea/' + temp + '/g" ' + conf_file
os.system(cmd)

cmd = 'sudo mv ' + conf_file + '    /etc/influxdb/influxdb.conf'
os.system(cmd)

