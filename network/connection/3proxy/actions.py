#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's|/usr/bin/install|/bin/install|g' Makefile.Linux")
    shelltools.system("sed -i 's|/usr/local|/usr|g' Makefile.Linux")
    shelltools.system("sed -i 's|-s ||g' Makefile.Linux")
    shelltools.system("sed -i 's|-Wall -g -O2|$CFLAGS|g' Makefile.Linux")
    shelltools.system("sed -i 's|\$(prefix)/etc/|/etc/|g' Makefile.Linux")

def build():
    autotools.make("-f Makefile.Linux prefix=/usr")

def install():
    pisitools.insinto("/usr/bin", "src/3proxy")
    pisitools.insinto("/usr/share/doc/", "doc/")
    pisitools.doman("man/*.8")
    pisitools.dodoc("authors", "copying", "README", "Release*")
