#coding=utf-8
import sensorsanalytics
import datetime,time
import Log

class Model_Recharge(object):
    """description of class"""
    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         uid INT,
                         ServerID INT,
                         RechargeOrderID VARCHAR(256),
                         Money INT,
                         RechargeType INT,
                         ArrivalDate VARCHAR(256),
                         OrderCreatedDate VARCHAR(256),
                         Diamond INT,
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
            RechargeOrderID = str(items[2])
            Money=str(items[3])
            RechargeType = str(items[4])
            ArrivalDate=str(items[5])
            OrderCreatedDate=str(items[6])
            Diamond=str(items[7])

            sa = sensorsanalytics.SensorsAnalytics(consumer)
            distinct_id =ServerID+'_'+ uid
            expire_time = ArrivalDate
            d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
            time_sec_float = time.mktime(d.timetuple())
            properties = {
            'uid' :uid,
            'ServerID' : ServerID,
            'RechargeOrderID' : RechargeOrderID,
            'Price':int(Money),
            'RechargeType':RechargeType,
            '$time':time_sec_float,
            'OrderCreatedDate':OrderCreatedDate,
            'Diamond':int(Diamond)
            }
            sa.track(distinct_id, 'Recharge', properties)
            sa.close()
            return 1
        except Exception as e:
            Log.error("Recharge error code: %s"%(str(e)))
            if '10060' in str(str(e)):
              return 10060
            else:
              return -1
