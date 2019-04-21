#!/usr/bin/python
# -*- coding: utf-8 -*-

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
	--enable-geanygendoc")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("NEWS", "README")
