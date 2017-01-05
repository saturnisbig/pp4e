# -*- coding: utf-8 -*-

import pickle

from initdata import db

bob = db['bob']
bob['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
