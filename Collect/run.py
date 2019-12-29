import time, sys, datetime, logging, os, commands
import Adafruit_DHT
#from influxdb import InfluxDBClient
import Module

def main():

    host = "127.0.0.1"
    port = 8086
    user = ""
    passwd = ""
    dbname = "Three_DHT11"
    sensor = Adafruit_DHT.DHT11
    sensor_gpips = [ 4 ]
    outputs = [ "/home/pi/Work/RPi_dht22/Collect/data/dht11_4.dat" ]
		
    measurements = [ "dht11_4" ]


    for n in range(len(sensor_gpips)):

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
