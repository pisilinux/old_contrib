#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./bootstrap")
    #autotools.autoreconf("-f")
    autotools.configure("--disable-static \
                         --with-aspell \
                         --with-zemberek \
                         --with-myspell-dir=/usr/share/hunspell \
                         --disable-ispell")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.rename("/usr/share/enchant/enchant.ordering", "enchant2.ordering")

    pisitools.dodoc("AUTHORS", "NEWS", "README", "HACKING")
