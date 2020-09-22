#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    #autotools.autoreconf("-vif")
    # suppress compiler warnings
    pisitools.cxxflags.add("-Wno-deprecated -Wno-unused-result -Wno-int-in-bool-context -Wno-sign-compare -Wno-stringop-truncation -Wno-format-overflow")
    # simple configuration for octave
    autotools.configure("--disable-doc \
                         --disable-matlab \
                         --disable-mex-kalman-steady-state")#\
                        # --disable-octave
    # matlab configuration
    #autotools.configure("--with-matlab=/usr/local/MATLAB/R2018a MATLAB_VERSION=R2018a --enable-openmp")

def build():
    autotools.make()
    #autotools.make("html")
    #autotools.make("info")
    # making pdf need too much dependency
    #autotools.make("pdf")

# takes too much time
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING", "README*")