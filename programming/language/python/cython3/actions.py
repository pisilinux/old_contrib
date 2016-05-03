#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Cython-%s" % get.srcVERSION()

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    pisitools.dodoc("COPYING*", "README*", "PKG-INFO")
    pisitools.domove("/usr/bin/cygdb","/usr/bin/cygdb3")
    pisitools.domove("/usr/bin/cythonize","/usr/bin/cythonize3")
    pisitools.domove("/usr/bin/cython","/usr/bin/cython3")

