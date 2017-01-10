#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import shelve

db = shelve.open('people-class')

bob = db['bob']

bob.give_raise(.10)
db['bob'] = bob

tom = db['tom']
tom.give_raise(.20)
db['tom'] = tom

db.close()
