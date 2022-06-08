#!/bin/bash
echo "WARNING: This script will update and install requirements, add it as an apt source and Check this."
echo ""
echo "If you do not want this, please press ctrl + C to cancel the script."
echo ""
echo "The script will start in 10 seconds."

sleep 10

echo "Running Update eLysBot app setup..."
echo "Run in sudo eLysBot for the next time."

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

clear

sudo chmod +x /etc/

clear

sudo chmod +x /usr/share/doc

clear

sudo rm -rf /usr/share/doc/eLys/

clear

cd /etc/

clear

sudo rm -rf /etc/eLys

clear

mkdir hackingtool

clear

cd elys

clear

git clone https://github.com/AeX03/eLys

clear

cd eLys

clear

sudo chmod +x QuickCheck.sh

clear

sudo python3 eLysBot.pyw

clear
