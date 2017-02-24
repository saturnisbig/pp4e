#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from sys import argv
from scanfile import scanner


class UnknownCommand(Exception):
    pass


def process_line(line):
    if line[0] == '*':
        print "Ms.", line[1:-1]
    elif line[0] == '+':
        print "Mr.", line[1:-1]
    else:
        raise UnknownCommand(line)

if __name__ == "__main__":
    filename = 'data.txt'
    if len(argv) == 2:
        filename = argv[1]
    scanner(filename, process_line)
