#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/wps-office-tr/work/ and:
WorkDir="."



def install():
    pisitools.insinto("/usr/lib/kingsoft/wps-office/office6/mui/tr_TR","tr_TR/*")

