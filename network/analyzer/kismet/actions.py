#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "hydra-%s-src" % get.srcVERSION()


def setup():
    autotools.configure()

def build():
    autotools.make("dep")
    autotools.make()
    autotools.make("plugins")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG", "README", "docs/DEVEL*", "docs/README*", "docs/devel-wiki-docs/*" )
