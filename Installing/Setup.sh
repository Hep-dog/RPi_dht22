#!/usr/bin/bash

sudo apt update		&&
#sudo apt upgrade	&&

sudo wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -	&&
sudo echo "deb https://repos.influxdata.com/debian buster stable" | sudo tee /etc/apt/sources.list.d/influxdb.list	&&

sudo apt update			&&
sudo apt install influxdb		&&
pip install influxdb			&&
#sudo apt install influxdb-client	&&
#sudo apt install telegraf		&&


sudo echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list	&&
sudo wget -qO- https://packages.grafana.com/gpg.key | sudo apt-key add -	&&

sudo apt update			&&
sudo apt install grafana	&&


sudo systemctl enable influxdb.service	&&
sudo systemctl enable grafana-server	&&

cd ../Adafruit_Python_DHT/ &&
sudo python setup.py install
