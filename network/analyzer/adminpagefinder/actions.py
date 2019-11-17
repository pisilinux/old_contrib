#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i '1i\#!/usr/bin/env python' AdminpageFinder.py.txt")


def install():
    pisitools.insinto("/usr/share/AdminpageFinder/", "AdminpageFinder.py.txt")
    shelltools.chmod(get.installDIR() + "/usr/share/AdminpageFinder/AdminpageFinder.py.txt", mode=0755)
    pisitools.dosym("/usr/share/AdminpageFinder/AdminpageFinder.py.txt", "/usr/bin/adminpagefinder")
