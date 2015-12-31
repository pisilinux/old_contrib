#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools

NoStrip = "/"

def setup():
    #shelltools.system("qmake-qt5 PREFIX=/usr LIBDIR=/usr/lib HEADER=/usr/include")
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()
    
   # pisitools.domove("/usr/local/include/*", "/usr/include/telegramqml/")
   # pisitools.dodir("/usr/include/telegramqml")
    pisitools.insinto("/usr/lib/", "*.so*")
    pisitools.insinto("/usr/include/telegramqml", "*.h")
    pisitools.dodoc("LICENSE", "README.md")