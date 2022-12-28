#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, mesontools, pisitools, get

i = ''.join([
    ' --prefix=/usr',
    ' -Dbroadway_backend=true',
    ' -Dxinerama=yes',
    ' -Dgtk_doc=false',
    ' -Dcloudproviders=true '
    ])

def setup():
	#shelltools.unlink('testsuite/gtk/gtkresources.c')
	shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer",""))

	mesontools.configure(i)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("NEWS")

	pisitools.rename("/usr/bin/gtk-update-icon-cache", "gtk3-update-icon-cache")
