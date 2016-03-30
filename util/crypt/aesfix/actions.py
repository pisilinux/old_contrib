#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

    
def build():
    autotools.make()

def install():
    pisitools.dobin("aesfix")
    pisitools.insinto("/usr/share/aesfix/","samples/")
    pisitools.dodoc("LICENSE", "README")
