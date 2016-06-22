#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    qt5.configure()
    
def build():    
    qt5.make()

def install():   
    qt5.install() 
    pisitools.domove(  "/usr/lib/qt5/bin/QMLPlayer", "/usr/bin")
    pisitools.domove("/usr/lib/qt5/bin/Player", "/usr/bin")
    
    pisitools.dodoc("Changelog", "README.md","gpl-3.0.txt", "lgpl-2.1.txt")
