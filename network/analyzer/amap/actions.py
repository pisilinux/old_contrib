#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--prefix=/usr/share/amap/")
    
def build():
    autotools.make()

def install():
    pisitools.dobin("amap")
    pisitools.insinto("/usr/bin/", "amap6")
    pisitools.dobin("amapcrap")
    pisitools.insinto("/usr/share/amap/etc/", "appdefs.*")
    pisitools.doman("amap.1")
    pisitools.dodoc("AMAP-LIB-INTERFACE", "CHANGES", "IGNORE", "LICENCE*", "README")
