#!/bin/sh

#execute this file in your project directory with $ sh ./setup.sh

#install escpos library
sudo pip3 install python-escpos

# back up old rc.local file
sudo mv /etc/rc.local /etc/backup_rc.local
# copy the rc.local file with the printer instructions to /etc
sudo cp rc.local /etc/rc.local

# copy the printer.sh file with the printer instructions to /bin
sudo cp printer.sh /bin/printer.sh
