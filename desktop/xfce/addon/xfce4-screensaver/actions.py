#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
	autotools.configure("--prefix=/usr --sysconfdir=/etc \
	\
	--enable-authentication-scheme=pam \
	--enable-locking \
	--enable-pam \
	\
	--disable-static \
	\
	--with-pam-auth-type=system \
	--with-console-kit \
	--with-mit-ext \
	--with-shadow \
	--with-libgl \
	\
	--without-systemd")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("COPYING*", \
	"INSTALL", \
	"NEWS", \
	"README.md")

