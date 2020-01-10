#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.dodir("/opt/master-pdf-editor-4")
    # install icon
    pisitools.insinto("/usr/share/pixmaps/", "masterpdfeditor4.png")
    # install language files
    pisitools.insinto("/opt/master-pdf-editor-4/lang","lang/*.qm")
    pisitools.insinto("/opt/master-pdf-editor-4/lang","lang/*.ts")
    pisitools.insinto("/opt/master-pdf-editor-4/lang/qt","lang/qt/*.qm")
    pisitools.insinto("/opt/master-pdf-editor-4/lang/qt","lang/qt/*.ts")
    # install font files
    pisitools.insinto("/opt/master-pdf-editor-4/fonts/standard","fonts/standard/*.ttf")
    # install stamp files
    pisitools.insinto("/opt/master-pdf-editor-4/stamps/Dynamic","stamps/Dynamic/*.pdf")
    pisitools.insinto("/opt/master-pdf-editor-4/stamps/Standard","stamps/Standard/*.pdf")
    #install template files
    pisitools.insinto("/opt/master-pdf-editor-4/templates/stamps","templates/stamps/*.pdf")
    #install binary
    pisitools.insinto("/opt/master-pdf-editor-4","masterpdfeditor4")
    pisitools.dosym("/opt/master-pdf-editor-4/masterpdfeditor4", "/usr/bin/masterpdfeditor4")
    # install license file
    pisitools.dodoc("license.txt")
