#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules, shelltools, pisitools

def setup():
	shelltools.system('sh scripts/create-mo-files.sh')
	shelltools.system('sh scripts/translate-desktop-files.sh')

def build():
	pass

def install():
	pythonmodules.install(pyVer = '3')
	pisitools.removeDir('/usr/share/*-python')

