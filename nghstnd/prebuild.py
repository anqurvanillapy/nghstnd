#!/usr/bin/env python

import os
from bs4 import BeautifulSoup


class HTMLPrebuilder(object):
    """Minify HTML associated with CSS for prebuilding"""
    def __init__(self, args):
        self.srcdir = args.srcdir
        self.validate_src(self.srcdir)

    def validate_src(self, src):
        """Validate source directory and pack source files"""
        if not os.path.isdir(src):
            raise IOError('No such source directory {}'.format(src))
        valid_exts = { '.html': 0, '.htm': 1 }
        for file in os.listdir(src):
            if os.path.isfile(src + file):
                if os.path.splitext(file)[1] in valid_exts:
                    print()
