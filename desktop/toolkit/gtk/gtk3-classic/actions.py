#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    '-Ddemos=true ',
    '-Dtests=false ',
    '-Dexamples=false ',
    '-Dcolord=no ',
    '-Dquartz_backend=false ',
    '-Dwin32_backend=false ',
    '-Dbroadway_backend=true ',
    ])

def setup():
	shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer",""))

	mesontools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.rename("/usr/bin/gtk-update-icon-cache", "gtk3-update-icon-cache")

