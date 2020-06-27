#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DBUILD_QCH=ON \
    					  -DBUILD_TESTING=OFF")

def build():
    cmaketools.make()

def install():
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    cmaketools.install()
   