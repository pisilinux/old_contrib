#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5

WorkDir = "Cutegram-2.7.1-stable/Cutegram"

def setup():
    shelltools.system("qmake -r .. PREFIX=/usr")
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()

    #pisitools.dodoc("LICENSE", "README.md",)
