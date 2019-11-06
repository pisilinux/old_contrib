# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	pisitools.dosed("src/xfpm-polkit.c", "procfs.h", "sys/procfs.h")
	pisitools.dosed("configure", "procfs.h", "sys/procfs.h")
	autotools.configure("\
	--enable-network-manager \
	--enable-polkit \
	--with-x")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", \
	"ChangeLog", \
	"COPYING", \
	"NEWS", \
	"README", \
	"TODO")
