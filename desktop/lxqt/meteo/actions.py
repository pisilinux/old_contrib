#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pisitools.dosed("setup.py", "lrelease", "lrelease-qt5")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
