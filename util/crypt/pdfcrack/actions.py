#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
#
#def setup():
#    pisitools.dosed("Makefile", "gcc", "%s" % get.CC())

def build():
    autotools.make()
    #autotools.make("CFLAGS=\"%s\"" % get.CFLAGS())

def install():
    pisitools.dobin("pdfcrack")

    pisitools.dodoc("COPYING", "README*", "TODO", "changelog")
