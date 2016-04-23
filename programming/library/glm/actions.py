#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DGLM_TEST_ENABLE=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.domove("/usr/lib64/cmake/*","/usr/lib/cmake")
    pisitools.removeDir("/usr/lib64")

    #pisitools.dodoc("readme.txt", "copying.txt", "doc/glm.pdf")
    pisitools.dohtml("doc/*")
