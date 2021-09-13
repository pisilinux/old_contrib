#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    ' --sysconfdir=/etc',
    ' --prefix=/usr',
    ' --libexecdir=/usr/libexec/openbox',
    ' --with-x',
    ' --enable-nls',
    ' --enable-startup-notification',
    ' --disable-static',
    ' --docdir=/%s/%s ' % (get.docDIR(), get.srcNAME())
    ])

def setup():
	autotools.autoreconf("-fiv")
	autotools.configure(j)

	pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
	pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	# GNOME Panel is no longer available in the official repositories
	pisitools.remove("/usr/bin/gdm-control")
	pisitools.remove("/usr/bin/gnome-panel-control")
	pisitools.remove("/usr/bin/openbox-gnome-session")
	pisitools.remove("/usr/share/man/man1/openbox-gnome-session.1")
	pisitools.remove("/usr/share/xsessions/openbox-gnome.desktop")
	pisitools.removeDir("/usr/share/gnome-session")

	pisitools.dodoc("AUTHORS", "CHANGELOG", "COPYING", "README")

