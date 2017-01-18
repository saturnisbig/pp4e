#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import shelve

fieldnames = ['name', 'age', 'pay', 'job']
maxfield = max(len(field) for field in fieldnames)
db = shelve.open('people-class')

while True:
    key = raw_input('\nkey? => ')
    if not key: break
    try:
        people = db[key]
    except:
        print 'No such key "%s"!' % key
    else:
        for field in fieldnames:
            print field.ljust(maxfield), '=>', getattr(people, field)
