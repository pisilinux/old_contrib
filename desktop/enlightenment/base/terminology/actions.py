#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.system("meson --prefix=/usr . build")

def build():
	shelltools.system("ninja -C build")

def install():
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README.md")

