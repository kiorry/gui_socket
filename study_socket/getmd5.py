import hashlib   
import os

filename = "ifelse.exe"

def GetFileMD5(FilePah):
    fr = open(filename,"rb")
    Fmd = hashlib.md5()
    Fmd.update(fr.read())
    fr.close()
    return Fmd.hexdigest()

print(GetFileMD5(filename))




