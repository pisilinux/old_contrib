#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

w = "-Wno-unused-result -Wno-deprecated-declarations"

def setup():
	pisitools.cxxflags.add(w)
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure("-L", sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make("translations")

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
	shelltools.cd("..")

	pisitools.dodoc("AUTHORS", "CHANGELOG.md", "LICENSE", "README.md")

