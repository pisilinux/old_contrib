#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    shelltools.makedirs(get.installDIR() + "/usr/bin")
    
    for i in ["msfbinscan", "msfconsole", "msfd", "msfelfscan", "msfmachscan", "msfpescan", "msfrop", "msfrpc", "msfrpcd", "msfupdate", "msfvenom"]:
        msfBashFile = open(get.installDIR() + "/usr/bin/%s" % i, "w")
        msfBashFile.write("#!/bin/sh\nexec ruby /usr/share/metasploit/%s \"$@\"\n" % i)
        msfBashFile.close()
        shelltools.system("chmod +x '%s/usr/bin/%s'" % (get.installDIR(), i))
    
    shelltools.copytree(get.workDIR() + "/metasploit-framework-%s/" % get.srcVERSION(), "%s/usr/share/metasploit/" % get.installDIR())
    shelltools.cd("%s/usr/share/metasploit/" % get.installDIR())
    shelltools.system("bundle install --jobs=1 --no-cache --deployment")
    shelltools.system("find vendor/bundle/ruby/*/gems/robots-* -exec chmod o+r '{}' \;")
    shelltools.cd("%s/metasploit-framework-%s" % (get.workDIR(), get.srcVERSION()))

    pisitools.insinto("/%s/metasploit" % get.docDIR(), "documentation/*")
    pisitools.dodoc("COPYING", "HACKING", "LICENSE", "README*")
