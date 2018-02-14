#!/usr/bin/env bash

# http://python-wordpress-xmlrpc.readthedocs.io/en/latest/overview.html

# Caso de erro de locals:
# export LC_ALL="en_US.UTF-8"
# export LC_CTYPE="en_US.UTF-8"
# sudo dpkg-reconfigure locales
echo "###############################################################"
echo "# Instalação das dependências do projeto                      #"
echo "###############################################################"
echo "Caso de erro de locals, executar os seguintes comandos:"
echo " $ export LC_ALL=\"en_US.UTF-8\""
echo " $ export LC_CTYPE=\"en_US.UTF-8\""
echo " $ sudo dpkg-reconfigure locales"
echo "###############################################################"

sudo apt-get install python3-pip
sudo python3.5 -m pip install --upgrade pip
sudo apt-get install python3-mysqldb
sudo python3.5 -m pip install python-wordpress-xmlrpc
sudo python3.5 -m pip install mysqlclient
sudo apt-get install -y libssl-dev python3-setuptools
sudo python3.5 -m pip install progressbar2
sudo python3.5 -m pip install numpy

echo "###############################################################"
echo "Fim da instalação das dependências."
