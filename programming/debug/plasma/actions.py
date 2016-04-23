#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def setup():
    shelltools.system("./requirements.sh")

def build():
    shelltools.system("python3 setup.py build_ext --inplace")

def install():
    pythonmodules.install(pyVer="3.4")
    pisitools.insinto("/usr/share/plasma/", "run_plasma.py")
    shelltools.chmod(get.installDIR() + "/usr/share/plasma/run_plasma.py", mode=0755)
    pisitools.dosym("/usr/share/plasma/run_plasma.py", "/usr/bin/plasma")
    pisitools.dodoc("LICENSE", "README*")
