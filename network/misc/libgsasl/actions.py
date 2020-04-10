#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("AUTOPOINT", "true")

    #autotools.autoreconf("-fi")
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-deprecated-declarations")
    autotools.configure("--disable-static")
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("COPYING*", "README*")