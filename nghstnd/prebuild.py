#!/usr/bin/env python

import os
from bs4 import BeautifulSoup


class HTMLPrebuilder(object):
    """Minify HTML associated with CSS for prebuilding"""
    def __init__(self, args):
        self.env = args.srcdir
        self.validate_env(self.env)
        self.html = []
        self.src = {
            '.html': self.html,
            '.htm': self.html,
            '.css': [],
            '.js': []
        }
        self.load_src(self.env)
        self.isprebuild = args.isprebuild

    def validate_env(self, env):
        """Validate source directory"""
        if not os.path.isdir(env):
            raise IOError("No such source directory '{}'".format(env))

    def load_src(self, dirname):
        """Load source files"""
        for file in os.listdir(dirname):
            filepath = os.path.join(dirname, file)
            if os.path.isfile(filepath):
                try:
                    self.src[os.path.splitext(file)[1]].append(filepath)
                except:
                    pass
            elif os.path.isdir(filepath):
                self.load_src(filepath)
