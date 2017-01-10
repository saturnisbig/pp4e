#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import shelve

db = shelve.open('people-class')

bob = db['bob']
sue = db['sue']
tom = db['tom']

print bob.name, bob.pay, bob.last_name()
print tom.job, tom.pay

print bob, sue, tom
