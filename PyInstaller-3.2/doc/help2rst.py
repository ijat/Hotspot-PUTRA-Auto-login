#!/usr/bin/env python
'''
This script reformats the output of `myprog --help` to decent rst.

Currently handles optparse and argparse output. Removes everything
before "Options" resp. "optional arguments" and after "Obsolete
options".
'''

from __future__ import print_function

import argparse
import subprocess
import textwrap
import re
import sys

__copyright__ = "Copyright (c) 2015-2016 PyInstaller Development Team, Copyright (c) 2015 Hartmut Goebel"
__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"


def gen_headings(text, headings_character):
    text = (t.rstrip() for t in text.splitlines())
    new_text = []
    dedent = 0
    for line in text:
        heading = line and not line.startswith((' ', '-'))
        if heading:
            # remove trailing colon
            line = line.rstrip(':')
            dedent = 0
        elif dedent:
            # dedent for this section already known
            assert line[:dedent].strip() == '', line
            line = line[dedent:]
        else:
            # dedent for this section not yet known
            # check for next optional arguments (starting with a dash)
            leading_whitespace = re.findall(r'^[ \t]*(?=-)', line)
            if leading_whitespace:
                dedent = len(leading_whitespace[0])
                line = line[dedent:]
        new_text.append(line)
        if heading:
            # append underline
            new_text.append(headings_character * len(line))
            new_text.append('')  # empty line for readability only
    return '\n'.join(new_text)


def process(program, generate_headings, headings_character):
    help = subprocess.check_output([sys.executable, program, '--help'],
                                   universal_newlines=True)
    if '\nOptions:' in help:
        # optparse style
        help = help.split('\nOptions:', 1)[1]
    elif '\noptional arguments:' in help:
        # argparse style
        help = help.split('\noptional arguments:', 1)[1]
    else:
        raise SystemError('unexpected format of output for --help')
    # Remove any obsolete options
    help = re.split(r'\n\s*Obsolete options', help)[0]

    help = help.strip('\n')
    # escape stars prior to other processing
    help = help.replace('*', r'\*')
    if generate_headings:
        help = textwrap.dedent(help)
        help = gen_headings(help, headings_character)
    return help


def to_file(program, generate_headings, headings_character, outfile):
    help = process(program, generate_headings, headings_character)
    with open(outfile, 'w') as ofh:
        print(help, file=ofh)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate-headings',
                        action='store_true', default=True,
                        help=("Generate section headings from arumgent groups"
                              " (this is the default)"))
    parser.add_argument('--no-generate-headings',action='store_false',
                        dest='generate_headings')
    g = parser.add_argument_group('tst')
    g.add_argument('--headings-character', default="-",
                        help=("Character to use for underlining section headers"
                              " (default: -)"))
    parser.add_argument('program')
    args = parser.parse_args()
    print(process(**vars(args)))

if __name__ == '__main__':
    main()
