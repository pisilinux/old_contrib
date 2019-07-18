#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
#	pisitools.dosed("libffmpegthumbnailer/pngwriter.cpp", "#include <cassert>", "#include <cassert>\n#include <cstring>")
	cmaketools.configure("\
	-DCMAKE_INSTALL_DIR=/usr \
	-DCMAKE_INSTALL_LIBDIR=lib \
	-DENABLE_THUMBNAILER=ON \
	-DENABLE_GIO=ON")

def build():
	cmaketools.make()

def install():
	cmaketools.install()

	# Empty files: NEWS, TODO
	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README.md")
