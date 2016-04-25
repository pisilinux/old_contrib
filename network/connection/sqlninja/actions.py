#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's|/home/user/trunk/|/usr/share/metasploit|g' sqlninja.conf")

def install():
    pisitools.insinto("/usr/share/sqlninja/", "sqlninja")
    shelltools.chmod(get.installDIR() + "/usr/share/sqlninja/sqlninja", mode=0755)
    #pisitools.dosym("/usr/share/sqlninja/sqlninja", "/usr/bin/sqlninja")
    pisitools.insinto("/usr/share/sqlninja/", "sqlninja.conf")
    shelltools.copytree("apps/", "%s/usr/share/sqlninja/" % get.installDIR())
    shelltools.copytree("lib/", "%s/usr/share/sqlninja/" % get.installDIR())
    shelltools.copytree("scripts/", "%s/usr/share/sqlninja/" % get.installDIR())
    shelltools.copytree("sources/", "%s/usr/share/sqlninja/" % get.installDIR())
    pisitools.dodoc("ChangeLog", "LICENSE", "README", "sqlninja-howto.html")

    shelltools.makedirs(get.installDIR() + "/usr/bin")
    sqlninjaBashFile = open(get.installDIR() + "/usr/bin/sqlninja", "w")
    sqlninjaBashFile.write("#!/bin/bash\ncd /usr/share/sqlninja\nexec ./sqlninja \"$@\"\n")
    sqlninjaBashFile.close()

    shelltools.system("chmod +x '%s/usr/bin/sqlninja'" % get.installDIR())
