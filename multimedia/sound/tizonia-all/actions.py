#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    # todo:
    # fix chmod +x sqlite3
    autotools.autoreconf("-fis")
    autotools.configure("--silent \
                        --enable-silent-rules \
                        CFLAGS='-O2 -s -DNDEBUG -Wno-stringop-overflow' \
                        CXXFLAGS='-O2 -s -DNDEBUG -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -Wno-deprecated-declarations'")
    # fix unused direct dependency analysis
    for dirs in ["3rdparty/dbus-cplusplus/", "cast/libtizcastclient/", "clients/chromecast/", "clients/chromecast/libtizchromecast/", "clients/gmusic/", "clients/gmusic/libtizgmusic/", "clients/plex/", "clients/plex/libtizplex/", "clients/soundcloud/", "clients/soundcloud/libtizsoundcloud/", "clients/spotify/", "clients/spotify/libtizspotify/", "clients/youtube/", "clients/youtube/libtizyoutube/", "libtizcore/", "libtizonia/", "libtizplatform/", "player/", "plugins/", "plugins/aac_decoder/", "plugins/chromecast_renderer/", "plugins/file_reader/", "plugins/file_writer/", "plugins/flac_decoder/", "plugins/http_renderer/", "plugins/http_source/", "plugins/mp3_decoder/", "plugins/mp3_encoder/", "plugins/mp3_metadata/", "plugins/mpeg_audio_decoder/", "plugins/ogg_demuxer/", "plugins/ogg_muxer/", "plugins/opus_decoder/", "plugins/opusfile_decoder/", "plugins/pcm_decoder/", "plugins/pcm_renderer_alsa/", "plugins/pcm_renderer_pa/", "plugins/spotify_source/", "plugins/vorbis_decoder/", "plugins/vp8_decoder/", "plugins/webm_demuxer/", "plugins/yuv_renderer/", "rm/libtizrmproxy/", "rm/tizrmd/",]:
        pisitools.dosed("%s/libtool" % dirs, " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README*")