#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.system("./bootstrap")
	cmaketools.configure("\
	\
	-DCMAKE_BUILD_TYPE=release \
	-DCMAKE_INSTALL_PREFIX=/usr \
	\
	-DBUILD_SHARED_LIBS=ON \
	-DENABLE_DOCUMENTATION=ON")

def build():
	cmaketools.make()

def install():
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("COPYING", "README")

