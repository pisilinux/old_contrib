#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools

# fix "virtual memory exhausted: Cannot allocate memory"
shelltools.export("JOBS", get.makeJOBS().replace("-j5", "-j1"))

def setup():
    # As bayraklari as 8D
    pisitools.dosed("player/tools/tizonia.desktop.in", "Top 100 Most Streamed Songs", "Onuncu Yil Marsi")
    
    # suppress compiler warnings
    options_c =   ''.join([
                  '-Wno-unused-result ',
                  '-Wno-unused-variable ',
                  '-Wno-stringop-overflow ',
                  '-Wno-stringop-truncation ',
                  '-Wno-unused-but-set-variable ',
                  '-Wno-incompatible-pointer-types'])

    options_cxx = ''.join([
                  '-Wno-format ',
                  '-Wno-unused-result ',
                  '-Wno-unused-variable ',
                  '-Wno-non-virtual-dtor ',
                  '-Wno-error=format-security ',
                  '-Wno-unused-but-set-variable ',
                  '-Wno-deprecated-declarations'])

    pisitools.cflags.add("-O2 -s -DNDEBUG -fno-strict-aliasing %s" % options_c)
    pisitools.cxxflags.add("-O2 -s -DNDEBUG -fno-strict-aliasing -fstack-protector --param=ssp-buffer-size=4 %s" % options_cxx)
    mesontools.configure("-Dbashcompletiondir=/usr/share/bash-completion/completions -Dzshcompletiondir=/usr/share/zsh/site-functions")

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.dodoc("COPYING*", "README*")