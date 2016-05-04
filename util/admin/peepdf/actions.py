#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="peepdf_%s" % get.srcVERSION()

def install():
    shelltools.cd("..")
    shelltools.copytree("peepdf_0.3/", "%s/usr/share/peepdf/" % get.installDIR())
    shelltools.cd(WorkDir)
    pisitools.remove("/usr/share/peepdf/AUTHORS")
    pisitools.remove("/usr/share/peepdf/CHANGELOG")
    pisitools.remove("/usr/share/peepdf/README")
    
    shelltools.makedirs(get.installDIR() + "/usr/bin")
    sqlninjaBashFile = open(get.installDIR() + "/usr/bin/peepdf", "w")
    sqlninjaBashFile.write("#!/bin/bash\nexec python /usr/share/peepdf/peepdf.py \"$@\"\n")
    sqlninjaBashFile.close()
    
    shelltools.system("chmod +x '%s/usr/bin/peepdf'" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "CHANGELOG", "README")

