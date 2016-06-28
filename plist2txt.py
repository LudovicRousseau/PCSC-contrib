#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#   plist2txt.py: convert a Info.plist file to a text list
#   Copyright (C) 2016  Ludovic Rousseau
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
# ./plist2txt.py /usr/lib/pcsc/drivers/ifd-ccid.bundle/Contents/Info.plist


import plistlib
import sys


def convert(filename):
    root = plistlib.readPlist(filename)
    for key in root:
        print key
    zipped = zip(root['ifdVendorID'], root['ifdProductID'],
                 root['ifdFriendlyName'])
    for elt in sorted(zipped):
        print elt

if __name__ == "__main__":
    convert(sys.argv[1])
