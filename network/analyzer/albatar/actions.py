#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    pisitools.insinto("/usr/share/albatar", "albatar.py")
    pisitools.insinto("/usr/share/albatar", "demo.py")
    shelltools.chmod(get.installDIR() + "/usr/share/albatar/albatar.py", mode=0755)
    pisitools.dosym("/usr/share/albatar/albatar.py", "/usr/bin/albatar")