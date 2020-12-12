#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.system("ln -s /usr/bin/python3 python")
	shelltools.export("PATH", ".")

def build():
	shelltools.system("scons -j1 target_python=python3 prefix=/usr sbindir=/sbin udevdir=/lib/udev")

def install():
	shelltools.system("DESTDIR=%s scons udev-install prefix=/usr" % get.installDIR())

	# fix shebang
	shelltools.system("find %s/usr/bin -type f -exec sed -i 's|env\ python$|env python3|g' {} \;" % get.installDIR())

	# Install UDEV files
#	pisitools.insinto("/lib/udev/rules.d", "gpsd.rules", "99-gpsd.rules")
#	pisitools.dobin("gpsd.hotplug", "/lib/udev")

	# Fix permissions
#	shelltools.chmod("%s/usr/lib/%s/site-packages/gps/gps.py" % (get.installDIR(), get.curPYTHON()))

