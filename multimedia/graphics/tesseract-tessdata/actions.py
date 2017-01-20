#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "cdparanoia-III-10.2"

def install():    
    
    #shelltools.system
    pisitools.insinto("/usr/share/tessdata", "tessdata/tessdata-3.04.00/*.traineddata")

    #pisitools.dodoc("COPYING", "README.md", "ChangeLog", "AUTHORS")
