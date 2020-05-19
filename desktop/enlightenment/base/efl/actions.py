#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

z = "-Dwl=true \
     -Dsdl=true \
     -Deeze=true \
     -Dbuffer=true \
     -Dpixman=true \
     -Dxpresent=true \
     -Dopengl=full \
     -Dsystemd=false \
     -Dbuild-tests=false \
     -Dbuild-examples=false \
    "

def setup():
	shelltools.system("meson --prefix=/usr --libdir=lib %s . build" % z)

def build():
	shelltools.system("ninja -C build")

def install():
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

	pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README")

