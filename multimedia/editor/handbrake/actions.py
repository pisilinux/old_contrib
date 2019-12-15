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
	shelltools.cd("gtk")
#	pisitools.dosed("configure.ac", "AM_CONFIG_HEADER", "AC_CONFIG_HEADERS")
#	pisitools.dosed("configure.ac", "AM_PROG_CC_STDC", "AC_PROG_CC")
	autotools.autoreconf("-fiv")
	shelltools.cd("..")
	autotools.rawConfigure("--prefix=/usr --force \
	\
	--enable-qsv \
	--enable-x265 \
	--enable-numa \
	--enable-fdk-aac \
	--enable-libav-aac \
	\
	--disable-rpath \
	--disable-static \
	--disable-silent-rules")

def build():
	shelltools.cd("build")
	autotools.make()

def install():
	shelltools.cd("build")
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	shelltools.cd("..")
	pisitools.dodoc(\
	\
	"AUTHORS.markdown", \
	"COPYING", \
	"LICENSE", \
	"NEWS.markdown", \
	"README.markdown", "THANKS.markdown")

