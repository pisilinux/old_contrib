#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
	pisitools.dosed("src/reader/reader_app/reader_app_config.c", "12", "1")
	pisitools.dosed("res/simple-fb2-reader.css", "font-family", deleteLine = True)
	shelltools.echo("res/simple-fb2-reader.css", ".book_textview {\n	font-family: Noto Serif;\n}")

	cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr")

def build():
	cmaketools.make()

def install():
	cmaketools.install()

	pisitools.dodoc("AUTHORS", "COPYING", "INSTALL", "NEWS", "README")
