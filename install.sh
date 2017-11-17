#!/usr/bin/env bash

# http://python-wordpress-xmlrpc.readthedocs.io/en/latest/overview.html

# Caso de erro de locals:
# export LC_ALL="en_US.UTF-8"
# export LC_CTYPE="en_US.UTF-8"
# sudo dpkg-reconfigure locales

sudo python3.5 pip install python-wordpress-xmlrpc
sudo python3.5 -m pip install mysqlclient
sudo apt-get install libssl-dev python3-setuptools
sudo python3.5 -m pip install progressbar2
sudo python3.5 -m pip install numpy
