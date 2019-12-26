import time, sys, datetime, logging, os, commands
import Adafruit_DHT
from influxdb import InfluxDBClient
import Module

def main():

    host = "127.0.0.1"
    port = 8086
    user = ""
    passwd = ""
    dbname = "Test"
    sensor = Adafruit_DHT.DHT11
    sensor_gpip = 4
    output = "/home/pi/Work/dht22/Collect/data/test.log"
    measurement = "dht11"

    # Create class to read and write dht11 data
    Test_dht11 = Module.Collection(host, port, user, passwd, dbname, measurement, sensor, sensor_gpip, output)

    Test_dht11.check_IP()
    Test_dht11.run_collection()

main()
