﻿#coding=utf-8
import sensorsanalytics
import datetime,time
import Log

class Model_Task(object):
    """description of class"""
    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         uid INT,
                         ServerID INT,
                         TaskID INT,
                         TaskFinishedDate VARCHAR(256),
                         KEY idx_uid (uid)
                         )'''
        return sql
        
    def getInsertSql(self,tablename):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s)'''
        return sql

              
    def sendSSNormal(self,consumer,items):
        try:
           uid = str(items[0])
           ServerID = str(items[1])
           TaskID = str(items[2])
           TaskFinishedDate=str(items[3])
           sa = sensorsanalytics.SensorsAnalytics(consumer)
           distinct_id =ServerID+'_'+ uid
           expire_time = TaskFinishedDate
           d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
           time_sec_float = time.mktime(d.timetuple())
           properties = {
           'uid' :uid,
           'ServerID' : ServerID,
           'TaskID':TaskID,
           '$time':time_sec_float,
           }
           sa.track(distinct_id, 'Task', properties)
           sa.close()
           return 1
        except Exception as e:
           Log.error("Task error code: %s"%(str(e)))
           if '10060' in str(str(e)):
              return 10060
           else:
              return -1

