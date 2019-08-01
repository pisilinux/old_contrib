# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.system("\
	meson \
	\
	-Dicons=false \
	-Dgtk2-solid-menu=true \
	\
	. build")

def build():
	shelltools.system("ninja -C build")

def install():
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

	pisitools.dodoc("CHANGELOG", "COPYRIGHT", "LICENSE", "README.md")

