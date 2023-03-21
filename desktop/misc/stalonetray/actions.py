#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

def setup():
	pisitools.dosed("configure.ac", "/usr/share/sgml/docbook/stylesheet/xsl/nwalsh", "/usr/share/xml/docbook/xsl-stylesheets")
	autotools.autoreconf("-fiv")
	autotools.configure("--disable-debug --with-x")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.insinto("/usr/share/doc/stalonetray", "stalonetrayrc.sample.in", "stalonetrayrc")
	pisitools.dodoc("AUTHORS", "NEWS")
