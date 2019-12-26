### This project is used to read the temperature and humidity values using the DHT11/DHT22 sensor for Raspberry
### The core package is the Adafruit_DHT
### Author: Jiyizi 
### Any problem you can contact: shenpx@ihep.ac.cn

The softwares needed:

1.  Influxdb  ( database )
2.  Telegraf  ( input the local results obtained from sensor readout to Influxdb )
3.  Grafana   ( Visualization of the data in database )


A:  You should run the influxdb and grafana auto after the Raspberry starting-up:
    sudo systemctl enable influxdb
    sudo systemctl enable grafana
    sudo systemctl enable telegraf

    The script to collect data using DHT11/22 sensor is: 
    ./Run/run.py   (collect single data once)

B:  To collect the data collection, we use the crontab command:
    sudo crontab -e  (sudo is needed here)
    the script is ./Run/schedule.py

C:  Notes for the configurations for softwares:

    You should create the database in Influxdb:
    1. influx
    2. create database DHT22

    You should add the configuration file for the telegraf to configuring the data format to database:
    telegraf  --config  temperatureLog.conf  (You should give you local IP and you database name for influxdb)



Useful links for the packages installation:

    1.  Adafruit_DHT:
            https://github.com/adafruit/Adafruit_Python_DHT

    2.  Influxdb, Grafana and Telegraf:
            https://www.terminalbytes.com/temperature-using-raspberry-pi-grafana/

===========================================================
       			Update (2019/8/8):
===========================================================

    Find the bug from influxdb: The influxdb process will use huge memory and lead to the system crash.
    
    Reason: Since there are old configuration files in /etc/telegraf/telegraf.d directory,
    the old measurements in database (dht11) will be merged to new database. The large data samples
    lead to the crash.

    Solution: 
        1.  remove the un-needed configuration files in /eta/telegraf/telegraf.d/

        2.  the default configuration files for the database of influxdb is /etc/influxdb/influxdb.conf.
            We can reset the default configurations like:
            [meta]
            dir = "/home/pi/Data/Influxdb/DHT22_cleanroom_table/influxdb/meta"
            [data]
            dir = "/home/pi/Data/Influxdb/DHT22_cleanroom_table/influxdb/data"
            wal-dir = "/home/pi/Data/Influxdb/DHT22_cleanroom_table/influxdb/wal"
	   
    Please NOTE: If you change the output folder of influxdb database, you should:
                 chown -R influxdb:influxdb  /.... (The new folder)
                 
		 If not, you will get the error: influxb  ...permission deny... blabla


===========================================================
       				Update (2019/8/10)
===========================================================
	
	By using the multiple services method, we use different telegraf configration files,
	to using 3 DHT22 sensors.

    Each sensor has specific database in influxdb, so we can vitualize the 3 datas in grafana


===========================================================
       				Update (2019/8/11)
===========================================================
	Some bugs were finded, the data of three sensors droped frequently.

	I guess that it was caused by the parallel using of AdafruitDHT programm and leads to the conflict of some
	data.

	So I reduce the data reading frequency with 2 times in one minute. And this bugs happended rarely corresponding.


===========================================================
       				Update (2019/8/12)
===========================================================
	Add some descriptions from other people familar with Adafruit_DHT_reader:

    Link:	www.sopwith.ismellsmoke.net/?p=400

    The Adafruit_DHT.read_retry( sensor, pin ) function call will attempt to read data from the sensor 15 times in 2
	second intervals. It returns as soon as is has valid data. This means the function call can take up to 30 seconds
	to return results. After 15 reties it gives up and return None values for the temp and humidity...
	... If you need a temp/humi reading more than once or twice a minute, this device is not for you.


===========================================================
       				Update (2019/8/15)
===========================================================
	Add the script to synchronize DHT22 read data to other places.
	Then we use crontab to run rsync on schedule ( 30min )
	
	Note:
		1. Use ssh-keygen to generate the ssh key (need named as id_rsa), than ssh-copy-id to remote server;
		2. When using the crontab, you should use the user "pi", which means that you should use:
			'crontab -e' instead of 'sudo crontab -e'
	

===========================================================
       				Update (2019/11/2)
===========================================================
    Now we want to synchronize the data from different sub sensors to a host (local network).
    So we trans the data to host using rsync:
        1. Using the ssh-key to avoid the password request:
            ssh-keygen; ssh-copy-id the key to host
        2. rsync -az -e  'ssh -p 26700' --progress /home/pi/Work/DHT22/Run/data/Temp_Humi_DHT22_1.log 
            root@95.169.9.61:/root/Work/data/Humi_Tempt/DHT22_1
            (26700 is the ssh port, root@95.169.9.61 is the user and ip address of host)



===========================================================
       				Update (2019/11/3)
===========================================================
    There is a problem: the telegraf on ubuntu just collect data to influxdb one time!!!
    I don't know what problem causes this.

    To fix this, I just start the telegraf every 2 seconds using the crontab (see the Start_telegraf.py)
    Then kill all the telegraf processes every 10 seconds (see the Stop_telegraf.py)

    Note: The data transfer causes 1 second delay, and the telegraf start-up causes about 2 seconds delay,
          so the total delay of grafana is about 3~4 seconds!!!


===========================================================
       				Update (2019/12/5)
===========================================================
	Adding the config files in Installing directory to install influxdb + grafana + telegraf automatically
	$ source Setup.sh

===========================================================
       				Update (2019/12/6)
===========================================================

	Since there will be large log files in the /var/log directory during the influxdb and telegraf running,
	and the Raspberry Pi system may be stuck due to this reason.

	So the regular cleaning of these files is performed by running the script named "Clean_log.py" in Installing
	directory, and it will be executed hourly with the crontab


===========================================================
       				Update (2019/12/6)
===========================================================
	Add the file to setup influxdb automatically:
	$python ./Installing/Config_influxdb.py


===========================================================
       				Update (2019/12/7)
===========================================================
	Update the method to upate the IP address for telegraf automatically.

	The template file named "DHT11.conf" in .../Installing/Templates directory is added. And the
	default IP address is: 120.0.0.1.

	We should run the Check_IP.py scripy when the system start-up by adding it in the .bashrc:
	python ..../Installing/Check_IP.py

	Then the IP address in /etc/telegraf/telegraf.d/... will be updated automatically


