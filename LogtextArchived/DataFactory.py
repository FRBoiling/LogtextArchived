#coding=utf-8
import DataAnalysis_Consume
import DataAnalysis_Obtain
import DataAnalysis_CharBaseAction
import DataAnalysis_CreateChar
import DataAnalysis_Battle
import Log

class DataFactory():
     m_tablename = ''
     data=[]
     swith =1
     def __init__(self,tablename,data,swith):
         self.m_tablename=tablename 
         self.data = data.split('|')
         self.swith =swith
     def work(self):
        arr = self.m_tablename.split('_')
        type = arr[0];
        try:
          calculation  = {'CONSUME':lambda:self.DataAnalysis_CONSUME(), 
                          'OBTAIN':lambda:self.DataAnalysis_OBTAIN(), 
                          'LOGIN':lambda:self.DataAnalysis_CHARBASEACTION(), 
                          'LOGOUT':lambda:self.DataAnalysis_CHARBASEACTION(), 
                          'BATTLE':lambda:self.DataAnalysis_Battle(),
                          'COMMENT':lambda:self.DataAnalysis_CHARBASEACTION(),
                          'TIPOFF':lambda:self.DataAnalysis_CHARBASEACTION(),
                          'CREATECHAR':lambda:self.DataAnalysis_CREATECHAR(), 
                          'RECHARGE':lambda:self.DataAnalysis_CHARBASEACTION(), 
                          'TASK':lambda:self.DataAnalysis_CHARBASEACTION(), 
                          'ENTERMAP':lambda:self.DataAnalysis_CHARBASEACTION(), 
                          'QUITMAP':lambda:self.DataAnalysis_CHARBASEACTION(), 
                          'ONLINE':lambda:self.DataAnalysis_CHARBASEACTION(),
                          'LISTENCHAT':lambda:self.DataAnalysis_CHARBASEACTION(),
                          } 
          nSuccess= calculation[type]() 
          return nSuccess
        except Exception as e:
          Log.error("DataFactory.work() error code: %s"%(str(e)))
          return -1
        #if result == False:
        pass

     def DataAnalysis_CONSUME(self):
         analysis = DataAnalysis_Consume.DataAnalysis_Consume(self.m_tablename,self.data)
         return analysis.analysis()
     
     def DataAnalysis_OBTAIN(self):
         analysis = DataAnalysis_Obtain.DataAnalysis_Obtain(self.m_tablename,self.data)
         return analysis.analysis()

     def DataAnalysis_Battle(self):
         analysis = DataAnalysis_Battle.DataAnalysis_Battle(self.m_tablename,self.data)
         return analysis.analysis()

     def DataAnalysis_CHARBASEACTION(self):
         analysis = DataAnalysis_CharBaseAction.DataAnalysis_CharBaseAction(self.m_tablename,self.data,self.swith)
         return analysis.analysis()

     def DataAnalysis_CREATECHAR(self):
         analysis = DataAnalysis_CreateChar.DataAnalysis_CreateChar(self.m_tablename,self.data,self.swith)
         return analysis.analysis()

     #def DataAnalysis_BATTLE(self):
     #    analysis = DataAnalysis_CreateChar.DataAnalysis_CharBaseAction(self.m_tablename,self.data,self.swith)
     #    return analysis.analysis()

     #def DataAnalysis_LOGIN(self):
     #    analysis = DataAnalysis_CharBaseAction.DataAnalysis_CharBaseAction(self.m_tablename,data)
     #    return analysis.analysis()

     #def DataAnalysis_LOGOUT(self):
     #    analysis = DataAnalysis_CharBaseAction.DataAnalysis_CharBaseAction(self.m_tablename,data)
     #    return analysis.analysis()

     #def DataAnalysis_RECHARGE(self):
     #    analysis = DataAnalysis_CharBaseAction.DataAnalysis_CharBaseAction(self.m_tablename,data)
     #    return analysis.analysis()

     #def DataAnalysis_TASK(self):
     #    analysis = DataAnalysis_CharBaseAction.DataAnalysis_CharBaseAction(self.m_tablename,data)
     #    return analysis.analysis()

     #def DataAnalysis_ENTERMAP(self):
     #    analysis = DataAnalysis_CharBaseAction.DataAnalysis_CharBaseAction(self.m_tablename,data)
     #    return analysis.analysis()

     #def DataAnalysis_QUITMAP(self):
     #    analysis = DataAnalysis_CharBaseAction.DataAnalysis_CharBaseAction(self.m_tablename,data)
     #    return analysis.analysis()

     #def DataAnalysis_ONLINE(self):
     #    analysis = DataAnalysis_CharBaseAction.DataAnalysis_CharBaseAction(self.m_tablename,data)
     #    return analysis.analysis()

