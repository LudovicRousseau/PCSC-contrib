#!/bin/bash

#   list_pcsc_applications.sh: list all the applications using PC/SC
#   Copyright (C) 2017  Ludovic Rousseau

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


if ! cat /proc/1/maps &> /dev/null
then
	echo "Run as root to get a complete list"
fi

cd /proc

for p in [0-9]*
do
	if grep libpcsclite.so.1.0.0 $p/maps &> /dev/null
	then
		echo -n "process: " 
		cat $p/cmdline
		echo " ($p)"
	fi
done
