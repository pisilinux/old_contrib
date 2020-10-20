#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

z = "-Wno-strict-prototypes -Wno-stringop-truncation \
-Wno-pointer-sign -Wno-unused-function -Wno-unused-variable \
-Wno-unused-but-set-variable -Wno-maybe-uninitialized"

def build():
	pisitools.cflags.add(z)

	pythonmodules.compile()

def install():
	pythonmodules.install()

	pisitools.dodoc("PKG-INFO", "README")

