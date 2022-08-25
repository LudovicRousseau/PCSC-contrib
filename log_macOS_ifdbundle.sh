#!/bin/bash

set -e

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

log stream --predicate 'process = "com.apple.ifdbundle"' $arg
