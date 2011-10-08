#!/usr/bin/env python

"""
    pcsc-watcher.py: send PC/SC events as DBus events
    Copyright (C) 2011 Florian "floe" Echtler <floe@butterbrot.org>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import gobject

import dbus
import dbus.service

from dbus.mainloop.glib import DBusGMainLoop

from smartcard.CardMonitoring import *
from smartcard.util import *


# dbus stuff

service = None

interface = "org.debian.alioth.pcsclite"  # also used as bus name
path = "/org/debian/alioth/pcsclite/reader0/slot0"


class PCSC_DBus_Service(dbus.service.Object):
    """ very simple DBus service class with one signal """
    def __init__(self, object_path):
        bus_name = dbus.service.BusName(interface, bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, object_path)

    @dbus.service.signal(interface)
    def CardPresenceChanged(self, atr, added):
        pass


# smartcard stuff

class PCSC_Card_Observer(CardObserver):
    """ simple card observer class which calls the DBus service """
    def update(self, observable, (addedcards, removedcards)):
        for card in addedcards:
            service.CardPresenceChanged(toHexString(card.atr), True)
        for card in removedcards:
            service.CardPresenceChanged(toHexString(card.atr), False)


# main

DBusGMainLoop(set_as_default=True)
gobject.threads_init()  # very important to avoid starving the PCSC thread

service = PCSC_DBus_Service(path)

cardmonitor = CardMonitor()
cardobserver = PCSC_Card_Observer()
cardmonitor.addObserver(cardobserver)

gobject.MainLoop().run()
