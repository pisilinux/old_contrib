#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --disable-ldap \
                         --disable-ldaps \
                         --with-ssl \
                         --with-zlib \
                         --with-libidn \
                         --with-libssh2 \
                         --with-gssapi=no \
                         --with-nghttp2 \
                         --with-libmetalink \
                         --without-librtmp \
                         --enable-ipv6 \
                         --enable-http \
                         --enable-ftp \
                         --enable-file \
                         --enable-dict \
                         --enable-manual \
                         --enable-gopher \
                         --enable-telnet \
                         --enable-largefile \
                         --enable-nonblocking \
                         --enable-threaded-resolver \
                         --enable-hidden-symbols \
                         --disable-versioned-symbols \
                         ac_cv_header_gss_h=no \
                         --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt \
                         --prefix=/usr \
                         --with-random=/dev/urandom \
                         --mandir=/usr/share/man ")


def build():
    autotools.make("-C lib")

def check():
    #shelltools.export("LD_LIBRARY_PATH", "%s/lib" % get.curDIR())
    #autotools.make("-C tests test")
    pass

def install():
    autotools.rawInstall("DESTDIR=%s -C lib" % get.installDIR())
    
    pisitools.domove("/usr/lib/libcurl.so.4.5.0", "/usr/lib", "libcurl-gnutls.so.4.5.0")
    
    for sym in ["3","4","4.0.0","4.1.0","4.2.0","4.3.0","4.4.0"]:
        pisitools.dosym("/usr/lib/libcurl-gnutls.so.4.5.0","/usr/lib/libcurl-gnutls.so.%s" % sym)
    
    pisitools.remove("/usr/lib/libcurl.so")
    pisitools.remove("/usr/lib/libcurl.so.4")
   
    pisitools.dodoc("CHANGES", "docs/FEATURES", "docs/FAQ", "docs/BUGS")
