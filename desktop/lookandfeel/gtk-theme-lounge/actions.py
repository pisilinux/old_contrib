#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.system("sed -i '91a\ \ GtkMenuBar::window-dragging\ =\ 1' src/gtk2/main.rc.in")
	shelltools.system("sed -i '92a\ \ GtkToolbar::window-dragging\ =\ 1' src/gtk2/main.rc.in")
#	shelltools.system("sed -i '41s/\#\#/#/' src/gtk2/gtkrc.in")

	shelltools.system("\
	meson \
	\
	-Dgtk2_solid_menu=true \
	-Dscale_style=fancy \
	-Dstyle=flat \
	-Dicons=true \
	\
	. build")

def build():
	shelltools.system("ninja -C build")

def install():
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

	pisitools.dodoc("CHANGELOG", "COPYRIGHT", "LICENSE", "README.md")

