#!/usr/bin/env python
"""
deduper.py walks the given directory looking for files
with the same md5 hash, then prints out all duplicates.
If -d is given as a flag, the copy with the lowest
lexicographical name is kept
Usage: deduper.py dir [-d -DEBUG]
"""
from utils import filehasher, copyfile, exif_time

import collections
import os
import sys

DEBUG = False
DELETE = False

def deduper(cdir, delete=False, debug=False):
    dic = collections.defaultdict(list)
    for cwd,dirs,files in os.walk(cdir):
        print 'Checking dir ' + cwd
        for f in files:
            fpath = os.path.join(cwd,f)
            time = exif_time(fpath)
            if not time:
                print "File: %s did not return a valid timestamp" % fpath
                continue
	    dic[time].append(fpath)
	    if debug:
		print "File %s obtained timestamp %d" %(fpath, time)
	
	uniques = []
	duplicates = []
    
    for key in dic.keys():
        if len(dic[key]) == 1:
	    continue
	file_hash = collections.defaultdict(list)
	for file in dic[key]:
	    cksum = filehasher(file)
	    file_hash[cksum].append(file)
	    for hash_values in file_hash.values():
		uniques.append(hash_values[0])
		if len(hash_values) == 1:
		    continue
		duplicates.extend(hash_values[1:])
		if debug:
		    print "Files below are duplicates:"
		    for duplicate in hash_values:
			print duplicate
    return uniques, duplicates

if __name__=='__main__':
    print __doc__
    try:
        cdir = sys.argv[1]
	DELETE = '-d' in sys.argv[2:]
	DEBUG = '-DEBUG' in sys.argv[2:]
    except:
        print "incorrect usage, see doc"

    deduper(cdir, delete=DELETE, debug=DEBUG)
