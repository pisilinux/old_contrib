#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
	shelltools.export(\
	\
	"CFLAGS", \
	\
	"%s -Wno-strict-prototypes \
	-Wno-pointer-sign \
	-Wno-unused-function \
	-Wno-unused-variable \
	-Wno-unused-but-set-variable \
	-Wno-maybe-uninitialized" \
	\
	% get.CFLAGS())

	pythonmodules.compile()

def install():
	pythonmodules.install()

	pisitools.dodoc("PKG-INFO", "README")

