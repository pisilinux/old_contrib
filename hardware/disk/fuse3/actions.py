#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("meson .. --prefix=/ \
                                --includedir=usr/include \
                                -Dexamples=false \
                                --mandir=usr/share/man")

def build():
    mesontools.build()

def install():
    mesontools.install()
        
    pisitools.removeDir("/dev")
    pisitools.removeDir("/etc")
    
    # Make compat symlinks into /usr/bin
    pisitools.dosym("/bin/fusermount3", "/usr/bin/fusermount3")
    
    # Move pkgconfig file to /usr/lib
    pisitools.domove("/lib/pkgconfig", "/usr/lib/")
    
    pisitools.dodoc("AUTHORS", "ChangeLog*", "README*")
