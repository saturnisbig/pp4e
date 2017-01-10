#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import shelve

from person import Person

from manager import Manager


bob = Person('Bob Smith', 42, 40000, 'software')
sue = Person('Sue Jones', 45, 50000, 'hardware')
tom = Manager('Tom Doe', 52, 60000)

db = shelve.open('people-class')

db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

db.close()
