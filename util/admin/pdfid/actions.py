#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="pdfid-%s" % get.srcVERSION()

def install():
    shelltools.cd("..")
    shelltools.copytree("pdfid-%s" % get.srcVERSION(), "%s/usr/share/pdfid/" % get.installDIR())
    shelltools.cd(WorkDir)
    
    shelltools.chmod(get.installDIR() + "/usr/share/pdfid/pdfid.py", mode=0755)
    pisitools.dosym("/usr/share/pdfid/pdfid.py", "/usr/bin/pdfid")
