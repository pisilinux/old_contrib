#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()
    
def check():
    pythonmodules.run("-m unittest Tests.tests")

def install():
    pythonmodules.install()

    for dirs in ["PDF_Samples", "Sample_Code"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)
