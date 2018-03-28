#coding=utf-8
import time
import Log

class Single(object):    
    _state = {}  
    def __new__(cls, *args, **kw):    
        ob = super(Single, cls).__new__(cls, *args, **kw)    
        ob.__dict__ = cls._state    
        return ob   
import CleanUp
class Monitor(Single):
    """description of class"""
    NodeTime =0
    intervaltime = 10
    clean = None

    def __init__(self):
        import Config
        config = Config.Config()
        config=config.loadConfig()
        intervalConfig = config["clearconfig"]["clear"]
        self.intervaltime =int(intervalConfig["interval_day"])*60*60*24
        #self.intervaltime =int(intervalConfig["interval_day"])
        self.clean =CleanUp.CleanUp()
        pass
    def setNodeTime(self):
        self.NodeTime =time.time()
        pass

    def IsTime(self,timeStamp):
        if time.time() > timeStamp + int(self.intervaltime):
           return True
        else:
            return False
        pass

    def Run(self):
        if(self.IsTime(self.NodeTime)):
           Log.info(">>>CleanUp start")
           self.clean.Run()
           self.setNodeTime()
           Log.info(">>>CleanUp stop")
