#coding=utf-8
class Model_Comment(object):
    """description of class"""
    #Id =0
    #Uid =0
    #CommentTime =0
    #HeroId =0
    #CommentText =0

    def getCreateTableSql(self,tablename):
        sql = '''create table if not exists '''+tablename+'''(
                         Id INT PRIMARY KEY AUTO_INCREMENT,
                         Uid INT(11) NOT NULL DEFAULT '0',
                         CommentTime VARCHAR(256) NOT NULL DEFAULT '',
                         HeroId int(11) NOT NULL DEFAULT '0',
                         CommentText TEXT NOT NULL,
                         KEY Uid (Uid),
                         KEY HeroId (HeroId)
                         )'''
        return sql
        
    def getInsertSql(self,tablename):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s)'''
        return sql


    def FormatData(self,tablename,arr):
        sql = '''insert into '''+tablename+''' values(NULL,%s,%s,%s,%s)'''
        return sql


