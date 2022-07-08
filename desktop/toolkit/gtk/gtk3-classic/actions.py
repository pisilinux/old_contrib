#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, mesontools, pisitools, get

j = ''.join([
    ' -Dx11_backend=true',
    ' -Dwayland_backend=true',
    ' -Dbroadway_backend=true',
    ' -Dcolord=no',
    ' -Ddemos=false',
    ' -Dtests=false',
    ' -Dexamples=false',
    ' -Dwin32_backend=false',
    ' -Dquartz_backend=false '
    ])

def setup():
	shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer",""))
	mesontools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()
	pisitools.rename("/usr/bin/gtk-update-icon-cache", "gtk3-update-icon-cache")
