#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#   local _gemdir="$(ruby -e'puts Gem.default_dir')"
#   HOME="/tmp" 
#   GEM_HOME="$_gemdir"
#   GEM_PATH="$_gemdir" 
#   gem install --no-user-install --ignore-dependencies -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" "$_gemname-$pkgver.gem"
#_gemdir="$(ruby -e'puts Gem.default_dir')"

def install():
    shelltools.makedirs(get.installDIR() + "/usr/bin")
    #shelltools.export("_gemdir", "ruby -e'puts Gem.default_dir'")
    #_gemdir = "ruby -e'puts Gem.default_dir'"
    _gemdir = "/usr/lib/ruby/gems/2.2.0"
    HOME="/tmp"
    GEM_HOME="_gemdir"
    GEM_PATH="_gemdir"
    shelltools.system("gem install --no-user-install --ignore-dependencies -i \"%s/%s\" -n \"%s/usr/bin\" bundler-1.11.2.gem"\
                        %(get.installDIR(), _gemdir, get.installDIR()))
    #shelltools.system("gem install bundler-1.11.2.gem")
    #shelltools.system("bundle init")
    #shelltools.system("echo 'gem \"rspec\"' >> Gemfile")
    #shelltools.cd(get.installDIR() + "/usr/bin")
    #shelltools.system("ls -l")
    #shelltools.system("./bundle install")
    #shelltools.system("bundle exec rspec")

    #pisitools.dodoc("LICENSE*", "README*")
