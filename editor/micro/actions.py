#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("GOPATH", get.workDIR())
shelltools.export("GOBIN", "%s/usr/bin" % get.installDIR())

def install():
    shelltools.cd("%s/src/%s" % (get.workDIR(), get.srcDIR()))
    autotools.install()
    pisitools.dodoc("LICENSE", "README.md")


