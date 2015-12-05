#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools

WorkDir = "Cutegram-2.7.0-stable/Cutegram"

def setup():
    shelltools.system("qmake-qt5 -r .. PREFIX=/usr")
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()

    #pisitools.dodoc("LICENSE", "README.md",)