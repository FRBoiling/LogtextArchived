#coding=utf-8
import DBManager
import Log

#YYZJ_CONSUME|703|1|1|1|1001|IOS|111122222|20180116|BattleWin|504|1000|29|0
class DataAnalysis_Consume():
     m_tableName = ''
     arr=[]
     db = None
     def __init__(self,tablename,arr):
         self.m_tableName=tablename 
         self.arr = arr
         self.db = DBManager.DBManager()

     def analysis(self):
        items =[]
        for i in range(1, len(self.arr)):
            if (i!=8):
                items.append(self.arr[i])
        
        if self.db == None:
           Log.error("dbManager is None!")
           return -1
        else:
           if self.db.dbSwitch == 1:
              try:
                  bRet=self.db.insert(self.m_tableName,items)
                  return bRet
              except Exception as e:
                  Log.error("DataAnalysis_Consume.analysis() db error code: %s"%(str(e)))
                  return -1
           else:
                return 0
            
          



