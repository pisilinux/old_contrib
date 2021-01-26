#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

j = ''.join([
    '--enable-introspection ',
    '--disable-examples ',
    '--disable-gtk-doc ',
    '--disable-deprecated ',
    '--disable-static ',
    ])

def setup():
	autotools.configure(j)

	pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("ChangeLog", "CONTRIBUTING.md", "NEWS", "README.md")

