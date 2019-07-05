# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
    --enable-bittorrent \
    --enable-libaria2 \
    --enable-metalink \
    --enable-epoll \
    --enable-nls \
    --disable-rpath \
    --with-libz \
    --with-gnutls \
    --with-sqlite3 \
    --with-libxml2 \
    --with-libssh2 \
    --with-libcares \
    --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt")

    ## ???!!1
    #--with-bashcompletiondir=/usr/share/bash-completion/bash_completion

def build():
    autotools.make("-C po update-gmo")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", \
    "COPYING", \
    "INSTALL", \
    "LICENSE.OpenSSL", \
    "NEWS", \
    "README*")
