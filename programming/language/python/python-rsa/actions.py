#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.rename("/usr/bin/pyrsa-verify","pyrsa-verify-py2")
    pisitools.rename("/usr/bin/pyrsa-keygen","pyrsa-keygen-py2")
    pisitools.rename("/usr/bin/pyrsa-priv2pub","pyrsa-priv2pub-py2")
    pisitools.rename("/usr/bin/pyrsa-sign","pyrsa-sign-py2")
    pisitools.rename("/usr/bin/pyrsa-encrypt","pyrsa-encrypt-py2")
    pisitools.rename("/usr/bin/pyrsa-decrypt","pyrsa-decrypt-py2")