#coding=utf-8
class Model_ListenChat(object):
    """description of class"""
    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         uid INT,
                         ServerID INT,
                         uName VARCHAR(256),
                         Level INT,
                         VipLevel INT,
                         Content TEXT,
                         Date VARCHAR(256),
                         State INT,
                         KEY idx_uid (uid)
                         )'''
        return sql
        
    def getInsertSql(self,tablename):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s,%s,%s,%s,1)'''
        return sql

