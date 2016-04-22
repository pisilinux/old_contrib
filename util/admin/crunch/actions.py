#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

    
def build():
    autotools.make()

def install():
    pisitools.dobin("crunch")
    pisitools.dodoc("COPYING")
    pisitools.doman("crunch.1")
    pisitools.insinto("/usr/share/crunch/", "charset.lst")
