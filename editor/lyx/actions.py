#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "--enable-qt5 \
     --enable-build-type=release \
     --disable-rpath \
     --disable-stdlib-debug \
     --with-enchant \
     --with-hunspell \
     --without-included-boost \
     --without-included-mythes \
    "

def setup():
	shelltools.export("PYTHON", "/usr/bin/python3")
#	autotools.autoreconf("-fi")
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("ANNOUNCE", "NEWS", "README", "UPGRADING")

