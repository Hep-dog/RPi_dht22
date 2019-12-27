#!/usr/bin/evn python

import time, sys, datetime, logging, os
import Server_module
from influxdb import InfluxDBClient

def main():

    host = "127.0.0.1"
    port = 8086
    user = ""
    passwd = ""
    dbname = "DHT11"
    sensor = "DHT11"
    sensor_gpip = 16
    outputs = [ "/home/jiyizi/Work/Coding/Raspberry/RPi_dht22/Collect/data/dht11_1.dat",
                "/home/jiyizi/Work/Coding/Raspberry/RPi_dht22/Collect/data/dht11_2.dat",
                "/home/jiyizi/Work/Coding/Raspberry/RPi_dht22/Collect/data/dht11_3.dat",
                "/home/jiyizi/Work/Coding/Raspberry/RPi_dht22/Collect/data/dht11_4.dat"
              ]
    measurement = [ "dht11_1", "dht11_2", "dht11_3", "dht11_4" ]

    # Create class to read and write dht11 data
    for n in range(len(outputs)):

        dht11 = Server_module.Collection(host, port, user, passwd, dbname, measurement[n], sensor, sensor_gpip, outputs[n])
        dht11.check_IP()
        dht11.sync_localdata_DHT()

main()
