#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
#   pcscd_perfs.py: calculate the cumulative times of pcscd logs
#   Copyright (C) 2010  Ludovic Rousseau
"""

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

# Usage:
# 1. start pcscd in debug mode to generate a trace
#    pcscd --foreground --debug
# 2. copy the trace into a file using Copy/Paste of your terminal
# 3. Make sure the first line of the log file is the first output line
#    00000000 debuglog.c:277:DebugLogSetLevel() debug level=debug
# 4. run the script
#    ./pcscd_perfs.py log

# Log file:
# 00000000 debuglog.c:277:DebugLogSetLevel() debug level=debug
# 00000316 configfile.l:242:DBGetReaderListDir() Parsing conf directory: /etc/reader.conf.d
# 00000029 configfile.l:284:DBGetReaderList() Parsing conf file: /etc/reader.conf.d/0comments

# Output:
# 00000000 00000000 debuglog.c:277:DebugLogSetLevel() debug level=debug
# 00000316 00000316 configfile.l:242:DBGetReaderListDir() Parsing conf directory: /etc/reader.conf.d
# 00000345 00000029 configfile.l:284:DBGetReaderList() Parsing conf file: /etc/reader.conf.d/0comments

# The first column is the cummulative time in µs i.e. the sum of the
# second column


def total_time(file):
    total = 0
    for line in open(file).readlines():
        fields = line.split(' ')
        delta = fields[0]

        # user entered a Ctrl-C
        if delta.startswith('\x03'):
            return

        total += int(delta)
        print("%08d" % total, line, end='')

if __name__ == "__main__":
    import sys

    total_time(sys.argv[1])
