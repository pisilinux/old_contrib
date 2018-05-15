#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def build():
    autotools.make("-C eepromer eeprom")
    autotools.make("-I../include py-smbus")
    
    
def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())

    pisitools.dodoc("CHANGES", "COPYING*", "README")
