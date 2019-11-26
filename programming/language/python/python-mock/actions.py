#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("rm %s/mock-3.0.5/mock/tests/testhelpers_py3.py" % get.workDIR())

def build():
    pythonmodules.compile()
    
    #pythonmodules.run("setup.py build_sphinx")
    
def check():
    pythonmodules.compile("test")

def install():
    pythonmodules.install()