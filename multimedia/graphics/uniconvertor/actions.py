#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

def setup():
	shelltools.system("mv setup-uc2.py setup.py")

def build():
	pythonmodules.compile()

def install():
	pythonmodules.install()

