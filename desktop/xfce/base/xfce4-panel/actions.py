#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
	autotools.configure("\
	--sysconfdir=/etc \
	--prefix=/usr \
	\
	--disable-gtk-doc \
	--disable-static \
	\
	--enable-introspection \
	--enable-gio-unix \
	--enable-vala \
	--enable-gtk2 \
	--with-x")

	#pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
	#pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
	pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", \
	"COPYING", \
	"NEWS", \
	"README", \
	"TODO")
