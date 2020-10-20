#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
    autotools.rawConfigure ("--prefix=/usr\
                             --with-systemdsystemunitdir=no \
                             --sysconfdir=/etc")

def build():
    autotools.make ()

def install():
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/share/pkgconfig/", "/usr/lib/pkgconfig/")
    pisitools.removeDir("/usr/lib/dracut/modules.d/00dash")
