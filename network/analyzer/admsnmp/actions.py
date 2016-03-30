#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

    
def build():
    shelltools.system("gcc $CFLAGS snmp.c -o admsnmp")

def install():
    pisitools.insinto("/usr/bin", "admsnmp")
    pisitools.dodoc("ADM*.README")
    pisitools.insinto("/usr/share/admsnmp","snmp.passwd")
