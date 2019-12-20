#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	pisitools.cxxflags.add("-O2 -DNDEBUG -Wall -Wno-sign-compare -Wno-unused-function")

def build():
	autotools.make("MATCHCOMPILER=yes FILESDIR=/usr/share/cppcheck HAVE_RULES=yes")

def install():
	autotools.rawInstall("DESTDIR=%s FILESDIR=/usr/share/cppcheck" % get.installDIR())

	pisitools.dodoc("AUTHORS", "COPYING", "readme*")

