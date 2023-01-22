#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, get

i = ''.join([
    ' --with-gtktheme',
    ' --with-lx',
    ' --with-pmenu',
    ' --prefix=/usr',
    ' --libdir=/usr/lib',
    ' --libexecdir=/usr/lib '
    ])

def setup():
	autotools.rawConfigure(i)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
