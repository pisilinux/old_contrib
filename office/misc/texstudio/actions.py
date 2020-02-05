#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

def setup():
	pisitools.cxxflags.add("-Wno-deprecated-declarations")
	qt5.configure("texstudio.pro", parameters='USE_SYSTEM_QUAZIP=1 USE_SYSTEM_HUNSPELL=1')

def build():
	qt5.make()

def install():
	qt5.install()

	pisitools.dodoc("COPYING", "README.md")

