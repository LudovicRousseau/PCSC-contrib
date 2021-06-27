#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
#   parse_PCSC_Part10_features.py: parse CM_IOCTL_GET_FEATURE_REQUEST
#   and FEATURE_GET_TLV_PROPERTIES results
#   Copyright (C) 2018  Ludovic Rousseau
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
# replace the bytes returned by the CM_IOCTL_GET_FEATURE_REQUEST control
# code

# CM_IOCTL_GET_FEATURE_REQUEST

# 00000017 ifdhandler.c:1415:IFDHControl() ControlCode: 0x42000D48, usb:08e6/34c2:libudev:0:/dev/bus/usb/003/003 (lun: 10000)
# 00000002 Control TxBuffer: 
# 00000019 Control RxBuffer: 06 04 42 33 00 06 07 04 42 33 00 07 0A 04 42 33 00 0A 12 04 42 33 00 12 

from smartcard.pcsc.PCSCPart10 import parseFeatureRequest, parseTlvProperties
from smartcard.util import toBytes

data = "06 04 42 33 00 06 07 04 42 33 00 07 0A 04 42 33 00 0A 12 04 42 33 00 12"
data_in = toBytes(data)

features = parseFeatureRequest(data_in)
print("CM_IOCTL_GET_FEATURE_REQUEST results:")
for (feature, value) in features:
    print(feature, hex(value))


# FEATURE_GET_TLV_PROPERTIES

# 00000005 ifdhandler.c:1415:IFDHControl() ControlCode: 0x42330012, usb:08e6/34c2:libudev:0:/dev/bus/usb/003/003 (lun: 10000)
# 00000001 Control TxBuffer: 
# 00000006 -> 000001 6B 01 00 00 00 00 09 00 00 00 02 
# 00001664 <- 000001 83 15 00 00 00 00 09 00 00 00 47 65 6D 49 44 42 72 69 64 67 65 20 43 54 37 78 30 41 33 31 6A 
# 00000020 Control RxBuffer: 01 02 11 02 04 02 11 00 05 02 02 00 03 01 00 08 15 47 65 6D 49 44 42 72 69 64 67 65 20 43 54 37 78 30 41 33 31 6A 06 01 04 07 01 10 02 01 02 09 01 00 0B 02 E6 08 0C 02 C2 34 0A 04 00 00 01 00 

data ="01 02 11 02 04 02 11 00 05 02 02 00 03 01 00 08 15 47 65 6D 49 44 42 72 69 64 67 65 20 43 54 37 78 30 41 33 31 6A 06 01 04 07 01 10 02 01 02 09 01 00 0B 02 E6 08 0C 02 C2 34 0A 04 00 00 01 00"
data_in = toBytes(data)

properties = parseTlvProperties(data_in)
print()
print("FEATURE_GET_TLV_PROPERTIES results")
for k, v in list(properties.items()):
    if isinstance(v, int):
        print(" %s: %d or 0x%04X" % (k, v, v))
    else:
        print(" %s: %s" % (k, v))
