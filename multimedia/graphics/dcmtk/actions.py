#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-DCMAKE_BUILD_TYPE=Release \
     -DCMAKE_INSTALL_SYSCONFDIR=/etc \
     -DCMAKE_INSTALL_PREFIX=/usr \
     -DCMAKE_INSTALL_LIBDIR=lib \
     -DBUILD_SHARED_LIBS=ON \
     -DDCMTK_WITH_PNG=ON \
     -DDCMTK_WITH_XML=ON \
     -DDCMTK_WITH_ZLIB=ON \
     -DDCMTK_WITH_TIFF=ON \
     -DDCMTK_WITH_OPENSSL=ON \
     -DDCMTK_WITH_PRIVATE_TAGS=ON \
    "

def setup():
    cmaketools.configure(j)

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
