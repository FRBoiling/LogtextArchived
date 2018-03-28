#coding=utf-8
import sensorsanalytics
import datetime,time
import Log

class Model_CreateChar(object):
    """description of class"""

    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         uid INT,
                         ServerID INT,
                         AccountID INT,
                         AccountName VARCHAR(256),
                         RoleName VARCHAR(256),
                         RoleCreatedDate VARCHAR(256),
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
           AccountID = str(items[2])
           AccountName=str(items[3])
           RoleName = str(items[4])
           RoleCreatedDate=str(items[5])

           sa = sensorsanalytics.SensorsAnalytics(consumer)
           distinct_id =ServerID+'_'+ uid
           expire_time = RoleCreatedDate.replace("\n","").replace("\r","")
           d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
           time_sec_float = time.mktime(d.timetuple())
           properties = {
           'uid' :uid,
           'ServerID' : ServerID,
           'AccountID':AccountID,
           'AccountName':AccountName,
           'RoleName':RoleName,
           '$time':time_sec_float
           }
           sa.track(distinct_id, 'CreateChar', properties)
           sa.close()
           return 1
        except Exception as e:
            Log.error("CreateChar error code: %s"%(str(e)))
            if '10060' in str(str(e)):
               return 10060
            else:
               return -1

        