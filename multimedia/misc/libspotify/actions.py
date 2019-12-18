#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("Makefile", "ldconfig", "")

def install():
    shelltools.system("make prefix=%s/usr install"% get.installDIR())
    
    # do documents and manpages manually
    shelltools.copytree("share/doc", "%s/usr/share/doc" % get.installDIR())
    shelltools.copytree("share/man3", "%s/usr/share/man/man3" % get.installDIR())