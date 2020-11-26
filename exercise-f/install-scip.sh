#!/bin/bash

set -e

cd $(dirname $(realpath $0))

if [ ! -f SCIPOptSuite-6.0.2-Linux.deb ]; then
    echo "Please download SCIPOptSuite-6.0.2-Linux.deb from http://scip.zib.de/download.php?fname=SCIPOptSuite-6.0.2-Linux.deb and save the file to this directory."
    exit 1
fi

sudo apt -y install libgfortran4 python3-pip
sudo apt -y install ./SCIPOptSuite-6.0.2-Linux.deb
pip3 install pyscipopt==2.2.3

