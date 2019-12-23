#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -Wno-strict-overflow" % get.CFLAGS())
    autotools.autoreconf("-i")
    autotools.configure("--with-experimental")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    
def check():
    autotools.make("check")

def install():
    autotools.install("sqlite=true experimental=true pcre=true")
    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE", "README", "VERSION")