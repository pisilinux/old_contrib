#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules


def install():
    pisitools.insinto("/usr/sbin/", "acccheck.pl")
    shelltools.chmod(get.installDIR() + "/usr/sbin/acccheck.pl", mode=0755)
    pisitools.dosym("/usr/sbin/acccheck.pl", "/usr/sbin/acccheck")
    pisitools.dodoc("COPYING*", "README*")
