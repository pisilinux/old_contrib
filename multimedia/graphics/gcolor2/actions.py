#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

def setup():
	pisitools.dosed("configure", "\[:space:\]", "[&]")
	autotools.configure()

def build():
	autotools.make("CFLAGS+='-fcommon'")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodir("/usr/share/applications")
	pisitools.dodoc("AUTHORS")
