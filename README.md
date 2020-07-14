### This project is used to read the temperature and humidity values using the DHT11/DHT22 sensor for Raspberry
### The core package is the Adafruit_DHT ( https://github.com/adafruit/Adafruit_Python_DHT )
### This repository is used to read data from multi DHT sensors
### Any problem you can contact: shenpx91@gmail.com

Two methods listed in this reposity, to transfer the data to influxdb and display it using the grafana:

1. Using the InfluxDBCilent (in Collect  directory)
2. Using the telegraf       (in telegraf directory) 

The first one is easy for configuration and modularizing for multi and different sensors,
so we take it as the official method in the further work.

======================== How to use =========================

For Raspberry Pi Client:

    We use the class named "Collection" in Module.py, to read, record and transfer data,
    there are several parameters should be give firstly, and the data fomat:

		host = host		// The IP address for influxdb. The default value is ok, which can be obtained with the function "Check_IP"
		port = port		// Port for influxdb, default is ok
		meas = meas     // Name for measurement in influxdb
		user = user     // User for influxdb, could be null
		passwd = passwd // Password for User in influxdb, could be null
		dbname = dbname // Name of the database
		outname= outname	// Name of the output file to save the data locally
		sensor = sensor		// Name of sensor for AdafruitDHT, like "Adafruit_DHT.DHT11"
		sensor_gpip = sensor_gpip // the gpio BCM number of the sensor

    the example for RPi to collect data is the script named "run.py" in Collect directory

Then we use rsync + inotify to synchronize data from RPi client to Ubuntu server.
More detailed descriptions can be found in the Sync directory


For the Ubuntu server:

    We transfer the data to influxdb with the functions defined in class "Collection".
    Then we run the main function in "Display" every minutes by crontab.

    One note: The data didn't updated to influxdb when using the crontab, caused by
    the environment of crontab not same as shell (the command "ifconfig" couldn't be found).
    We use the absolute directory for the files and commands to fix this.


Note:

    Since we use the rsync to synchronize data from RPi clients to Ubuntu server,
    the data in server will be lost if those in clients are lost.
    So we add the script in directory "Backup" to backup data day by day.
    In this way, the origin data could be keey the size for latest few days
    to save storage, because all data are backup in server.
    One should add the running of the backup script to crontab with per day schedule.

======================== Install and setup ==================

The softwares used:

1.  Influxdb  ( database )
2.  Telegraf  ( optional, input the local results obtained from sensor readout to Influxdb )
3.  Grafana   ( Visualization of the data in database )


	A. The configure file named "Setup.sh" is used for installing influxdb, grafana, telegraf automatically;

	B. The config_influxdb.py is used for setting the directory for influxdb database;


Descriptions from other people familar with Adafruit_DHT_reader:

(Link:	www.sopwith.ismellsmoke.net/?p=400)

    The Adafruit_DHT.read_retry( sensor, pin ) function call will attempt to read data from the sensor 15 times in 2
	second intervals. It returns as soon as is has valid data. This means the function call can take up to 30 seconds
	to return results. After 15 reties it gives up and return None values for the temp and humidity...
	... If you need a temp/humi reading more than once or twice a minute, this device is not for you.


To synchronize data to other storage, we use crontab to run rsync on schedule ( 30min )
	
	1. Use ssh-keygen to generate the ssh key (need named as id_rsa), than ssh-copy-id to remote server;
	2. When using the crontab, you should use the user "pi", which means that you should use:
		'crontab -e' instead of 'sudo crontab -e'
	
    To transfer the data to host using rsync:
        1. Using the ssh-key to avoid the password request:
            ssh-keygen; ssh-copy-id the key to host
        2. rsync -az -e  'ssh -p 26700' --progress /home/pi/Work/DHT22/Run/data/Temp_Humi_DHT22_1.log 
            root@95.169.9.61:/root/Work/data/Humi_Tempt/DHT22_1
            (26700 is the ssh port, root@95.169.9.61 is the user and ip address of host)


Since there will be large log files in the /var/log directory during the influxdb and telegraf running,
and the Raspberry Pi system may be stuck due to this reason.

So the regular cleaning of these files is performed by running the script named "Clean_log.py" in Installing
directory, and it will be executed hourly with the crontab

