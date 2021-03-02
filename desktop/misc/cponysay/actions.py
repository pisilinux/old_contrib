#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
	pass

def build():
	cmaketools.make()

def install():
	pisitools.dobin("build/cponysay")
	pisitools.dosym("/usr/bin/cponysay", "/usr/bin/ponysay")
