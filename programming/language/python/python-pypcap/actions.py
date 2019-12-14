#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing -Wno-unused-function -Wno-implicit-function-declaration -Wno-deprecated-declarations" % get.CFLAGS())
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    pythonmodules.compile()
    
    #pythonmodules.run("setup.py build_sphinx")
    
def check():
    pythonmodules.compile("test")

def install():
    pythonmodules.install()