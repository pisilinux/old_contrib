#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=/usr/lib \
        -DCMAKE_BUILD_TYPE=Release")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    # Update Turkish translation
    #shelltools.system("lrelease src/translations/keepassx-tr_TR.ts")
   # pisitools.insinto("/usr/share/keepassx/i18n/", "src/translations/*tr*.qm")

    #Remove unused mime info
    #pisitools.removeDir("/usr/share/mimelnk")

    #pisitools.dodoc("changelog", "COPYING")
