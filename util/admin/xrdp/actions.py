#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --sbindir=/usr/bin \
                         --enable-jpeg \
                         --enable-tjpeg \
                         --enable-fuse \
                         --enable-opus \
                         --enable-rfxcodec \
                         --enable-mp3lame \
                         --enable-pixman=yes \
                         --enable-painter \
                         --enable-vsock")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS*", "COPYING", "README*")
