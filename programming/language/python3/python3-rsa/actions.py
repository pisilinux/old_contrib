#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    pisitools.rename("/usr/bin/pyrsa-verify","pyrsa-verify3")
    pisitools.rename("/usr/bin/pyrsa-keygen","pyrsa-keygen3")
    pisitools.rename("/usr/bin/pyrsa-priv2pub","pyrsa-priv2pub3")
    pisitools.rename("/usr/bin/pyrsa-sign","pyrsa-sign3")
    pisitools.rename("/usr/bin/pyrsa-encrypt","pyrsa-encrypt3")
    pisitools.rename("/usr/bin/pyrsa-decrypt","pyrsa-decrypt3")