#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("\
	\
	--enable-debugger \
	--enable-gitchangebar \
	--enable-geanylua \
	--enable-geanypy \
	--enable-geanypg \
	--enable-utilslib \
	--enable-spellcheck \
	--enable-geanygendoc \
	--enable-gtkspell=yes \
	\
	--disable-devhelp \
	--disable-markdown \
	--disable-webhelper \
	--disable-geanypy \
	--disable-multiterm")

def build():
	autotools.make()

def check():
	autotools.make("check")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("NEWS", "README")

