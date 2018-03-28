#coding=utf-8
import os
from xml.dom.minidom import Document
markFile = "Mark.txt"
errMarkFile = "errMark.txt"
errMarkFile_db = "errMark_db.txt"
errMarkFile_ss = "errMark_ss.txt"

def setMark(val):
    f=open(markFile,"w+")
    S='\n'.join(str(v) for v in val)
    f.write(S)
    f.close()

def setErrMark(tablename,name,val):
    f=open(errMarkFile,"a")
    S =name+ '<>>>'+tablename+ '<>>>'+str(val).replace("\n","")
    f.write(S+'\n')
    f.close()

def setErrMark_db(tablename,name,val):
    f=open(errMarkFile_db,"a")
    S =name+ '<>>>'+tablename+ '<>>>'+str(val).replace("\n","")
    f.write(S+'\n')
    f.close()

def setErrMark_ss(tablename,name,val):
    f=open(errMarkFile_ss,"a+")
    S =name+ '<>>>'+tablename+ '<>>>'+str(val).replace("\n","")
    f.write(S+'\n')
    f.close()

def deleteMark():
    if os.path.exists(markFile):
       os.remove(markFile)

def createMark():
    pass

def readMark():
    arr=[]
    if os.path.exists(markFile):
       file_object = open(markFile,'r+')
       name = file_object.name
       index = 0
       for line in file_object:
          arr.append(line)
    else:
       pass
    return arr



