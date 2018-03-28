#coding=utf-8
# build的时候会把python sdk和pypinyin,pymysql都拷贝过来
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
import LogtextArchived

def run():
    interval = 1
    command = r'ifconfig'
    LogtextArchived.run(interval, command)

if __name__=="__main__":
  run()
