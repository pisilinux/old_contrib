#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

Workdir="."
#def setup():
    #autotools.configure("--disable-static")

#def build():
    #autotools.make()
def install():
    pisitools.dodir("/opt/pycharm-community")
    pisitools.dodir("/usr/share/applications")
    pisitools.dodir("/usr/share/pixmaps")
    pisitools.insinto("/opt/pycharm-community/", "*")
    pisitools.dosym("/opt/pycharm-community/bin/pycharm.sh", "/usr/bin/pycharm")
    pisitools.domove("/opt/pycharm-community/bin/pycharm.png","/usr/share/pixmaps")
    pisitools.remove("/opt/pycharm-community/build.txt")
