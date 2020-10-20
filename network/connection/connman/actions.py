#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

z = "--disable-selinux \
     --enable-pptp \
     --enable-openconnect \
     --enable-polkit \
     --enable-client \
     --enable-nmcompat \
     --with-systemdunitdir='' \
     --with-tmpfilesdir='' \
    "

def setup():
	autotools.configure(z)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO")

