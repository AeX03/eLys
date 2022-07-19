#!/bin/bash
echo "WARNING: This script will install requirements and add it as an apt source and Check this."
echo ""
echo "If you do not want this, please press ctrl + C to cancel the script."
echo ""
echo "The script will start in 5 seconds."

sleep 5

echo "Running eLysBot app setup..."
echo "						";
echo "         888                        ";
echo "         888                        ";
echo "         888                        ";
echo "  .d88b. 888     888  888.d8888b    ";
echo " d8P  Y8b888     888  88888K        ";
echo " 88888888888     888  888 Y8888b.   ";
echo " Y8b.    888     Y88b 888     X88   ";
echo "   Y8888 88888888  Y88888 88888P    ";
echo "                      888           ";
echo "                 Y8b d88P           ";
echo "                   Y88P"           "";
echo "						";  

sleep 3

# Install Python if necessary
which python3 > /dev/null
status=$?

if test $status -ne 0
then
	echo "Installing Python 3.6..."
	apt-get install python3.6 -y

else
	echo "Confirmed Python is installed."
	
	# Installs Pip even if a Python installation is found because some users don't install pip
	
	sudo apt install python3-pip

fi

# Install Python packages
echo "Installing Python packages..."
python3 -m pip install CMake==3.18.4
python3 -m pip install -r eLys/web-gui/requirements.txt

	echo "Confirmed requirements is installed."

esac
