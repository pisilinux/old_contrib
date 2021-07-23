#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

f = ''.join([
    '-Wno-discarded-qualifiers ',
    '-Wno-deprecated-declarations ',
    '-Wno-incompatible-pointer-types '
    ])

def setup():
    pisitools.cflags.add(f)
    autotools.configure("--disable-static --disable-schemas-compile --disable-introspection")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
