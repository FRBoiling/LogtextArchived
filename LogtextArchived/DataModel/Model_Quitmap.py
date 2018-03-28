#coding=utf-8
import sensorsanalytics
import datetime,time
import Log

class Model_Quitmap(object):
    """description of class"""
    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         uid INT,
                         ServerID INT,
                         StageID INT,
                         ExitDate VARCHAR(256),
                         StateType VARCHAR(256),
                         CurrentExp INT,
                         CurrentDiamond INT,
                         CurrentCoin INT,
                         KEY idx_uid (uid)
                         )'''
        return sql
        
    def getInsertSql(self,tablename):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s,%s,%s,%s,%s)'''
        return sql

    def sendSSNormal(self,consumer,items):
        try:
             uid = str(items[0])
             ServerID = str(items[1])
             StageID = str(items[2])
             ExitDate=str(items[3])
             StateType = str(items[4])
             CurrentExp = str(items[5])
             CurrentDiamond=str(items[6])
             CurrentCoin=str(items[7])

             sa = sensorsanalytics.SensorsAnalytics(consumer)
             distinct_id =ServerID+'_'+ uid
             expire_time = ExitDate
             d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
             time_sec_float = time.mktime(d.timetuple())
             properties = {
             'uid' :uid,
             'ServerID' : ServerID,
             'StageID' : StageID,
             '$time':time_sec_float,
             'StateType':StateType,
             'CurrentExp':int(CurrentExp),
             'CurrentDiamond':int(CurrentDiamond),
             'CurrentCoin':int(CurrentCoin)
             }
             sa.track(distinct_id, 'ExitMap', properties)
             sa.close()
             return 1
        except Exception as e:
             Log.error("Exitmap error code: %s"%(str(e)))
             if '10060' in str(str(e)):
                return 10060
             else:
                return -1
