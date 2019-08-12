# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

#from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("\
	--prefix=/usr \
	--enable-polkit \
	--disable-static \
	--disable-legacy-sm \
	--with-x")

	#pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
	#pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
	#pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
#	shelltools.system("sed -i '102s/\<exec\>/& dbus-launch --exit-with-session/' scripts/xinitrc")
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", \
	"COPYING", \
	"BUGS", \
	"NEWS", \
	"README", \
	"TODO")
