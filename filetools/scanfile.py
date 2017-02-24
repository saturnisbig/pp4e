#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def scanner(name, function):
    file = open(name, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        function(line)
    file.close()
