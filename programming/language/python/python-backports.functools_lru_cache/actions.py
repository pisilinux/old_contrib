#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

def build():
    shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","1.6.1")
    pythonmodules.compile()

def install():
    shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","1.6.1")
    pythonmodules.install()