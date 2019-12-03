#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.cd("asio")
    shelltools.system("./autogen.sh")
    autotools.autoreconf("-fiv")
    autotools.configure()

def build():
    shelltools.cd("asio")
    autotools.make()

def check():
    shelltools.cd("asio")
    autotools.make("check")

def install():
    shelltools.cd("asio")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING", "LICENSE*", "README*")
