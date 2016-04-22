#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def install():
    pisitools.insinto("/usr/bin/", "AndroidSniffer.pl.txt")
    shelltools.chmod(get.installDIR() + "/usr/bin/AndroidSniffer.pl.txt", mode=0755)
    pisitools.dosym("/usr/bin/AndroidSniffer.pl.txt", "/usr/bin/androidsniffer")
