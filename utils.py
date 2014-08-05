import os.path
import os
import sys
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
        if os.path.isfile(dst) and os.access(dst, os.R_OK):
            if filehasher(src) == filehasher(dst):
                print "Hash already present...\nignorIng."
                return
            else:
                print "Date collision, renaming...\n"
                
                srcname,srcext = os.path.splitext(src)
                dstname,dstext = os.path.splitext(dst)

                newsrc = srcname + "_1" + srcext
                newdst = dstname + "_2" + dstext
                
                copyhelper(src,newsrc)
                copyhelper(dst,newdst)

                return

        else:
            copyhelper(src,dst)
        

def copyhelper(src,dst):
    with open(src,"rb") as srcobj:
        with open(dst,"wb") as dstobj:
            copyfileobj(srcobj, dstobj)
    

def fotowalker(direct):
    pass


if __name__=="__main__":
    src = sys.argv[1]
    print newname(src)
    copyfile(src,newname(src))
