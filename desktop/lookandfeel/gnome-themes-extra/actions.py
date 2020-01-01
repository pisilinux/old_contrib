#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	pisitools.dosed("themes/Adwaita-dark/gtk-2.0/hacks-dark.rc", "000000", "777777")
	shelltools.system("sed -i '82a\ \ GtkMenuBar::window-dragging\ =\ 1' themes/Adwaita*/gtk-2.0/main.rc")
	shelltools.system("sed -i '83a\ \ GtkToolbar::window-dragging\ =\ 1' themes/Adwaita*/gtk-2.0/main.rc")

	shelltools.cd("./themes/Adwaita/gtk-2.0/")
	pisitools.unlink("./assets/*")
	for f in shelltools.ls("*.sh"):
		shelltools.system("./%s" % f)

	shelltools.cd("../../Adwaita-dark/gtk-2.0/")
	pisitools.unlink("./assets/*")
	for f in shelltools.ls("*.sh"):
		shelltools.system("./%s" % f)

	shelltools.cd("%s/%s" % (get.workDIR(), get.srcDIR()))
	shelltools.system("./autogen.sh --prefix=/usr")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.removeDir("/usr/share/locale")
	pisitools.dodoc("LICENSE", "NEWS", "README.md")

