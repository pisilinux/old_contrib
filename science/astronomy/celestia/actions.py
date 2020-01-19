#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
#	pisitools.flags.add("-fsigned-char")
	autotools.autoreconf("-fi")
	autotools.configure("\
	\
	--enable-pch \
	--enable-cairo \
	--enable-theora \
	--enable-new-ldflags \
	\
	--with-gtk \
	--with-pic \
	--with-lua \
	\
	--disable-rpath \
	--disable-static \
	\
	--without-arts")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc(\
	"ABOUT-NLS", "AUTHORS", "COPYING", "README", "TRANSLATORS", "locale/COPYING_*")

