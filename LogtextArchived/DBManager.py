#coding=utf-8
import sys
import MySql
import Model_Consume
import Model_Obtain
import Model_CreateChar
import Model_Login
import Model_Logout
import Model_Recharge
import Model_Task
import Model_Entermap
import Model_Quitmap
import Model_Online
import Model_ListenChat
import Model_Battle
import Model_Comment
import Model_Tipoff
import Config
import Log

class DBsingle(object):    
    _state = {}  
    def __new__(cls, *args, **kw):    
        ob = super(DBsingle, cls).__new__(cls, *args, **kw)    
        ob.__dict__ = cls._state    
        return ob   

class DBManager(DBsingle):
    db = None
    dbSwitch = 1
    def __init__(self):
        pass
       
    def DBconnect(self):
        config = Config.Config()
        dbconfig = config.loadDbConfig()
        dbconfig["port"] = int(dbconfig["port"])
        self.dbSwitch = config.getdbSwitch()
        if self.dbSwitch == 1:
            try:
                Log.info("DB is ready to connect,please wait...!")
                self.db = MySql.MySql(dbconfig)
                if self.db == None:
                    return False
                else:
                    Log.info("DB is connected success !")
                    return True
            except Exception as e:
                Log.error("Mqsql error code: %s" % (str(e.args)))
                return False
        else:
           self.db = None
           Log.war("DB switch is not 1")
        return True
          
    def createTable(self,tablename):
        arr = tablename.split('_')
        type = arr[0]
        try:
          calculation = {
                          'CONSUME':lambda:self.getCreateSqlConsume(tablename), 
                          'OBTAIN':lambda:self.getCreateSqlObtain(tablename), 
                          'LOGIN':lambda:self.getCreateSqlLogin(tablename), 
                          'LOGOUT':lambda:self.getCreateSqlLogout(tablename), 
                          'BATTLE':lambda:self.getCreateSqlBattle(tablename),
                          'COMMENT':lambda:self.getCreateSqlComment(tablename),
                          'TIPOFF':lambda:self.getCreateSqlTipoff(tablename),
                          'CREATECHAR':lambda:self.getCreateSqlCreateChar(tablename),
                          'RECHARGE':lambda:self.getCreateSqlRecharge(tablename), 
                          'TASK':lambda:self.getCreateSqlTask(tablename), 
                          'ENTERMAP':lambda:self.getCreateSqlEntermap(tablename), 
                          'QUITMAP':lambda:self.getCreateSqlQuitmap(tablename), 
                          'ONLINE':lambda:self.getCreateSqlOnline(tablename),
                          'LISTENCHAT':lambda:self.getCreateSqlListenChat(tablename)
                          }
          sql = calculation[type]() 
          if self.dbSwitch == 1:
             result = self.db.query(sql)
             return 1
          else:
             Log.war("DB switch is not 1")
             return 0
        except Exception as e:
            Log.error("DBManager get CreateSql error code: %s" % (str(e)))
            return -1
        #if result == False:
        #    print("create return false");
 
    def getCreateSqlConsume(self,tablename):
        consumeModel = Model_Consume.Model_Consume()
        return consumeModel.getCreateTableSql(tablename)
    def getCreateSqlObtain(self,tablename):
        consumeModel = Model_Obtain.Model_Obtain()
        return consumeModel.getCreateTableSql(tablename)
        
    def getCreateSqlCreateChar(self,tablename):
        consumeModel = Model_CreateChar.Model_CreateChar()
        return consumeModel.getCreateTableSql(tablename)
    
    def getCreateSqlLogin(self,tablename):
        consumeModel = Model_Login.Model_Login()
        return consumeModel.getCreateTableSql(tablename)

    def getCreateSqlLogout(self,tablename):
        consumeModel = Model_Logout.Model_Logout()
        return consumeModel.getCreateTableSql(tablename)

    def getCreateSqlRecharge(self,tablename):
        consumeModel = Model_Recharge.Model_Recharge()
        return consumeModel.getCreateTableSql(tablename)

    def getCreateSqlTask(self,tablename):
        consumeModel = Model_Task.Model_Task()
        return consumeModel.getCreateTableSql(tablename)

    def getCreateSqlEntermap(self,tablename):
        consumeModel = Model_Entermap.Model_Entermap()
        return consumeModel.getCreateTableSql(tablename)

    def getCreateSqlQuitmap(self,tablename):
        consumeModel = Model_Quitmap.Model_Quitmap()
        return consumeModel.getCreateTableSql(tablename)

    def getCreateSqlOnline(self,tablename):
        consumeModel = Model_Online.Model_Online()
        return consumeModel.getCreateTableSql(tablename)

    def getCreateSqlListenChat(self,tablename):
        consumeModel = Model_ListenChat.Model_ListenChat()
        return consumeModel.getCreateTableSql(tablename)

    def getCreateSqlBattle(self,tablename):
        consumeModel = Model_Battle.Model_Battle()
        return consumeModel.getCreateTableSql(tablename)
   
    def getCreateSqlComment(self,tablename):
        consumeModel = Model_Comment.Model_Comment()
        return consumeModel.getCreateTableSql(tablename)
    
    def getCreateSqlTipoff(self,tablename):
        consumeModel = Model_Tipoff.Model_Tipoff()
        return consumeModel.getCreateTableSql(tablename)



    def insert(self,tablename,items):
        nCreated = self.createTable(tablename)
        if nCreated == -1 or nCreated == 0:
            return nCreated
        arr = tablename.split('_')
        type = arr[0]
        try:
          calculation = {'CONSUME':lambda:self.getInsertSqlConsume(tablename), 
                          'OBTAIN':lambda:self.getInsertSqlObtain(tablename), 
                          'LOGIN':lambda:self.getInsertSqlLogin(tablename), 
                          'LOGOUT':lambda:self.getInsertSqlLogout(tablename), 
                          'BATTLE':lambda:self.getInsertSqlBattle(tablename),
                          'COMMENT':lambda:self.getInsertSqlComment(tablename),
                          'TIPOFF':lambda:self.getInsertSqlTipoff(tablename),
                          'CREATECHAR':lambda:self.getInsertSqlCreateChar(tablename), 
                          'RECHARGE':lambda:self.getInsertSqlRecharge(tablename), 
                          'TASK':lambda:self.getInsertSqlTask(tablename), 
                          'ENTERMAP':lambda:self.getInsertSqlEntermap(tablename), 
                          'QUITMAP':lambda:self.getInsertSqlQuitmap(tablename), 
                          'ONLINE':lambda:self.getInsertSqlOnline(tablename),
                          'LISTENCHAT':lambda:self.getInsertSqlListenChat(tablename)
                          }
          sql = calculation[type]() 

          if self.dbSwitch == 1:
             id = self.db.insertParam(sql,items)
             if id == False:
                print("insert return false")
                return -1
             return 1
          else:
             Log.war("DB switch is not 1")
             return 0
          
        except Exception as e:
            Log.error("DBManager get insertSql error code: %s" % (str(e)))
            return -1

    def getInsertSqlConsume(self,tablename):
        Model = Model_Consume.Model_Consume()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlObtain(self,tablename):
        Model = Model_Obtain.Model_Obtain()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlCreateChar(self,tablename):
        Model = Model_CreateChar.Model_CreateChar()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlLogin(self,tablename):
        Model = Model_Login.Model_Login()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlLogout(self,tablename):
        Model = Model_Logout.Model_Logout()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlRecharge(self,tablename):
        Model = Model_Recharge.Model_Recharge()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlTask(self,tablename):
        Model = Model_Task.Model_Task()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlEntermap(self,tablename):
        Model = Model_Entermap.Model_Entermap()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlQuitmap(self,tablename):
        Model = Model_Quitmap.Model_Quitmap()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlOnline(self,tablename):
        Model = Model_Online.Model_Online()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlListenChat(self,tablename):
        Model = Model_ListenChat.Model_ListenChat()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlBattle(self,tablename):
        Model = Model_Battle.Model_ListenChat()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlComment(self,tablename):
        Model = Model_Comment.Model_Comment()
        sql = Model.getInsertSql(tablename)
        return sql

    def getInsertSqlListenChat(self,tablename):
        Model = Model_Tipoff.Model_Tipoff()
        sql = Model.getInsertSql(tablename)
        return sql
    
    def select(self,tablename):
        sql = "select * from " + tablename
        self.db.query(sql)
        result = self.db.fetchAllRows()
        return result

#if __name__ == '__main__':
#    db1 = DBManager()
#    tablename ="testtable22"
#    db1.createTable(tablename)
#    arr1 =("testststst333")
#    arr2 =(0,"testststst","33333")
#    db1.insert(tablename,arr2)
  