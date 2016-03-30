#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
WorkDir="ADMIDpack" + "/src/"

def build():
    shelltools.system('make CC="gcc $CFLAGS"')

def install():
    pisitools.dobin("../ADMbin/ADM*")
    pisitools.insinto("/usr/share/doc/admid-pack", "../Docs/*")
