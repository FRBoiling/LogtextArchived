#coding=utf-8
import sensorsanalytics
import datetime,time
import Log

class Model_Entermap(object):
    """description of class"""
    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         uid INT,
                         ServerID INT,
                         StageID INT,
                         EnterDate VARCHAR(256),
                         CurrentExp INT,
                         CurrentDiamond INT,
                         CurrentCoin INT,
                         KEY idx_uid (uid)
                         )'''
        return sql
        
    def getInsertSql(self,tablename):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s,%s,%s,%s)'''
        return sql

    def sendSSNormal(self,consumer,items):
       try:
           uid = str(items[0])
           ServerID = str(items[1])
           StageID = str(items[2])
           EnterDate=str(items[3])
           CurrentExp = str(items[4])
           CurrentDiamond=str(items[5])
           CurrentCoin=str(items[6])
       
           sa = sensorsanalytics.SensorsAnalytics(consumer)
           distinct_id =ServerID+'_'+ uid
           expire_time = EnterDate
           d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
           time_sec_float = time.mktime(d.timetuple())
           properties = {
           'uid' :uid,
           'ServerID' : ServerID,
           'StageID' : StageID,
           '$time':time_sec_float,
           'CurrentExp':int(CurrentExp),
           'CurrentDiamond':int(CurrentDiamond),
           'CurrentCoin':int(CurrentCoin)
           }
           sa.track(distinct_id, 'EnterMap', properties) 
           sa.close()
           return 1
       except Exception as e:
            Log.error("Entermap error code: %s"%(str(e)))
            if '10060' in str(str(e)):
               return 10060
            else:
              return -1

       