#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="beautifulsoup4-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir, "build_python3")
    shelltools.cd(WorkDir)

def build():
    pythonmodules.compile()

    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.compile(pyVer = "3")

def install():
    pythonmodules.install("--optimize=1 --skip-build")
    
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.install(pyVer = "3")
    pisitools.dodoc("COPYING.txt", \
    "LICENSE", \
    "NEWS.txt", \
    "README.md")
