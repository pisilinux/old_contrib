# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

WorkDir = "shiboken2-master"

def setup():
    shelltools.makedirs("build3")
    shelltools.cd("build3")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr  \
                        -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                        -DUSE_PYTHON_VERSION=3.4 \
                        -DBUILD_TESTS=OFF \
                        -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.4m \
                        -DPYTHON_LIBRARY=/usr/lib/libpython3.4m.so \
                        -DCMAKE_INSTALL_LIBDIR=/usr/lib", sourceDir="..")


def build():
    shelltools.cd("build3")
    autotools.make()

def install():
    shelltools.cd("build3")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())


