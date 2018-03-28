#coding=utf-8
import sensorsanalytics
import datetime,time
import Log
class Model_Online(object):
    """description of class"""
    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         ServerID INT,
                         RegistCount INT,
                         OnlineCount INT,
                         CurDate VARCHAR(256),
                         KEY idx_serverId (ServerID)
                         )'''
        return sql
        
    def getInsertSql(self,tablename):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s)'''
        return sql

    def sendSSNormal(self,consumer,items):
        try:
            ServerID = str(items[0])
            RegistCount = str(items[1])
            OnlineCount = str(items[2])
            CurDate=str(items[3])
            sa = sensorsanalytics.SensorsAnalytics(consumer)
            distinct_id =ServerID+'_onlinecount';
            expire_time = CurDate

            d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
            time_sec_float = time.mktime(d.timetuple())

            properties = {
            'ServerID' : ServerID,
            'RegistCount' :int(RegistCount),
            'OnlineCount':int(OnlineCount),
            '$time':time_sec_float
            }
            sa.track(distinct_id, 'Online', properties)
            sa.close()
            return 1
        except Exception as e:
            Log.error("Online error code: %s"%(str(e)))
            if '10060' in str(str(e)):
              return 10060
            else:
              return -1


    