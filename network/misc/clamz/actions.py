#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    pisitools.dosed("Makefile","LDFLAGS = ", "LDFLAGS = -Wl,-O1,--as-needed ")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #pisitools.remove("/usr/share/applications/mimeinfo.cache")
    pisitools.insinto("/usr/share/applications", "clamz.desktop")
    pisitools.dodoc("COPYING", "README")
