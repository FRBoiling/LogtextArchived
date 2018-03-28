#coding=utf-8
import DBManager
import Log

class DataAnalysis_Obtain():
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
                     Log.error("DataAnalysis_Obtain.analysis() db error code: %s"%(str(e)))
                     return -1
            else:
                return 0         
            
               



