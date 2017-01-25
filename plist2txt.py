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

from __future__ import print_function

import plistlib
import sys


def convert(filename):
    root = plistlib.readPlist(filename)
#    for key in root:
#        print key

    n_ifdVendorID = len(root['ifdVendorID'])
    n_ifdProductID = len(root['ifdProductID'])
    n_ifdFriendlyName = len(root['ifdFriendlyName'])
    if n_ifdVendorID != n_ifdProductID or n_ifdVendorID != n_ifdFriendlyName:
        print("Error: wrongs sizes")
        print("ifdVendorID:", n_ifdVendorID)
        print("ifdProductID:", n_ifdProductID)
        print("ifdFriendlyName:", n_ifdFriendlyName)
        return

    zipped = zip(root['ifdVendorID'], root['ifdProductID'],
                 root['ifdFriendlyName'])
    for elt in sorted(zipped):
        print(":".join(elt))

if __name__ == "__main__":
    convert(sys.argv[1])
