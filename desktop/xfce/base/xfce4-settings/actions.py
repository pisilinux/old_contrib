#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
	autotools.configure("--prefix=/usr \
	--enable-colord \
	--enable-xrandr \
	--enable-xcursor \
	--enable-gio-unix \
	--enable-libnotify \
	--enable-libxklavier \
	--enable-upower-glib \
	--enable-xorg-libinput \
	--enable-sound-settings \
	--enable-pluggable-dialogs \
	\
	--disable-debug \
	--disable-static")

	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", \
	"COPYING", \
	"NEWS", \
	"README", \
	"TODO")
