#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/wps-office-dicts/work/ and:
WorkDir="."
dictsdir="/usr/lib/kingsoft/wps-office/office6/dicts/"


def install():
    for lang in ["ca_ES","cs_CZ","de_DE","el_GR","en_GB","es_ES","fr_FR","hr_HR","it_IT","km_KH","lt_LT","nl_NL","pt_BR","pt_PT","ro_RO","ru_RU","sv_SE","tr_TR","uk_UA"]:
           pisitools.insinto( dictsdir+lang,lang+"/*")
