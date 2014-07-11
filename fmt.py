#!/usr/bin/env python
# encoding: utf-8

"""
Beautify the output of `manage.py show_urls`.

Usage:

    $ ./manage.py show_urls | fmt.py

by Laszlo Szathmary, alias Jabba Laci, 2014
jabba.laci@gmail.com
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)


import sys

from termcolor import colored


def analyze(li):
    """
    Figure out the lengths of the longest strings.

    We get a list of tuples. A tuple has 3 strings: (s1, s2, s3).
    Find the length of the longest string in the column of s1.
    Repeat the same procedure with the 2nd and 3rd columns.
    """
    sizes = [-1, -1, -1]
    for t in li:
        s1, s2, s3 = t
        if len(s1) > sizes[0]:
            sizes[0] = len(s1)
        if len(s2) > sizes[1]:
            sizes[1] = len(s2)
        if len(s3) > sizes[2]:
            sizes[2] = len(s3)
    return sizes


def pretty_print(li, sizes):
    for t in li:
        s1, s2, s3 = t
        part1 = "{0:{width}}".format(s1, width=sizes[0])
        part1 = colored(part1, "green", attrs=['bold'])
        #
        part2 = "{0:{width}}".format(s2, width=sizes[1])
        pos = part2.rfind(".")
        part2 = "{0}.{1}".format(
            colored(part2[:pos], 'yellow'),
            colored(part2[pos+1:], 'white', attrs=['bold'])
        )
        #
        part3 = "{0:{width}}".format(s3, width=sizes[2])
        part3 = colored(part3, "red")
        #
        print("{0}   {1}   {2}".format(part1, part2, part3))


def main():
    li = []
    for line in sys.stdin:
        line = line.rstrip("\n").split()
        if len(line) == 2:
            line.append("")
        li.append(tuple(line))

    sizes = analyze(li)
    pretty_print(li, sizes)

##############################################################################

if __name__ == "__main__":
    main()
