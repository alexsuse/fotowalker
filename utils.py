from os.path import splitext, getmtime
from datetime import datetime

def newname(src):
    """
    Takes a filename and returns a new filename, given by
    the date the file was created with the same extension
    ex: YY_MM_DD_HH_mm_SS.png
    """
    filename, ext = splitext(src)
    lm = datetime.fromtimestamp(getmtime(src))
    name = "_".join( map(str, [lm.year, lm.month, lm.day, 
                               lm.hour, lm.minute, lm.second]))
    return name + ext

if __name__=="__main__":
    src = 'test.png'
    print newname(src)
