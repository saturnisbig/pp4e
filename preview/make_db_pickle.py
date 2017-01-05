#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

from initdata import db

dbfile = open('peopel-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
