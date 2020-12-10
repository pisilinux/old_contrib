#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

def setup():
	# fix installation stage.
	shelltools.unlink("README")
	shelltools.system("touch README.md")
	shelltools.system("ln -s ./README.md README")

def build():
	pythonmodules.compile(pyVer = '3')

def install():
	pythonmodules.install(pyVer = '3')
