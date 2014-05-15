import os.path
import os
from datetime import datetime
from shutil import copy2

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
    if not os.path.exists(dst):
        print "creating directories"
        os.makedirs(dst)
    copy2(src,dst)

if __name__=="__main__":
    src = 'test.png'
    print newname(src)
    copyfile(src,newname(src))
