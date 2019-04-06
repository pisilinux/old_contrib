#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt5

def setup():
    shelltools.system("sed -i 's|{TARGET}|{PREFIX}|g' VaktiSalah.pro")
    shelltools.system("sed -i 's|opt/||g' VaktiSalah.pro")
    shelltools.system("sed -i 's|settings.json|.settings.json|g' main.qml")
    qt5.configure("VaktiSalah.pro")

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.dodoc("LICENSE", "README*")
