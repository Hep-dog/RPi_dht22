#!/usr/bin/python

import time, sys, datetime, logging, os, commands
import Adafruit_DHT
from influxdb import InfluxDBClient


class Collection():

    def __init__(self, host, port, user, passwd, dbname, meas, sensor, sensor_gpip, outname):
        self.host = host
        self.port = port
        self.meas = meas
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.outname= outname
        self.sensor = sensor
        self.sensor_gpip = sensor_gpip

    def check_IP(self):
        cmd = 'ifconfig  |grep broadcast | awk -F \'netmask\' {\'system("echo " $1)\'} | awk -F \'inet\'  {\'system("echo " $2)\'}'
        status, output = commands.getstatusoutput(cmd)
        self.host = str(output)



    def run_collection(self):

        # Set the output file
        logging.basicConfig( filename=self.outname, filemode='a', format='%(message)s', level=logging.INFO)

        while True:
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.sensor_gpip)
            iso = int(round(time.time()*1000000000))
            data = [
                    {
                        "measurement" : self.meas,
                        #                    "tags" : {
                        #                        "location" : location,
                        #                        },
                        "time" : iso,
                        "fields" : {
                            "temperature" : temperature,
                            "humidity"    : humidity
                            }
                        }
                    ]
    
            if temperature is not None and humidity is not None:
                if float(humidity)<100:
                    #logging.info('Temp={0:0.1f}C and Humidity={1:0.1f}%'.format(temperature, humidity))
                    logging.info('{0:18d} Temp={1:0.1f}C and Humidity={2:0.1f}%'.format(iso, temperature, humidity))

                    # Create the InfluxDB client object
                    # The data will be saved locally, even thought the influxdb doesn't works
                    client = InfluxDBClient( self.host, self.port, self.user, self.passwd, self.dbname)
                    client.write_points(data)
                    #print("[%s] Temp: %s, Humidity: %s" % (iso ,temperature, humidity))
                    break

    # This function is used the synchronize the local DHT data the influxdb
    def sync_localdata_DHT(self):
        file = open(self.outname, "r")
        
        while True:
            lines = file.readlines()
            if not lines:
                break
            for line in lines:
                iso  = int(line.split(" ")[0])
                temp = float(((line.split(" ")[1]).split("Temp=")[1]).split("C")[0])
                humi = float(((line.split(" ")[3]).split("dity=")[1]).split("%")[0])
                #print(iso, temp, humi)

                data = [
                        {
                            "measurement" : self.meas,
                            #                    "tags" : {
                            #                        "location" : location,
                            #                        },
                            "time" : iso,
                            "fields" : {
                                "temperature" : temp,
                                "humidity"    : humi
                                }
                            }
                        ]
                if temp is not None and humi is not None:
                    if float(humi)<100:
                        # Create the InfluxDB client object
                        client = InfluxDBClient( self.host, self.port, self.user, self.passwd, self.dbname)
                        client.write_points(data)
                        #print("[%s] Temp: %s, Humidity: %s" % (iso ,temperature, humidity))
        
        file.close()


def main():

    host = "127.0.0.1"
    port = 8086
    user = ""
    passwd = ""
    dbname = "sync"
    sensor = Adafruit_DHT.DHT11
    sensor_gpip = 4
    output = "/home/pi/Work/dht22/Collect/data/test.log"
    measurement = "dht11"

    # Create class to read and write dht11 data
    Test_dht11 = Collection(host, port, user, passwd, dbname, measurement, sensor, sensor_gpip, output)

    Test_dht11.check_IP()
    print(Test_dht11.host)
    Test_dht11.run_collection()
    Test_dht11.sync_localdata_DHT()

if __name__ == "__main__":
    main()
