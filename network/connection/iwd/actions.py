#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-systemd-service \
                         --enable-sim-hardcoded  \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --enable-client \
                         --enable-monitor \
                         --enable-ofono \
                         --enable-hwsim \
                         --enable-wired \
                         --enable-tools          \
                         --enable-sim-hardcoded  \
                         --with-dbus-busdir=/etc/dbus-1 \
                         --libexecdir=/usr/libexec")
    

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "TODO", "ChangeLog", "COPYING", "README")
