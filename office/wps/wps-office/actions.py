#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/wps-office/work/ and:
# WorkDir="wps-office-"+ get.srcVERSION() +"/sub_project_dir/"

def install():
      pisitools.insinto("/usr/bin","et")
      pisitools.insinto("/usr/bin","wpp")
      pisitools.insinto("/usr/bin","wps")
      pisitools.insinto("/usr/share","resource/*")
      pisitools.insinto("etc/fonts/conf.avail","fontconfig/*")
      pisitools.insinto("/usr/share/fonts/wps-office","fonts/*")
      pisitools.insinto("/usr/lib/kingsoft/wps-office/office6","office6/*")
# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("wps-office")

# You can use these as variables, they will replace GUI values before build.
# Package Name : wps-office
# Version : 10.1.0.5672
# Summary : Kingsoft Office Suite

# For more information, you can look at the Actions API
# from the Help menu and toolbar.
