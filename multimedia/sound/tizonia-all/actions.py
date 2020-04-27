#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# fix "virtual memory exhausted: Cannot allocate memory"
shelltools.export("JOBS", get.makeJOBS().replace("-j5", "-j1"))

def setup():
    # suppress compiler warnings
    pisitools.cflags.add("-O2 -s -DNDEBUG -fno-strict-aliasing -Wno-stringop-overflow -Wno-unused-but-set-variable -Wno-unused-variable -Wno-stringop-truncation -Wno-incompatible-pointer-types -Wno-unused-result")
    pisitools.cxxflags.add("-O2 -s -DNDEBUG -fno-strict-aliasing -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -Wno-deprecated-declarations -Wno-unused-result -Wno-unused-variable -Wno-unused-but-set-variable -Wno-non-virtual-dtor")
    mesontools.configure("-Dbashcompletiondir=/usr/share/bash-completion/completions -Dzshcompletiondir=/usr/share/zsh/site-functions")

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.dodoc("COPYING*", "README*")