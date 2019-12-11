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

#WorkDir = "shiboken2-master"

def setup():
    shelltools.cd("sources/shiboken2")
    shelltools.makedirs("build3")
    shelltools.cd("build3")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DBUILD_TESTS=OFF \
                          -DUSE_PYTHON_VERSION=3", sourceDir="..")


def build():
    shelltools.cd("sources/shiboken2/build3")
    autotools.make()

def install():
    shelltools.cd("sources/shiboken2/build3")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())


