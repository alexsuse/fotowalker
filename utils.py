import os.path
import os
from datetime import datetime
from shutil import copyfileobj
from hashlib import md5

def filehasher(src):
    """
    Calculate checksum of a binary file
    """
    hasher = md5()
    with open(src,"rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

def newname(src):
    """
    Takes a filename and returns a new filename, given by
    the date the file was created with the same extension
    ex: YY_MM_DD_HH_mm_SS.png
    """
    filename, ext = os.path.splitext(src)
    lm = datetime.fromtimestamp(os.path.getmtime(src))
    name = "_".join( map(str, [lm.year, lm.month, lm.day, 
                               lm.hour, lm.minute, lm.second]))
    name = os.path.join(str(lm.year),str(lm.month),str(lm.day),name)
    return name + ext

def copyfile(src, dst):
    """
    Copies a file from src to dst
    creating new directories if needed.
    """
    basedir = os.path.dirname(dst)
    if not os.path.exists(basedir):
        print "creating directories"
        os.makedirs(basedir)
    else:
        # check for collision
        if filehasher(src) == filehasher(dst):
            print "file is already present,\n...ignoring."
        else:
            #handle collision
            pass
    with open(src,"rb") as srcobj:
        with open(dst,"wb") as dstobj:
            copyfileobj(srcobj, dstobj)

if __name__=="__main__":
    src = 'test.png'
    print newname(src)
    copyfile(src,newname(src))
