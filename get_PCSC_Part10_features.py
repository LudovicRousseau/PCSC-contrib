#!/usr/bin/env python3

"""
#   get_PCSC_Part10_features.py: get and parse CM_IOCTL_GET_FEATURE_REQUEST
#   and FEATURE_GET_TLV_PROPERTIES results
#   Copyright (C) 2023  Ludovic Rousseau
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


from smartcard.pcsc.PCSCPart10 import parseFeatureRequest, parseTlvProperties
from smartcard.System import readers
from smartcard.pcsc.PCSCPart10 import SCARD_SHARE_DIRECT
from smartcard.scard import SCARD_CTL_CODE

CM_IOCTL_GET_FEATURE_REQUEST = SCARD_CTL_CODE(3400)

# for each reader
for reader in readers():
    print("Reader:", reader)

    card_connection = reader.createConnection()
    card_connection.connect(mode=SCARD_SHARE_DIRECT)

    data_in = card_connection.control(CM_IOCTL_GET_FEATURE_REQUEST)

    features = dict()
    for (feature, value) in parseFeatureRequest(data_in):
        features[feature] = value
    print("CM_IOCTL_GET_FEATURE_REQUEST results:")
    for feature in features:
        print(" {}: 0x{:X}".format(feature, features[feature]))

    print("  Supports Secure PIN Entry (SPE): ", end="")
    if "FEATURE_VERIFY_PIN_DIRECT" in features:
        print("yes")
    else:
        print("no")

    if "FEATURE_GET_TLV_PROPERTIES" in features:
        print("FEATURE_GET_TLV_PROPERTIES results:")
        data_in = card_connection.control(features["FEATURE_GET_TLV_PROPERTIES"])
        properties = parseTlvProperties(data_in)
        for k, v in list(properties.items()):
            if isinstance(v, int):
                print(" %s: %d or 0x%04X" % (k, v, v))
            else:
                print(" %s: %s" % (k, v))

    print()
