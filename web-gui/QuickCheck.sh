#!/bin/bash
echo "WARNING: This script will install requirements and add it as an apt source and Check this."
echo ""
echo "If you do not want this, please press ctrl + C to cancel the script."
echo ""
echo "The script will start in 10 seconds."

sleep 10

echo "Running eLysBot app setup..."
"
        888                      
        888                      
        888                      
 .d88b. 888     888  888.d8888b  
d8P  Y8b888     888  88888K      
88888888888     888  888 Y8888b. 
Y8b.    888     Y88b 888     X88 
  Y8888 88888888  Y88888 88888P 
                     888         
                Y8b d88P         
                  Y88P"   

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
python3 -m pip install -r requirements.txt

else

	echo "Confirmed requirements is installed."

esac
