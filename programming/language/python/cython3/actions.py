#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "cython-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)

def build():
    pythonmodules.compile()
   
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install("--skip-build")
   
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.install("--skip-build", pyVer="3")
   
    for dirs in ["Doc", "Demos", "tests"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)
       
    pisitools.dodoc("COPYING*", "README*", "USAGE*", "LICENSE*")
