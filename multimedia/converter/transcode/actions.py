#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

pisitools.flags.add("-DDCT_YUV_PRECISION=1")

def setup():
	autotools.autoreconf("-vfi")

	autotools.configure("\
	\
	--enable-deprecated \
	--enable-lzo \
	--enable-a52 \
	--enable-mmx \
	--enable-nuv \
	--enable-sdl \
	--enable-ogg \
	--enable-v4l \
	--enable-sse \
	--enable-sse2 \
	--enable-alsa \
	--enable-lame \
	--enable-x264 \
	--enable-xvid \
	--enable-faac \
	--enable-3dnow \
	--enable-libdv \
	--enable-vorbis \
	--enable-theora \
	--enable-libxml2 \
	--enable-libv4l2 \
	--enable-libjpeg \
	--enable-libmpeg2 \
	--enable-freetype2 \
	--enable-mjpegtools \
	--enable-libdvdread \
	--enable-imagemagick \
	--enable-libpostproc \
	--enable-libquicktime \
	--enable-libv4lconvert \
	--enable-libmpeg2convert \
	\
	--with-mod-path=/usr/lib/transcode \
	--with-x \
	--with-lzo-includes=/usr/include/lzo")

def build():
	autotools.make("all")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

