#!/usr/bin/env python

import os, sys
import argparse
import prebuild


__version__ = '0.1.0'


def init_path():
    """Checkout whether in path"""
    path = os.getcwd()
    if path not in sys.path:
        sys.path.append(path)


def parse_arguments():
    """Specify project source directory as input"""
    parser = argparse.ArgumentParser(description='Nghstnd project')

    parser.add_argument(
        'srcdir',
        action='store',
        metavar='directory',
        help='specify source directory')

    parser.add_argument(
        '-p', '--pre-build',
        action='store_true',
        default=False,
        dest='isprebuild',
        help='output pre-build minified files before compiling')

    return parser.parse_args()


def main():
    init_path()
    args = parse_arguments()
    run = prebuild.HTMLPrebuilder(args)


if __name__ == '__main__':
    main()
