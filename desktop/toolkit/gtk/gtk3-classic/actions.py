#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, pisitools, autotools, get

i = ''.join([
    ' --prefix=/usr',
    ' --sysconfdir=/etc',
    ' --enable-x11-backend',
    ' --enable-wayland-backend',
    ' --enable-broadway-backend '
    ])

def setup():
	shelltools.unlink('testsuite/gtk/gtkresources.c')
	shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer",""))

	autotools.autoreconf("-fiv")
	autotools.configure(i)

	pisitools.dosed("libtool", "( -shared )", r" -Wl,-O1,--as-needed\1")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	# remove empty dir
	pisitools.removeDir("/usr/share/man")
	pisitools.dodoc("AUTHORS", "README*", "HACKING", "ChangeLog*", "NEWS*")

	pisitools.rename("/usr/bin/gtk-update-icon-cache", "gtk3-update-icon-cache")
