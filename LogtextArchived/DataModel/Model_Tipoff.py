#coding=utf-8
class Model_Tipoff(object):
    """description of class"""

    #Id =0
    #SourceUid =0
    #Time =0
    #DestUid =0
    #Type =0
    #Coment =""
    #Detail=""

    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         SourceId INT(11) NOT NULL DEFAULT '0',
                         TipoffTime VARCHAR(256) NOT NULL DEFAULT '',
                         DestUid INT(11) NOT NULL DEFAULT '0',
                         TipoffType INT(11) NOT NULL DEFAULT '0',
                         Coment TEXT NOT NULL,
                         Detail VARCHAR(256) NOT NULL DEFAULT '',
                         KEY SourceId(SourceId),
                         KEY DestUid (DestUid),
                         KEY TipoffType (TipoffType)
                         )'''
        return sql
        
    def getInsertSql(self,tablename):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s,%s,%s)'''
        return sql


    def FormatData(self,tablename,arr):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s,%s,%s)'''
        return sql


