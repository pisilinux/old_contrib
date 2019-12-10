#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("--enable-debugger \
	--enable-gitchangebar \
	--enable-geanylua \
	--enable-devhelp \
	--enable-geanypy \
	--enable-geanypg \
	--enable-spellcheck \
	--enable-multiterm \
	--enable-geanygendoc \
	--enable-gtkspell=yes")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("NEWS", "README")
