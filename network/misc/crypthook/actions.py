#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

    
def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/share/crypthook", "crypthook.so")
    shelltools.chmod(get.installDIR() + "/usr/share/crypthook/crypthook.so", mode=0755)
    pisitools.dodoc("README*")
