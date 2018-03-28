#coding=utf-8
import datetime,time
import sensorsanalytics
import Model_Login
import Model_Logout
import Model_CreateChar
import Model_Recharge
import Model_Entermap
import Model_Quitmap
import Model_Task
import Model_Online
import Config
import Log

class SSDBSingle(object):    
    _state = {}  
    def __new__(cls, *args, **kw):    
        ob = super(SSDBSingle, cls).__new__(cls, *args, **kw)    
        ob.__dict__ = cls._state    
        return ob   

class SensorsanalyticsDdManger(SSDBSingle):
    """description of class"""
    #SERVER_URL = 'http://123.59.209.213:8006/sa?project=default'
    consumer = None
    ssSwitch = 1

    def __init__(self):
       
        pass
    
    def SSDBconnect(self):
        config = Config.Config()
        ssconfig=config.loadSensorsConfig()
        self.ssSwitch = config.getssSwitch();
        if self.ssSwitch==1:
           self.consumer=sensorsanalytics.DefaultConsumer(ssconfig["url"])
        else:
           self.consumer=None
           Log.war("ssDB switch is not 1")

    def send(self,tablename,items):
        if self.ssSwitch==1:
           arr = tablename.split('_')
           type = arr[0];
           try:
             calculation  = {'CONSUME':lambda:self.sendConsume(items), 
                             'OBTAIN':lambda:self.sendObtain(items), 
                             'CREATECHAR':lambda:self.sendCreateChar(items), 
                             'LOGIN':lambda:self.sendLogin(items), 
                             'LOGOUT':lambda:self.sendLogout(items), 
                             'RECHARGE':lambda:self.sendRecharge(items), 
                             'TASK':lambda:self.sendTask(items), 
                             'ARENA':lambda:self.sendArena(items), 
                             'ENTERMAP':lambda:self.sendEntermap(items), 
                             'QUITMAP':lambda:self.sendQuitmap(items), 
                             'ONLINE':lambda:self.sendOnline(items),
                             'LISTENCHAT':lambda:self.sendTest(items) 
                             }
             nflag = calculation[type]() 
             return nflag
           except Exception as e:
              Log.error("ss  send error code : %s"%(str(3)))
              return -1
        else:
           Log.war("ssDB switch is not 1")
           return 0

    
    def sendTest(self,items):    
        return 1
                 
    def sendConsume(self,items):    
        return 1

    def sendObtain(self,items):
        return 1

    def sendCreateChar(self,items):
        consumeModel = Model_CreateChar.Model_CreateChar()
        return consumeModel.sendSSNormal(self.consumer,items)

    def sendLogin(self,items):
        consumeModel = Model_Login.Model_Login()
        return consumeModel.sendSSNormal(self.consumer,items)

    def sendLogout(self,items):
        consumeModel = Model_Logout.Model_Logout()
        return consumeModel.sendSSNormal(self.consumer,items)

    def sendRecharge(self,items):
        consumeModel = Model_Recharge.Model_Recharge()
        return consumeModel.sendSSNormal(self.consumer,items)

    def sendArena(self,items):
        consumeModel = Model_Arena.Model_Arena()
        return consumeModel.sendSSNormal(self.consumer,items)
    
    def sendTask(self,items):
        consumeModel = Model_Task.Model_Task()
        return consumeModel.sendSSNormal(self.consumer,items)

    def sendEntermap(self,items):
        consumeModel = Model_Entermap.Model_Entermap()
        return consumeModel.sendSSNormal(self.consumer,items)

    def sendQuitmap(self,items):
        consumeModel = Model_Quitmap.Model_Quitmap()
        return consumeModel.sendSSNormal(self.consumer,items)

    def sendOnline(self,items):
        consumeModel = Model_Online.Model_Online()
        return consumeModel.sendSSNormal(self.consumer,items)

    def sendListenChat(self,items):
        return 1
  
#if __name__ == '__main__':
#    import SensorsanalyticsDdManger
#    mmm= SensorsanalyticsDdManger.SensorsanalyticsDdManger()
#    item=[]
#    mmm.testNormal(item)
#    print("stop")

