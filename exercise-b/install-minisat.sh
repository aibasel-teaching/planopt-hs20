#!/bin/bash

sudo apt-get install -y wget
wget http://minisat.se/downloads/MiniSat_v1.14_linux
chmod u+x MiniSat_v1.14_linux
sudo mv MiniSat_v1.14_linux /usr/bin/minisat
