#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i '1i\#!/usr/bin/env python' allthevhosts.py")

def install():
    pisitools.insinto("/usr/bin/", "allthevhosts.py")
    shelltools.chmod(get.installDIR() + "/usr/bin/allthevhosts.py", mode=0755)
    pisitools.dosym("/usr/bin/allthevhosts.py", "/usr/bin/allthevhosts")
