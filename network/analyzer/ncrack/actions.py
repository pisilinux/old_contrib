#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "ncrack-%sALPHA" % get.srcVERSION()

def setup():
    # suppress compiler warning
    pisitools.cflags.add("-Wno-stringop-truncation -Wno-implicit-function-declaration -Wno-stringop-overflow -Wno-format-overflow")
    pisitools.cxxflags.add("-Wno-stringop-truncation -Wno-class-memaccess -Wno-array-bounds -Wno-format-overflow")
    autotools.configure("--without-openssl-header-check")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README*")