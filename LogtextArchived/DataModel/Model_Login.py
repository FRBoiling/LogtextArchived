#coding=utf-8
import sensorsanalytics
import datetime,time
import Log
class Model_Login(object):
    """description of class"""
    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         uid INT,
                         ServerID INT,
                         LoginDate VARCHAR(256),
                         LoginChanelID VARCHAR(256),
                         IPAddress VARCHAR(256),
                         CurrentDiamond INT,
                         KEY idx_uid (uid)
                         )'''
        return sql
        
    def getInsertSql(self,tablename):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s,%s,%s)'''
        return sql

    def sendSSNormal(self,consumer,items):
        try:
               uid = str(items[0])
               ServerID = str(items[1])
               LoginDate = str(items[2])
               LoginChanelID=str(items[3])
               IPAddress=str(items[4])
               CurrentDiamond=str(items[5])

               sa = sensorsanalytics.SensorsAnalytics(consumer)
               distinct_id =ServerID+'_'+ uid
               expire_time = LoginDate
               d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
               time_sec_float = time.mktime(d.timetuple())
               properties = {
               'uid' :uid,
               'ServerID' : ServerID,
               '$time' :time_sec_float,
               'LoginChanelID':LoginChanelID,
               '$ip':IPAddress,
               'CurrentDiamond':int(CurrentDiamond)
               }
               sa.track(distinct_id, 'Login', properties)
               sa.close()
               return 1
        except Exception as e:
            Log.error("Login error code: %s"%(str(e)))
            if '10060' in str(str(e)):
               return 10060
            else:
              return -1           
        