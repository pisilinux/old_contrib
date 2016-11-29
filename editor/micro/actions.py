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

def setup():
    shelltools.move("%s/micro-1.1.2" % get.workDIR(), "%s/src/github.com/zyedidia/micro" % get.workDIR())

def install():
    shelltools.cd("%s/src/github.com/zyedidia/micro" % get.workDIR())
    autotools.install()
    pisitools.dodoc("%s/src/github.com/zyedidia/micro/LICENSE" % get.workDIR(), "%s/src/github.com/zyedidia/micro/README.md" % get.workDIR())


