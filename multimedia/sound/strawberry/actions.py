#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, mesontools, pisitools

j = ''.join([
    ' -DBUILD_WITH_QT5=ON',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DUSE_TAGPARSER=ON',
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    pisitools.dosed("ext/libstrawberry-tagreader/tagreadertagparser.cpp", "core/timeconstants.h", "utilities/timeconstants.h")
    cmaketools.configure(j)

def build():
    mesontools.build("-C build")

def install():
    mesontools.install("-C build")

    pisitools.dodoc("Changelog")
