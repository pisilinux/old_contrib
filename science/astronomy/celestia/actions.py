#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "--enable-pch \
     --enable-cairo \
     --enable-theora \
     --disable-rpath \
     --disable-static \
     --with-gtk \
     --with-lua \
    "

def setup():
	pisitools.dosed("src/celestia/gtk/data/celestia.desktop", "celestia-gtk", "celestia")
	pisitools.flags.add("-fsigned-char")
	autotools.autoreconf("-fi")
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TRANSLATORS")

