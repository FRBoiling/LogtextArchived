#coding=utf-8
import os
import re  
import sys 
import Mark
import Utils
import Log
import DataFactory
import DBManager
import SensorsanalyticsDdManger
import Config

class Func:
    db=None
    SSdb=None
    tableName = ""
    dbSwitch = 1
    ssSwich =1
    logPath =""
    backupPath=""
    errPath=""

    def __init__(self):
        self.db = DBManager.DBManager()
        if self.db ==None:
           Log.error("dbManager is None!")
        else:
           if self.db.DBconnect():
              self.dbSwitch = self.db.dbSwitch
           else:
              pass
        self.SSdb = SensorsanalyticsDdManger.SensorsanalyticsDdManger()
        if self.SSdb == None:
           Log.error("SSdbManager is None!")
        else:
           self.SSdb.SSDBconnect()
           self.ssSwich = self.SSdb.ssSwitch
        
        config = Config.Config()
        if config == None:
           Log.error("Config is None!")
        else:
           config.SetConfigPath("")
           constconfig=config.loadConstConfig();
           self.logPath = constconfig["log_path"]
           self.backupPath = constconfig["backup_path"]
           self.errPath = constconfig["err_path"]
        pass
    def Run(self):
        if self.ssSwich == 0 and self.dbSwitch==0:
           Log.war("No Function is running!Please check 'config.ini' to open switch!")
           pass
        else:
            list = Utils.GetFileList(self.logPath,[])
            count = len(list)
            if len(list)>0:
               Log.info(">>>Run")
               Log.info("find %s files"%(count))
            else:
               Log.info("%s is empty"%(self.logPath))
               return         
            for e in list:
                   if os.path.isfile(e) and ('.now' in e) >0:
                      pass
                   else:
                       if os.path.isfile(e) and ('.log' in e)>0:
                          #u'D:\\Src\\MCWY_30001_1_CONSUME_2016-11-01-21-20.log'
                          nA =e.rfind('\\')+1
                          strA =e[nA:-10]
                          nReadReturn =self.ReadFile(e)
                          if nReadReturn>0:
                              desPath = self.backupPath+'\\'+strA
                              if not os.path.exists(desPath):
                                 os.makedirs(desPath)
                              else:
                                 pass
                              if os.system("copy %s %s"%(e,desPath)) == 0:
                                 os.remove(e)
                                 Mark.deleteMark()
                              else:
                                  pass
                          elif nReadReturn<0:
                              errDir = self.errPath+'\\'+strA
                              if not os.path.exists(errDir):
                                 os.makedirs(errDir)
                              else:
                                  pass
                              if os.system("copy %s %s"%(e,errDir)) == 0:
                                 os.remove(e)
                              else:
                                  pass
                              pass
                          elif nReadReturn == 0:
                              Log.war("No Function is running!Please check 'config.ini' to open switch!")
                              pass
                       else:
                           pass
            Log.info(">>>Stop")

    def getDayTableName(self,arr):
        return arr[3]+"_"+arr[4][:10].replace("-","_")

    def getMonthTableName(self,arr):
        return arr[3]+"_"+arr[4][:7].replace("-","_")

    def getErrLogTableName():
        pass

    def AnalysisData(self,name,index,line):
        strline = line
        path = str(name)
        val = str(index)
        nA=path.rfind('\\')+1
        strHead =path[nA:]
        curtime=Utils.GetCurTime();
        arr=[path,val,curtime]
        swith = 0
        if 'errMark' in name:
           tempdata = strline.split('<>>>')
           strline = tempdata[2]
           if 'errMark_ss' in name:
               self.tableName= tempdata[1]
               swith = 2 #ss  error  only
           elif 'errMark_db' in name:
               self.tableName= tempdata[1]
               swith = 3 #db error only
           else:
               self.tableName = tempdata[1]
               swith = 1 #both error
               pass
        pro=DataFactory.DataFactory(self.tableName,strline.replace("\n",""),swith)

        nFlag = pro.work()
        if nFlag == 1:
           Mark.setMark(arr)
        if nFlag ==-1:
           Mark.setErrMark_db(self.tableName,strHead,strline);
        elif nFlag ==-2:
            Mark.setErrMark(self.tableName,strHead,strline);
        elif nFlag ==-3:
            Mark.setErrMark_ss(self.tableName,strHead,strline);
        elif nFlag == 0:
           pass

        return nFlag    

    def ReadFile(self,dir):
        nReturn = 1
        file_object = open(dir,'rb')
        try:
           name = file_object.name
           nIndex = name.find('errMark')
           if nIndex>0 :
              self.tableName = name[nIndex:]
              pass
           else:          
              arr =name.split('_')
              type = arr[3];
              try:
                getTableName  = {'CONSUME':lambda:self.getDayTableName(arr), 
                                'OBTAIN':lambda:self.getDayTableName(arr), 
                                'CREATECHAR':lambda:self.getDayTableName(arr), 
                                'LOGIN':lambda:self.getDayTableName(arr), 
                                'LOGOUT':lambda:self.getDayTableName(arr), 
                                'RECHARGE':lambda:self.getDayTableName(arr), 
                                'TASK':lambda:self.getDayTableName(arr), 
                                'ARENA':lambda:self.getDayTableName(arr), 
                                'ENTERMAP':lambda:self.getDayTableName(arr), 
                                'QUITMAP':lambda:self.getDayTableName(arr), 
                                'ONLINE':lambda:self.getDayTableName(arr),
                                'LISTENCHAT':lambda:self.getDayTableName(arr)
                                } 
                self.tableName= getTableName[type]() 
              except Exception as e:
                Log.error("GetDBtablename err at : %s"%(dir))
                Log.error("Func.ReadFile() error code: %s"%(str(e)))
                return -1
           #if self.db == None:
           #   pass
           #else:
           #   if self.db.dbSwitch == 1 :
           #      bRet=self.db.createTable(self.tableName)
           index = 0
           arrMark = Mark.readMark()
          
           if len(arrMark)==3:
                try:
                    if name in arrMark[0]:
                        for line in file_object:
                          index+=1
                          if index > int(arrMark[1]):
                             nRe = self.AnalysisData(name,index,line)
                             if nRe<0:
                                nReturn=nRe
                          else:
                             pass
                    else:
                         pass
                except Exception as e:
                    Log.error("DataFactory.work() error code: %s"%(str(e)))
           else:
                 for line in file_object:
                     index+=1
                     nR = self.AnalysisData(name,index,line.decode())
                     if nR<0:
                        nReturn=nR

        
           index=0
           return nReturn
        finally:
           Log.debug("Close File:\n%s"%(dir))
           if file_object==None:
              pass
           else:
              file_object.close()

   