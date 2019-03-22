#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's|${CC-cc} -E|${CC-cc} -O2 -E|g' configure")
    autotools.configure("--program-transform-name=s/l//")

def build():
    autotools.make("-j1")

def install():
    autotools.install("-j1")
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
