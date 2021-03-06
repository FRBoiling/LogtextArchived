﻿#coding=utf-8
class Model_Obtain(object):
    """description of class"""
    #Id =0
    #PcUid =0
    #Account =""
    #PcName =""
    #PcLevel =0
    #ServerId =0
    #ChanelName =""
    #DateTime =0
    #ObtainWay =0
    #ObtainType=0,
    #OriginalCount =0
    #ObtainCount =0
    #Param=""

    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         PcUid INT NOT NULL DEFAULT '0',
                         Account VARCHAR(256) NOT NULL DEFAULT '',
                         PcName VARCHAR(256) NOT NULL DEFAULT '',
                         PcLevel INT NOT NULL DEFAULT '0',
                         ServerId INT NOT NULL DEFAULT '0',
                         ChanelName VARCHAR(256) NOT NULL DEFAULT '',
                         DateTime VARCHAR(256) NOT NULL DEFAULT '',
                         ObtainWay VARCHAR(256) NOT NULL DEFAULT '',
                         ObtainType INT NOT NULL DEFAULT '0',
                         OriginalCount INT NOT NULL DEFAULT '0',
                         ObtainCount INT NOT NULL DEFAULT '0',
                         Param VARCHAR(256) NOT NULL DEFAULT '',
                         KEY PcUid (PcUid)
                         )'''
        return sql
        
    def getInsertSql(self,tablename):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        return sql


    def FormatData(self,tablename,arr):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        return sql


