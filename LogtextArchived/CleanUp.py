#coding=utf-8
import Config
import Log

class CleanUp(object):
    """description of class"""
    intervaltime = 10
    needCleanupPaths = []

    def __init__(self):
        config = Config.Config()
        config = config.loadConfig()
        constConfig = config["clearconfig"]["clear"]
        self.needCleanupPaths =str(constConfig["needcleanup_paths"]).split(';')
        pass

    def Run(self):
        if len(self.needCleanupPaths)>0:
            for s in self.needCleanupPaths:
               if s!='':
                  self.CleanUpDir(s);

    def IsUsefulDir(self,dirName):
        if len(self.needCleanupPaths)>0:
            for s in self.needCleanupPaths:
                if s==dirName:
                    return True
        return False

    def CleanUpDir(self,dirName):
        import os
        if os.path.isdir(dirName):
           if not os.listdir(dirName):
               #删除空文件夹
               if not self.IsUsefulDir(dirName):
                  os.rmdir(dirName)
           else:
              for s in os.listdir(dirName):
                 newName = os.path.join(dirName,s)
                 if os.path.isfile(newName): 
                   if '.now' in newName:
                      pass
                   else:
                     if '.log' in newName or '.txt' in newName:
                        self.CleanUpFile(newName)
                 elif os.path.isdir(newName):
                    self.CleanUpDir(newName)
                    pass
              #删除空文件夹
              if not os.listdir(dirName):
                 if not self.IsUsefulDir(dirName):
                    os.rmdir(dirName)
        else:
            Log.error("Can not find the dir:%s"%(dirName))

    def CleanUpFile(self,fileName):
        import os
        ctime = os.path.getctime(fileName)
        import Monitor
        monitor = Monitor.Monitor()
        if monitor.IsTime(int(ctime)):
            self.removeFile(fileName)
        pass

    def removeDir(self,dirName):
        #删除非空文件夹
        import shutil
        shutil.rmtree(dirName)
        pass
    def removeFile(self,fileName):
        import os
        os.remove(fileName)
        pass

#if __name__ == "__main__":
#    import CleanUp
#    import Monitor

#    #monitor = Monitor.Monitor()
#    #monitor.setNodeTime()
#    #import testClass
#    #test = testClass.testClass()
#    #test.setNodeTime()

#    clean = CleanUp.CleanUp()
#    clean.Run()

