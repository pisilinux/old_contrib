#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#docname = get.srcNAME()

def setup():
    shelltools.system("sed -i '/extern int yyleng;/d' rtf-fix/rtf2rtf.l")
    autotools.rawConfigure("--prefix=/usr --mandir=/usr/share/man")
def build():
    autotools.make()

def install():
    #pisitools.dodir("/usr/bin")
    #pisitools.dodir("/usr/lib")

    #autotools.rawInstall("prefix=%s/usr/bin \
    #                      libdir=%s/usr/lib" \
    #                      % (get.installDIR(), \
    #                         get.installDIR()))
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dosym("sx", "/usr/bin/sgml2xml")

    #pisitools.insinto("/usr/share/sgml/%s" % docname, "dsssl/builtins.dsl")
    #for i in ["dsssl/dsssl.dtd", "dsssl/style-sheet.dtd", "dsssl/fot.dtd"]:
    #    pisitools.insinto("/usr/share/sgml/%s/dsssl" % docname, i)
    #pisitools.insinto("/usr/share/sgml/%s/pubtext" % docname, "pubtext/*")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "VERSION")
    #pisitools.dohtml("doc/*.htm")

    #pisitools.insinto("/usr/share/doc/%s/jadedoc" % get.srcNAME(), "jadedoc/*.htm")
    #pisitools.insinto("/usr/share/doc/%s/jadedoc/images" % get.srcNAME(), "jadedoc/images/*")


