#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_SKIP_RPATH=True \
                          -DCMAKE_INSTALL_PREFIX=/usr" \
                          , sourceDir="..")

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    # 2020-02-27: BlueDeviL's Note: while installing, CMakeLists execute a python script.
    # that script downloads a file from github and copies under /usr/share
    # so, to avoid sandbox violations we will do this process by modifying CMakeLists.txt
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    pisitools.dodoc("README*", "LICENSE*")