#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
	perlmodules.configure()

def build():
	perlmodules.make()

def check():
	pass

def install():
	perlmodules.install()

