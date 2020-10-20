#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="pysqlite-%s" % get.srcVERSION()
#code = "%s/%s/code" % (get.docDIR(), get.srcNAME())

def setup():
    pisitools.dosed("setup.cfg", "libraries=sqlite3", "define=\ninclude_dirs=/usr/include\nlibrary_dirs=/usr/lib\nlibraries=sqlite3")
    shelltools.chmod("doc/includes/sqlite3/*", 0644)

def build():
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -Wl,-O1 -Wl,-z,relro -Wl,--hash-style=gnu -Wl,--as-needed -Wl,--sort-common")
    shelltools.export("CFLAGS", "-Wno-int-conversion -Wno-strict-aliasing %s" % get.CFLAGS())
    pisitools.dosed("setup.py", "pysqlite2-doc", "share/doc/python-pysqlite")
    pythonmodules.compile("build_docs")

def check():
    pythonmodules.compile("check")

def install():
    pythonmodules.install()

    #pisitools.dohtml("build/doc/")
    #pisitools.insinto(code, "doc/includes/sqlite3/*")
    #pisitools.remove("%s/%s/install-source.txt" % (get.docDIR(), get.srcNAME()))

