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

WorkDir="capstone-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python")
    shelltools.copytree("./%s/bindings/python/" % WorkDir,  "build_python")
    shelltools.cd(WorkDir)
    
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s/bindings/python/" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)

def build():
    autotools.make()
    
    shelltools.cd("../build_python/python")
    pythonmodules.compile(pyVer="2.7")

    shelltools.cd("..")
    shelltools.cd("../build_python3/python")
    pythonmodules.compile(pyVer="3")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "LICENSE.TXT", "README", "RELEASE_NOTES", "TODO")
    pisitools.insinto("/usr/share/doc/capstone/", "docs/")
    
    shelltools.cd("../build_python/python")
    pythonmodules.install(pyVer="2.7")
    
    shelltools.cd("..")
    shelltools.cd("../build_python3/python")
    pythonmodules.install(pyVer="3")

