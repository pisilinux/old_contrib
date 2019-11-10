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
    #shelltools.ls("..")
    pisitools.dosed("Makefile", "Wall", "Wno-discarded-qualifiers")
    shelltools.cd("..")
    shelltools.makedirs("build_python")
    shelltools.copytree("./%s" % WorkDir,  "build_python")
    shelltools.cd(WorkDir)
    
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)

def build():
    autotools.make()
    
    shelltools.cd("../build_python/capstone-%s/bindings/python" % get.srcVERSION())
    pythonmodules.compile(pyVer="2.7")

    shelltools.cd("../../..")
    shelltools.cd("../build_python3/capstone-%s/bindings/python" % get.srcVERSION())
    pythonmodules.compile(pyVer="3")
    shelltools.cd("../../../../%s" % WorkDir)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "LICENSE.TXT", "README.md", "RELEASE_NOTES")
    for dirs in ["docs", "tests"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)

    shelltools.cd("../build_python/capstone-%s/bindings/python" % get.srcVERSION())
    pythonmodules.install(pyVer="2.7")
    
    shelltools.cd("../../..")
    shelltools.cd("../build_python3/capstone-%s/bindings/python" % get.srcVERSION())
    pythonmodules.install(pyVer="3")
    
    #shelltools.cd("../../../../%s" % WorkDir)
    #pisitools.dobin("cstool")

