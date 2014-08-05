#!/usr/bin/env python
"""
deduper.py walks the given directory looking for files
with the same md5 hash, then prints out all duplicates.
If -d is given as a flag, the copy with the lowest
lexicographical name is kept
Usage: deduper.py (-d) dir
"""
from utils import filehasher, copyfile
import os
import sys

def deduper(cdir):
    dic = {}
    for cwd,dirs,files in os.walk(cdir):
        print 'Checking dir ' + cwd
        for f in files:
            fpath = os.path.join(cwd,f)
            cksum = filehasher(fpath)
            try:
                dic[cksum].append(fpath)
            except:
                dic[cksum] = [fpath]
    
    for key in dic.keys():
        if len(dic[key])>1:
            print dic[key]

if __name__=='__main__':
    print __doc__
    try:
        cdir = sys.argv[1]
    except:
        print "incorrect usage, see doc"

    deduper(cdir)
