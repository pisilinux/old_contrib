#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("python3/Makefile.am", "\) -c 'import xapian'", ") -c 'import xapian'\n\t$(OSX_SIP_HACK_ENV) $(PYTHON3) -m py_compile xapian/__init__.py")
    pisitools.dosed("python3/Makefile.am", "O -c 'import xapian'", "O -c 'import xapian'\n\t$(OSX_SIP_HACK_ENV) $(PYTHON3) -O -m compileall xapian/__init__.py")
    autotools.autoreconf("-vfi")
    shelltools.export("XAPIAN_CONFIG", "/usr/bin/xapian-config")

def build():
    PYTHON3="/usr/bin/python3"
    autotools.configure("--prefix=/usr --with-python3")
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "HACKING","README")