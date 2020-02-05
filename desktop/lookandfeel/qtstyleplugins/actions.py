#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

def setup():
	shelltools.export("CXXFLAGS", \
	"%s -Wno-deprecated-declarations -Wno-implicit-fallthrough -Wno-unused-result" % \
	get.CXXFLAGS())

	qt5.configure()

def build():
	qt5.make()

def install():
	qt5.install()

