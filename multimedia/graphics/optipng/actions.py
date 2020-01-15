#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.rawConfigure("\
	-prefix=/usr -mandir=/usr/share/man -with-system-zlib -with-system-libpng")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dohtml("doc/*.html")
	pisitools.dodoc(\
	"AUTHORS.txt", "LICENSE.txt", "README.txt", "doc/history.txt", "doc/todo.txt")

