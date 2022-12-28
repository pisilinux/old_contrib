#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, pisitools, get

P = "%s" % get.curPYTHON()
p = ''.join([
    ' addhelper',
    ' animation',
    ' animationaddon',
    ' animationjc',
    ' animationplus',
    ' annotate',
    ' blur',
    ' ccp',
    ' clone',
    ' colorfilter',
    ' commands',
    ' compiztoolbox',
    ' composite',
    ' copytex',
    ' crashhandler',
    ' cube',
    ' cubeaddon',
    ' dbus',
    ' decor',
    ' expo',
    ' extrawm',
    ' ezoom',
    ' fade',
    ' fadedesktop',
    ' firepaint',
    ' gnomecompat',
    ' grid',
    ' imgjpeg',
    ' imgpng',
    ' imgsvg',
    ' inotify',
    ' mag',
    ' matecompat',
    ' maximumize',
    ' mousepoll',
    ' move',
    ' neg',
    ' notification',
    ' obs',
    ' opacify',
    ' opengl',
    ' place',
    ' put',
    ' regex',
    ' resize',
    ' resizeinfo',
    ' ring',
    ' rotate',
    ' scale',
    ' scaleaddon',
    ' scalefilter',
    ' screenshot',
    ' session',
    ' shelf',
    ' shift',
    ' showdesktop',
    ' showmouse',
    ' showrepaint',
    ' simple-animations',
    ' snap',
    ' splash',
    ' staticswitcher',
    ' switcher',
    ' text',
    ' titleinfo',
    ' trailfocus',
    ' vpswitch',
    ' wall',
    ' wallpaper',
    ' water',
    ' winrules',
    ' wizard',
    ' wobbly',
    ' workarounds',
    ' workspacenames '
    ])
j = ''.join([
    ' -B_build',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -DBUILD_GLES=ON',
    ' -DBUILD_GTK=ON',
    ' -DBUILD_GNOME=OFF',
    ' -DBUILD_METACITY=OFF',
    ' -DCYTHON_BIN=/usr/bin/cython3',
    ' -DPYTHON_EXECUTABLE=/usr/bin/python3',
    ' -DPYTHON_LIBRARY=/usr/lib/libpython%sm.so' % P,
    ' -DPYTHON_INCLUDE_DIR=/usr/include/python%sm' % P,
    ' -DCOMPIZ_DEFAULT_PLUGINS=%s -L ' % p
    ])

def setup():
    pisitools.dosed("cmake/recompile_gsettings_schemas_in_dir_user_env.cmake", "execute", deleteLine = True)
    cmaketools.configure(j)

def build():
    cmaketools.make("-C _build")

def install():
    cmaketools.install("-C _build install")

    pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README")
