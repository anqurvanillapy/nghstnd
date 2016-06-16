#!/usr/bin/env python

import os
from bs4 import BeautifulSoup, Comment


class HTMLPrebuilder(object):
    """\
    - Minify HTML associated with CSS for pre-building.
    - Supported extension names are:
        + `.html`, `.css`, `.js`
    - `.htm` is for old Windows environments, please do not name that.
    """
    def __init__(self, args):
        self.env = args.srcdir
        self.validate_env(self.env)
        self.src = {
            '.html': [],
            '.css': [],
            '.js': []
        }
        self.load_src(self.env)
        self.parse_src()
        self.isprebuild = args.isprebuild

    def validate_env(self, env):
        """Validate source directory"""
        if not os.path.isdir(env):
            raise IOError("No such source directory '{}'".format(env))

    def load_src(self, dirname):
        """Load source files"""
        for root, dirn, fn in os.walk(dirname):
            for f in fn:
                fp = os.path.join(root, f)
                try:
                    self.src[os.path.splitext(f)[1]].append(fp)
                except:
                    pass

    def parse_src(self):
        """Parse the DOM tree and attach the style rules"""
        for file in self.src['.html']:
            with open(file, 'r') as filehandle:
                dom = BeautifulSoup(filehandle.read(), 'lxml')
                cmt = dom.findAll(text=lambda t:isinstance(t, Comment))
                [c.extract() for c in cmt]  # extract comments
                print(dom)
