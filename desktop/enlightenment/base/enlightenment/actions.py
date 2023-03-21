#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools

j = ''.join([
    ' -Dwl-wl=true',
    ' -Dwl-drm=true',
    ' -Dmount-eeze=true',
    ' -Dsystemd=false',
    ' -Dgeolocation=false '
    ])

def setup():
	mesontools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "NEWS")
