#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def build():
    # suppress compiler warnings
    options = ''.join([
              '-Wno-missing-braces ',
              '-Wno-maybe-uninitialized ',
              '-Wno-unused-but-set-variable'])
    pisitools.cflags.add("%s" % options)
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")