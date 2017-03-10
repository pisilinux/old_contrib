#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt5

def setup():
    shelltools.system('qmake-qt5 CONFIG+="configure WITH_I18N" QMAKE_CFLAGS_ISYSTEM= PREFIX=/usr QT5LIBDIR=/usr/lib/qt5 lumina.pro')

def build():
    qt5.make()

def install():
    qt5.install()
    pisitools.dodoc("LICENSE","README*")
