#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

j = ''.join([
     '"-Wno-incompatible-pointer-types',
     ' -Wno-unused-but-set-variable',
     ' -Wno-misleading-indentation',
     ' -Wno-maybe-uninitialized',
     ' -Wno-strict-prototypes',
     ' -Wno-unused-function',
     ' -Wno-strict-aliasing',
     ' -Wno-pointer-sign',
     ' -Wno-format "',
    ])

def build():
	pisitools.cflags.add(j)
	pythonmodules.compile()

def install():
	pythonmodules.install()

	pisitools.dodoc("CHANGES.md", "LICENSE.txt", "README.txt")

