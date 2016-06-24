#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="pefile-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)
    
    pisitools.dosed("../build_python3/pefile-2016.3.28/setup.py", \
                    "'pefile.py', 'r'", \
                    "'pefile.py', 'r', encoding='utf-8'")
    
    pisitools.dosed("../build_python3/pefile-2016.3.28/setup.py", \
                    "import sys", \
                    "import sys\nfrom io import open")

def build():
    pythonmodules.compile()

    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.compile(pyVer="3")

def check():
    pythonmodules.compile("check")
    
    shelltools.cd("../build_python3/%s" % WorkDir)
    shelltools.system("python3 setup.py check")

def install():
    pythonmodules.install()
    
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.install(pyVer="3")

    pisitools.dodoc("LICENSE", "MANIFEST*", "README*")
