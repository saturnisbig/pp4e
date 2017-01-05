#!/usr/bin/env python
# -*- coding: utf-8 -*-

dbfilename = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '=>'


def storeDbase(db, dbfilename=dbfilename):
    with open(dbfilename, 'w') as fd:
        for key in db:
            fd.write(key+'\n')
            for k, v in db[key].items():
                fd.write(k+RECSEP+repr(v)+'\n')
            fd.write(ENDREC+'\n')
        fd.write(ENDDB)


def loadDbase_2(dbfilename=dbfilename):
    db = {}
    with open(dbfilename) as dbfile:
        import sys
        sys.stdin = dbfile
        key = raw_input()
        while key != ENDDB:
            rec = raw_input()
            data = {}
            while rec != ENDREC:
                k, v = rec.split(RECSEP)
                data[k] = eval(v)
                rec = raw_input()
            db[key] = data
            key = raw_input()
    return db



def loadDbase(dbfilename=dbfilename):
    db = {}
    key = ''
    tmp = {}
    with open(dbfilename, 'r') as fd:
        for line in fd:
            line = line.rstrip('\n')
            if line == ENDDB:
                return db
            elif line == ENDREC:
                db[key] = tmp
                key = ''
                tmp = {}
            elif line.find(RECSEP) != -1:
                k, v = line.split(RECSEP)
                tmp[k] = eval(v)
            else:
                key = line
    return db


def loadDbase_example(dbfilename=dbfilename):
    dbfile = open(dbfilename)
    db = {}
    import sys
    sys.stdin = dbfile
    # 这里用raw_input不用input，因为input输入时必须是具体的某一类型的数据，
    # 比如输入abc，会报错，'abc' not define
    key = raw_input()
    while key != ENDDB:
        rec = {}
        field = raw_input()
        while field != ENDREC:
            k, v = field.split(RECSEP)
            rec[k] = eval(v)
            field = raw_input()
        db[key] = rec
        key = raw_input()
    return db


if __name__ == "__main__":
    #from initdata import db
    #storeDbase(db)
    #db = loadDbase()
    #db = loadDbase_example()
    db = loadDbase_2()
    print(db)
