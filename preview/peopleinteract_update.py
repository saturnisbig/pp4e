#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import shelve
from person import Person

fieldnames = ['name', 'age', 'pay', 'job']

db = shelve.open('people-class')
key = raw_input('key? => ')

while True:
    if not key:
        break
    try:
        record = db[key]
    except:
        new_record = Person('?', '?')
        #print 'No such key "%s"' % key
        for field in fieldnames:
            print '[%s]=%s' % (field, getattr(new_record, field))
            v = raw_input('\tnew?=> ')
            if v:
                setattr(new_record, field, eval(v))
                db[key] = new_record
    else:
        for field in fieldnames:
            print '[%s]=%s' % (field, getattr(record, field))
            v = raw_input('\tnew?=> ')
            if v:
                setattr(record, field, eval(v))
                db[key] = record
    key = raw_input('key? => ')

db.close()
