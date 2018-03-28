#coding=utf-8
import DBManager
import SensorsanalyticsDdManger
import Log
import Config
import Utils

class DataAnalysis_CreateChar():
     m_tableName = ''
     arr=[]
     db = None
     SSdb = None
     Swith = 0
     def __init__(self,tablename,arr,swith):
         self.m_tableName=tablename 
         self.arr = arr
         self.db = DBManager.DBManager()
         self.Swith =swith

     def analysis(self):
        items =[]
        bRet = 1
        bSSRet = 1
        #self.arr:  MCWY_CREATECHAR|1884|1002|5044|8795145|米莉ぅ笆笆拉|2016-12-30 22:58:44
        for i in range(1, len(self.arr)):
            items.append(self.arr[i])
        items[4] = Utils.filter_emoji(items[4],'??')   #charName字段过滤非法emoji字符
        strLog =self.arr[0]+'|'+ '|'.join(items)
        Log.debug("analysis data :\n %s"%strLog)

        if self.db == None:
           Log.error("dbManager is None!")
           bRet = -1
        else:
            bRet=self.db.dbSwitch
            if self.db.dbSwitch == 0 or self.Swith==2:
                pass
            else:
               try:
                   bRet=self.db.insert(self.m_tableName,items)
                   if bRet ==1:
                      Log.debug("db input successed !")
                   elif bRet==-1:
                      Log.error("db input failed: \n   %s"%strLog)
               except Exception as e:
                   Log.error("DataAnalysis_CharBaseAction.analysis() db error code: %s"%(str(e)))
                   bRet = -1

        self.SSdb = SensorsanalyticsDdManger.SensorsanalyticsDdManger()
        if self.SSdb == None:
           Log.error("SSdbManager is None!")
           bSSRet = -1
        else:
            bSSRet=self.SSdb.ssSwitch
            if self.SSdb.ssSwitch == 0 or self.Swith==3:
                pass
            else:
                if self.SSdb.ssSwitch ==1:
                   try:
                       bSSRet=self.SSdb.send(self.m_tableName,items)
                       if bSSRet==1:
                          Log.debug("ssDb input successed !")
                       else:
                          Log.war("ssDb input errcode:  %s"%(str(bSSRet)))
                          Log.war("ssDb input failed:\n  %s"%strLog)
                          Log.war("errline second send begin...")
                          bSSRet=self.SSdb.send(self.m_tableName,items)
                          Log.war("errline second send end...")
                       if bSSRet == -1:
                          Log.error("ssDb input failed: \n  %s"%strLog)
                   except Exception as e:
                       Log.error("DataAnalysis_CharBaseAction.analysis() SSdb error code: %s"%(str(e)))
                       bSSRet=-1

        if bRet==-1 and bSSRet >=0:
            return -1   
        if bRet==-1 and bSSRet==-1:
            return -2
        if bSSRet==-1 and bRet >=0:
            return -3
        elif bRet==0 and bSSRet==0:
            return 0 
        else:
            return 1

