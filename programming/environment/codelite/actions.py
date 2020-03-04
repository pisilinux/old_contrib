#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # BlueDeviL Note: i've fixed codelite's rpath but left wxcrafter's rpath, because if we disable
    # wxcrafter cannot find codelite!
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_CXX_FLAGS='-Wno-write-strings %s' \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DCMAKE_SKIP_RPATH=True\
                          -DENABLE_CLANG=1 \
                          -DENABLE_LLDB=1 \
                          -DWITH_MYSQL=1" % get.CXXFLAGS(), sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    pisitools.dodoc("COPYING", "LICENSE", "README.md")