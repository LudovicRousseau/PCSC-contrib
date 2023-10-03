#!/bin/bash

set -e

# 4. enable APDU  logging:
# 	sudo defaults write /Library/Preferences/com.apple.security.smartcard Logging -bool yes
# 	please note that APDU logging is not persistent and after reboot or reader replug is disabled
# 5. enable detailed logging:
# 	sudo log config --mode "level:debug"
# 	sudo log config --mode "level:debug,persist:debug" --subsystem com.apple.CryptoTokenKit

# default level
arg=--info

args=`getopt dbe $*` ; errcode=$?; set -- $args

if [ $errcode != 0 ]
then
	echo "Usage: $0 [-d]"
	echo "-d: debug level (default is info level)"
	exit 2
fi

# check the script arguments
for i
do
	case "$i"
	in
		-d)
			arg=--debug
			break;;
	esac
done

log stream --predicate '(process = "usbsmartcardreaderd") || (process = "com.apple.ctkpcscd") || (process = "com.apple.ifdreader") || (process = "com.apple.CryptoTokenKit")' --source $arg
