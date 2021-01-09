#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import autotools
WorkDir="/"
def setup():
    shelltools.system("rm -rf MEGAsync-4.3.3.0_Linux/src/MEGASync/mega/*")
    shelltools.system("mv sdk-3.6.9/* MEGAsync-4.3.3.0_Linux/src/MEGASync/mega")
    shelltools.cd("MEGAsync-4.3.3.0_Linux/src/MEGASync/mega")
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
        --disable-examples \
        --disable-java \
        --disable-php \
        --disable-python \
        --enable-chat \
        --enable-gcc-hardening \
        --with-cares \
        --with-curl \
        --with-sqlite \
        --with-zlib \
        --without-freeimage \
        --without-termcap \
    --without-ffmpeg")
    

def build():
    shelltools.cd("MEGAsync-4.3.3.0_Linux/src")
    shelltools.system("qmake CONFIG+='release' MEGA.pro")
    shelltools.system("lrelease MEGASync/MEGASync.pro")
    shelltools.system("make")
   

def install():
    shelltools.cd("MEGAsync-4.3.3.0_Linux/")
    pisitools.insinto("/usr/share/licenses/megasync/","LICENCE.md")
    pisitools.insinto("/usr/share/licenses/megasync/","installer/terms.txt")
    pisitools.insinto("/usr/bin","src/MEGASync/megasync")
    #pisitools.insinto("/usr/share/applications/","src/MEGASync/platform/linux/data/megasync.desktop")
    #pisitools.insinto("/usr/share/apps/","src/MEGASync/platform/linux/data/icons/hicolor/*")
