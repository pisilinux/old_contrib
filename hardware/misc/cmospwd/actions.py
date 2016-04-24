#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="cmospwd-%s" % get.srcVERSION() + "/src/"

def setup():
    pisitools.dosed("Makefile", "CFLAGS=-Wall -W -O2", "CFLAGS=-Wall -W -O2 -Wno-sign-compare -Wno-pointer-sign")


def build():
    autotools.make("-B")

def install():
    pisitools.insinto("/usr/bin", "cmospwd")
    pisitools.dodoc("../COPYING", "../cmospwd.txt")
