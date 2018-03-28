# -*- encoding: utf-8 -*-
import sys 
import os
import time
import re
from html.parser import HTMLParser

ISOTIMEFORMAT='%Y-%m-%d %X'
Separator = '^'

def filter_emoji(desstr,restr=u'?'):
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    #resovle_value = highpoints.sub(u'??', src_string2)  
    resovle_value = co.sub(restr, desstr)
    return resovle_value

#def str_2_emoji(emoji_str):
#    if not emoji_str:
#        return emoji_str
#    h = HTMLParser()
#    emoji_str = h.unescape(h.unescape(emoji_str))
#    co = re.compile(ur"u[\'\"]\\[Uu]([\w\"]{9}|[\w\"]{5})")
#    pos_list=[]
#    result=emoji_str
#    for m in co.finditer(emoji_str):
#        pos_list.append((m.start(),m.end()))
#    for pos in range(len(pos_list)):
#        if pos==0:
#            result=emoji_str[0:pos_list[0][0]]
#        else:
#            result=result+emoji_str[pos_list[pos-1][1]:pos_list[pos][0]]
#        result = result +eval(emoji_str[pos_list[pos][0]:pos_list[pos][1]])
#        if pos==len(pos_list)-1:
#            result=result+emoji_str[pos_list[pos][1]:len(emoji_str)]
#    return result


def GetCurTime():
    curtime =time.strftime(ISOTIMEFORMAT, time.localtime()) 
    return curtime

def Encode(str):
     type = sys.getfilesystemencoding()
     return str.decode('utf-8').encode(type)

def Decode(str):
    type = sys.getfilesystemencoding()
    strUtf8 = str.decode('utf-8')
    return strUtf8
    #return str.encode('utf-8').decode(type)


def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
          
            #if s == "xxx":
                #continue
            newDir = os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList