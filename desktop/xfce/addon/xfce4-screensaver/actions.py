#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
	autotools.configure("\
	--sysconfdir=/etc \
	--prefix=/usr \
	--disable-static \
	--enable-authentication-scheme=pam \
	--enable-locking \
	--enable-pam \
	--with-pam-auth-type=system \
	--with-console-kit \
	--with-mit-ext \
	--with-shadow \
	--with-libgl")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("COPYING*", \
	"INSTALL", \
	"NEWS", \
	"README.md")
