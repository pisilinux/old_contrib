#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
	shelltools.system("sed -i '30,31s:SDL:SDL2/SDL:g' src/system_includes.h")
	shelltools.system("sed -i '45,46s:SDL:SDL2/SDL:g' third_party/imgui/imgui_impl_sdl.cpp")

def build():
	shelltools.system("./build-lin.sh")

def install():
	pisitools.insinto("/usr/bin", "build/Milton", "milton")
	for i in ["build/Carlito*"]:
		pisitools.insinto("/usr/share/fonts/truetype/Carlito/", "%s" % i)

	shelltools.system("icotool -x milton_icon.ico")
	for t in ["256x256", "128x128", "64x64", "48x48", "32x32", "16x16"]:
		pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % t, "milton_icon_*_%sx32.png" % t, "milton.png")

	pisitools.dodoc("CONTRIBUTING.md", "CREDITS.md", "README.md")

