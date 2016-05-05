#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="yara-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-crypto --enable-magic")

def build():
    autotools.make()

    shelltools.cd("yara-python")
    pythonmodules.compile(pyVer="2.7")
    pythonmodules.compile(pyVer="3")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "CONTRIBUTORS", "README*", "COPYING")
    pisitools.insinto("/usr/share/doc/yara/", "docs/")

    shelltools.cd("yara-python")
    pythonmodules.install(pyVer="2.7")
    pythonmodules.install(pyVer="3")
