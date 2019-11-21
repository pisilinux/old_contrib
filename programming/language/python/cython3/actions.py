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
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)

def build():
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -Wl,-O1 -Wl,-z,relro -Wl,--hash-style=gnu -Wl,--as-needed -Wl,--sort-common")
    shelltools.export("CFLAGS", "-fno-strict-aliasing -mtune=generic -march=x86-64 -O2 -pipe -fstack-protector -D_FORTIFY_SOURCE=2 -g -fPIC -fwrapv -DNDEBUG -g -fwrapv -O3 -Wno-strict-aliasing")
    pythonmodules.compile()
   
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install()
   
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.install(pyVer="3")
   
    for dirs in ["Doc", "Demos", "tests"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)
       
    pisitools.dodoc("COPYING*", "README*", "USAGE*", "LICENSE*")
