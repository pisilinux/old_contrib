#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os
from distutils.dir_util import copy_tree

WorkDir = "."

def setup():
    # Unpack and prepare files
    for tar_file in shelltools.ls('.'):
        if tar_file.endswith("xz"):
            shelltools.system("tar Jxfv %s" % tar_file)

def build():
    for folder in ["tlpkg"]:
        shelltools.unlinkDir(folder)

def install():
    pisitools.dodir("/usr/share")

    wanteddirs = []
    for file_ in shelltools.ls('.'):
        if shelltools.isDirectory(file_) and not "texmf" in file_:
            wanteddirs.append(file_)

    for folder in wanteddirs:
        pisitools.insinto("/usr/share/texmf-dist", folder)

    if shelltools.can_access_directory("texmf-dist"):
        # Recursively copy on directory on top of another, overwrite duplicate files too
        copy_tree("texmf-dist", "%s/usr/share/texmf-dist" % get.installDIR())

    ## chmod of script files
    script_dir = get.installDIR() + "/usr/share/texmf-dist/scripts"
    if shelltools.can_access_directory(script_dir):
        for root, dirs, files in os.walk(script_dir):
            for name in files:
                shelltools.chmod(os.path.join(root, name), 0755)

    i = "/usr/share/texmf-dist/scripts"

    pisitools.dosym("%s/authorindex/authorindex" % i, "/usr/bin/authorindex")
    pisitools.dosym("%s/exceltex/exceltex" % i, "/usr/bin/exceltex")
    pisitools.dosym("%s/glossaries/makeglossaries" % i, "/usr/bin/makeglossaries")
    pisitools.dosym("%s/glossaries/makeglossaries-lite.lua" % i, "/usr/bin/makeglossaries-lite")
    pisitools.dosym("%s/l3build/l3build.lua" % i, "/usr/bin/l3build")
    pisitools.dosym("%s/makedtx/makedtx.pl" % i, "/usr/bin/makedtx")
    pisitools.dosym("%s/pax/pdfannotextractor.pl" % i, "/usr/bin/pdfannotextractor")
    pisitools.dosym("%s/perltex/perltex.pl" % i, "/usr/bin/perltex")
    pisitools.dosym("%s/pygmentex/pygmentex.py" % i, "/usr/bin/pygmentex")
    pisitools.dosym("%s/splitindex/splitindex.pl" % i, "/usr/bin/splitindex")
    pisitools.dosym("%s/svn-multi/svn-multi.pl" % i, "/usr/bin/svn-multi")
    pisitools.dosym("%s/vpe/vpe.pl" % i, "/usr/bin/vpe")
    pisitools.dosym("%s/webquiz/webquiz.py" % i, "/usr/bin/webquiz")
    pisitools.dosym("%s/wordcount/wordcount.sh" % i, "/usr/bin/wordcount")
    pisitools.dosym("%s/yplan/yplan" % i, "/usr/bin/yplan")

