#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = ''.join([
    '--libexecdir=/usr/lib/vte ',
    '--localstatedir=/var ',
    '--enable-introspection ',
    '--enable-python ',
    '--disable-gtk-doc ',
    '--disable-static ',
    '--without-glX ',
    ])

def setup():
	autotools.configure(i)

	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS")

