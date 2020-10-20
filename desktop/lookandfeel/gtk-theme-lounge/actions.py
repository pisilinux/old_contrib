#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-Dgtk2_solid_menu=true \
     -Dscale_style=fancy \
     -Dstyle=flat \
     -Dicons=true \
    "

def setup():
	shelltools.system("sed -i '91a\ \ GtkMenuBar::window-dragging\ =\ 1' src/gtk2/main.rc.in")
	shelltools.system("sed -i '92a\ \ GtkToolbar::window-dragging\ =\ 1' src/gtk2/main.rc.in")
	mesontools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("CHANGELOG", "COPYRIGHT", "LICENSE", "README.md")

