#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # suppress compiler warnings
    shelltools.export("CFLAGS", "%s -Wno-implicit-function-declaration -Wno-int-conversion -Wno-unused-result" % get.CFLAGS())
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared=yaz \
                        --with-xslt \
                        --disable-static")
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*", "LICENSE", "NEWS", "ChangeLog")
