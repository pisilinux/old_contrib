#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("NOCONFIGURE", "1")
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-unused-result -Wno-format -Wno-int-conversion -Wno-format-truncation -Wno-unused-result")
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-static --enable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "README")