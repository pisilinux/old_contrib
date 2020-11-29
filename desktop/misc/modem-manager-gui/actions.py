#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
	pisitools.dosed("meson.build", "19.1", "20")
	pisitools.dosed("meson.build", "^po4a", "#po4a")
	pisitools.dosed("meson.build", "\'man\'", deleteLine = True)
	pisitools.dosed("Makefile", "\ man\ ", deleteLine = True)
	mesontools.configure()

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "Changelog")

