#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --enable-wm-session \
                         --enable-i18n \
                         --enable-antialiasing \
                         --enable-shaped-decorations \
                         --enable-gradients")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "CHANGES", "COPYING", "README")
