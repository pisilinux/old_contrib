#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-pixman=yes \
                         --enable-jpeg=yes \
                         --enable-tjpeg=yes \
                         --enable-fuse=yes \
                         --enable-opus=yes \
                         --enable-rfxcodec=yes \
                         --enable-mp3lame=yes \
                         --enable-kerberos=yes \
                         --enable-painter=yes \
                         --enable-vsock=yes \
                         --enable-ipv6only=yes \
                         --enable-ipv6=yes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS*", "COPYING", "README*")
