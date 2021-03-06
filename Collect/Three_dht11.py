import time, sys, datetime, logging, os, commands
import Adafruit_DHT
from influxdb import InfluxDBClient
import Module

def main():

    host = "127.0.0.1"
    port = 8086
    user = ""
    passwd = ""
    dbname = "Three_DHT11"
    sensor = Adafruit_DHT.DHT11
    sensor_gpips = [ 4, 18, 23 ]
    outputs = [ "/home/pi/Work/RPi_dht22/Collect/data/dht11_1.dat",
    		"/home/pi/Work/RPi_dht22/Collect/data/dht11_2.dat",
    		"/home/pi/Work/RPi_dht22/Collect/data/dht11_3.dat"]
		
    measurements = [ "dht11_1", "dht11_2", "dht11_3" ]


    for n in range(3):

       # Newfile=True
       # cmd = 'touch ' + outputs[n]
       # if(not os.path.exists(outputs[n])):
       #     os.system(cmd)
       #     print("lalala " + str(n))


        # Create class to read and write dht11 data
        Test_dht11 = Module.Collection(host, port, user, passwd, dbname, measurements[n], sensor, sensor_gpips[n], outputs[n])

        Test_dht11.check_IP()
        Test_dht11.run_collection()

        #print ( outputs[n] )
	

main()
