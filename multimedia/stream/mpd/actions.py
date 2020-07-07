#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
#	pisitools.dosed("doc/meson.build", "sphinx-build", "sphinx-build3")
	pisitools.ldflags.add("-lbsd")
	pisitools.cxxflags.add("-lbsd")
	mesontools.configure("-Ddocumentation=true -Dfifo=false \
	\
	-Dtcp=true \
	-Ddsd=true \
	-Dcue=true \
	-Dpipe=true \
	-Dhttpd=true \
	-Depoll=true \
	-Ddaemon=true \
	-Dinotify=true \
	-Deventfd=true \
	-Dsignalfd=true \
	-Drecorder=true \
	-Ddatabase=true \
	-Dneighbor=true \
	-Dwave_encoder=true \
	-Dlocal_socket=true \
	\
	-Dao=enabled \
	-Dgme=enabled \
	-Dmad=enabled \
	-Dmms=enabled \
	-Dnfs=enabled \
	-Dicu=enabled \
	-Doss=enabled \
	-Dfaad=enabled \
	-Dflac=enabled \
	-Dipv6=enabled \
	-Dupnp=enabled \
	-Dcurl=enabled \
	-Dalsa=enabled \
	-Dopus=enabled \
	-Dlame=enabled \
	-Djack=enabled \
	-Ddbus=enabled \
	-Dpcre=enabled \
	-Dyajl=enabled \
	-Dzlib=enabled \
	-Dzzip=enabled \
	-Dqobuz=enabled \
	-Dtidal=enabled \
	-Diconv=enabled \
	-Dshout=enabled \
	-Dbzip2=enabled \
	-Dshine=enabled \
	-Dpulse=enabled \
	-Dexpat=enabled \
	-Dopenal=enabled \
	-Dmpg123=enabled \
	-Dvorbis=enabled \
	-Dudisks=enabled \
	-Dwebdav=enabled \
	-Dffmpeg=enabled \
	-Dmikmod=enabled \
	-Did3tag=enabled \
	-Dsqlite=enabled \
	-Dmodplug=enabled \
	-Dwavpack=enabled \
	-Dtwolame=enabled \
	-Diso9660=enabled \
	-Dsndfile=enabled \
	-Dsmbclient=enabled \
	-Daudiofile=enabled \
	-Dvorbisenc=enabled \
	-Dfluidsynth=enabled \
	-Dsoundcloud=enabled \
	-Dchromaprint=enabled \
	-Dlibmpdclient=enabled \
	-Dlibsamplerate=enabled \
	-Dcdio_paranoia=enabled \
	-Dsolaris_output=enabled \
	\
	-Dzeroconf=auto \
	\
	-Dsoxr=disabled \
	-Dsndio=disabled \
	-Dadplug=disabled \
	-Dtremor=disabled \
	-Dmpcdec=disabled \
	-Dsidplay=disabled \
	-Dsystemd=disabled \
	-Dwildmidi=disabled")

def build():
	mesontools.build()

def install():
	mesontools.install()
	pisitools.insinto("/etc", "doc/mpdconf.example", "mpd.conf")

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README.md")

