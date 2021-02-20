#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "--enable-openconnect \
     --enable-session-policy-local \
     --enable-polkit \
     --enable-client \
     --enable-wifi \
     --enable-gadget \
     --enable-ethernet \
     --enable-loopback \
     --enable-nmcompat \
     --enable-bluetooth \
     --disable-pptp \
     --disable-selinux \
     --with-dbusconfdir=/etc \
     --with-dbusdatadir=/usr/share \
     --with-systemdunitdir='' \
     --with-tmpfilesdir='' \
    "

def setup():
	pisitools.ldflags.add("-lc -lpolkit-agent-1 -lpolkit-gobject-1")
	autotools.autoreconf("-vif")
	autotools.configure(i)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO")

