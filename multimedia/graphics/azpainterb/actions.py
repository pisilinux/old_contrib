#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.export("CFLAGS", "%s -Wno-unused-result" % get.CFLAGS())
	autotools.configure()

def build():
	autotools.make("CC=gcc")

def install():
	shelltools.system("DESTDIR=%s make install-strip" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

