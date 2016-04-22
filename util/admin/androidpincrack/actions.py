#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def install():
    pisitools.insinto("/usr/bin/", "AndroidPINCrack.py")
    shelltools.chmod(get.installDIR() + "/usr/bin/AndroidPINCrack.py", mode=0755)
    pisitools.dosym("/usr/bin/AndroidPINCrack.py", "/usr/bin/androidpincrack")
    pisitools.insinto("/usr/share/doc/AndroidPINCrack/", "README.md")
