#coding=utf-8
class Model_Battle(object):
    """description of class"""
    #Id =0
    #PcUid =0
    #Account =""
    #PcName =""
    #PcLevel =0
    #ServerId =0
    #ChanelName =""
    #EndTime =0
    #BattleType =0
    #LadderLevel=0,
    #BattleResult =0
    #BattleTime =0
    #VedioName=""
    #Heros =""
    #Skills = ""
    #Param =""

    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         PcUid INT NOT NULL DEFAULT '0',
                         Account VARCHAR(256) NOT NULL DEFAULT '',
                         PcName VARCHAR(256) NOT NULL DEFAULT '',
                         PcLevel INT NOT NULL DEFAULT '0',
                         ServerId INT NOT NULL DEFAULT '0',
                         ChanelName VARCHAR(256) NOT NULL DEFAULT '',
                         BattleEndTime VARCHAR(256) NOT NULL DEFAULT '',
                         BattleType INT NOT NULL DEFAULT '0',
                         LadderLevel INT NOT NULL DEFAULT '0',
                         BattleResult INT NOT NULL DEFAULT '0',
                         BattleTime INT NOT NULL DEFAULT '0',
                         VedioName VARCHAR(256) NOT NULL DEFAULT '',
                         Heros VARCHAR(256) NOT NULL DEFAULT '',
                         Skills VARCHAR(256) NOT NULL DEFAULT '',
                         Param VARCHAR(256) NOT NULL DEFAULT '',
                         KEY PcUid (PcUid)
                         )'''
        return sql
        
    def getInsertSql(self,tablename):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        return sql


    def FormatData(self,tablename,arr):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        return sql


