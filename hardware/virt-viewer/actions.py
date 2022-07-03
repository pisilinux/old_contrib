#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.system('sed -i "/doxygen.sh/d" "spice-0.15.0/meson.build"')
    mesontools.configure()

def build():
    mesontools.build("meson --prefix=/usr")
    #shelltools.system("ninja -C build")

def check():
    mesontools.build("test")

def install():
    mesontools.install()
    pisitools.dodoc("COPYING", "README.md")
