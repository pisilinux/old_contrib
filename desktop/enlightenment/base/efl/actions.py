#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools

j = ''.join([
    ' -Dwl=true',
    ' -Dsdl=true',
    ' -Deeze=true',
    ' -Dbuffer=true',
    ' -Dpixman=true',
    ' -Dxpresent=true',
    ' -Dopengl=full',
    ' -Dsystemd=false',
    ' -Dbuild-tests=false',
    ' -Dbuild-examples=false '
    ])

def setup():
	mesontools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "NEWS")
