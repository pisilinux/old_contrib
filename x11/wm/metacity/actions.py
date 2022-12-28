#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

j = ''.join([
    ' --enable-debug',
    ' --disable-static',
    ' --disable-canberra',
    ' --disable-schemas-compile',
    ' --disable-startup-notification '
    ])

def setup():
#	pisitools.cflags.remove("-O2")
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")

	pisitools.removeDir("/usr/share/gnome-control-center")
