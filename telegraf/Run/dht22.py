import pigpio
import DHT22
import time
import logging

logging.basicConfig( filename='/home/pi/Work/DHT22/Run/Log/Temp_Humi.log', filemode='a', format='%(created)f %(message)s',
        level=logging.INFO )

pi = pigpio.pi()
dht22 = DHT22.sensor(pi, 4)
dht22.trigger()

def readDHT22():
    dht22.trigger()
    humidity = '%.2f' % (dht22.humidity())
    temp     = '%.2f' % (dht22.temperature())
    return ( humidity, temp )

while True:
    humidity, temperature = readDHT22()
    h = float(humidity)
    t = float(temperature)
    if h>0 and t>0 :
        #print("Humidity is: " + humidity + "%")
        logging.info('Temp={0:0.1f}C and Humidity={1:0.1f}%'.format(t, h))
        break
    time.sleep(0.5)
    #if humidity >0 and temperature>0:
    #    print("Humidity is: " + humidity + "%")
    #    print("Temperature is: " + temperature + "C")
    #    time.sleep(1)
