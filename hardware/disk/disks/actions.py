#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

w = "-Dlogind=none \
     -Dgsd_plugin=false \
     -Dman=true \
    "

def setup():
	mesontools.configure(w)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "TODO")

