#coding=utf-8
import configparser
import sys

class ConfigSingle(object):    
    _state = {}  
    def __new__(cls, *args, **kw):    
        ob = super(ConfigSingle, cls).__new__(cls, *args, **kw)    
        ob.__dict__ = cls._state    
        return ob  

class Config(ConfigSingle):
    partLable = ("<",">")
    sectionLable = ("[","]")
    endlineLable = "\r\n" # windows下的行标志
    #endlineLable = "\n"   # linux下的行标志
    equalLable = "=" # 赋值标志
    noteLable = '#' # 注释标志
    #configPath = sys.path[0]+"\config.ini"
    configPath = sys.path[0]+"\config.ini"

    def __init__(self):
       pass

    def SetConfigPath(self ,path):
        if path=="":
           self.configPath = sys.path[0]+"\config.ini"
        else:
           self.configPath =path
        
    # 得到总配置的map
    def getPlatformMap(self,strtmp,lable1 = partLable,lable2 = sectionLable):
        tmp = strtmp.decode("gb2312").split(lable1[0])
        tmp = [elem for elem in tmp if len(elem) > 1]
        tmp = [elem for elem in tmp if elem.rfind(lable1[1]) > 0]
        platdict = {}
        for elem in tmp:
            key = elem[0:elem.find(lable1[1]):]
            value = elem[elem.find(lable2[0])::]
            platdict[key] = value
        return platdict
    
    # 得到各部分的map
    def getSectionMap(self,strtmp,lable1 = sectionLable):
        tmp = strtmp.split(lable1[0])
        tmp = [elem for elem in tmp if len(elem) > 1]
        tmp = [elem for elem in tmp if elem.rfind(lable1[1]) > 0]
        sectionDict = {}
        for elem in tmp:
            key = elem[0:elem.find(lable1[1]):]
            value = elem[elem.find(self.endlineLable)+len(self.endlineLable)::]
            sectionDict[key] = value
        return sectionDict
    
    # 获取具体配置值
    def getValueMap(self,strtmp):
        tmp = strtmp.split(self.endlineLable)
        tmp = [elem for elem in tmp if len(elem) > 1]
        valueDict = {}
        for elem in tmp:
            if elem.find(self.noteLable) > 0: # 如果有注释则去掉注释
                elem = elem[0:elem.find(self.noteLable):]
            elem = ''.join(elem.split()) # 去掉空白字符
            key = elem[0:elem.find(self.equalLable):]
            value = elem[elem.find(self.equalLable)+len(self.equalLable)::]
            valueDict[key] = value
        return valueDict
    
    def loadConfig(self):
        f = open(self.configPath,"rb")
        strFileContent = f.read()
        f.close()
        vardict = {}
        
        var1 = self.getPlatformMap(strFileContent)
        
        for k,v in var1.items():
            var2 = self.getSectionMap(v)
            dict3 = {}
            for k2,v2 in var2.items():
                var3 = self.getValueMap(v2)
                dict3[k2] = var3
            vardict[k] = dict3
        return vardict
        
    def loadDbConfig(self):
        f = open(self.configPath,"rb")
        strFileContent = f.read()
        f.close()
        vardict = {}
        
        var1 = self.getPlatformMap(strFileContent)
        
        for k,v in var1.items():
            var2 = self.getSectionMap(v)
            dict3 = {}
            for k2,v2 in var2.items():
                var3 = self.getValueMap(v2)
                dict3[k2] = var3
            vardict[k] = dict3
        return vardict["dbconfig"]["global"]
        #print vardict["dbconfig"]["global"]["ip"]

    def loadConstConfig(self):
        f = open(self.configPath,"rb")
        strFileContent = f.read()
        f.close()
        vardict = {}
        
        var1 = self.getPlatformMap(strFileContent)
        
        for k,v in var1.items():
            var2 = self.getSectionMap(v)
            dict3 = {}
            for k2,v2 in var2.items():
                var3 = self.getValueMap(v2)
                dict3[k2] = var3
            vardict[k] = dict3
        return vardict["constconfig"]["global"]

    def loadSensorsConfig(self):
        f = open(self.configPath,"rb")
        strFileContent = f.read()
        f.close()
        vardict = {}
        
        var1 = self.getPlatformMap(strFileContent)
        
        for k,v in var1.items():
            var2 = self.getSectionMap(v)
            dict3 = {}
            for k2,v2 in var2.items():
                var3 = self.getValueMap(v2)
                dict3[k2] = var3
            vardict[k] = dict3
        return vardict["SensorsAnalyticsConfig"]["const"]
    
    def getdbSwitch(self):
        f = open(self.configPath,"rb")
        strFileContent = f.read()
        f.close()
        vardict = {}
        
        var1 = self.getPlatformMap(strFileContent)
        
        for k,v in var1.items():
            var2 = self.getSectionMap(v)
            dict3 = {}
            for k2,v2 in var2.items():
                var3 = self.getValueMap(v2)
                dict3[k2] = var3
            vardict[k] = dict3
        return int(vardict["dbconfig"]["other"]["swith"])


    def getssSwitch(self):
        f = open(self.configPath,"rb")
        strFileContent = f.read()
        f.close()
        vardict = {}
        
        var1 = self.getPlatformMap(strFileContent)
        
        for k,v in var1.items():
            var2 = self.getSectionMap(v)
            dict3 = {}
            for k2,v2 in var2.items():
                var3 = self.getValueMap(v2)
                dict3[k2] = var3
            vardict[k] = dict3
        return int(vardict["SensorsAnalyticsConfig"]["other"]["swith"])

#if __name__=="__main__":
#    import Config
#    config = Config.Config()
#    arr = {}
#    arr= config.loadConfig()
#    config=arr["dbconfig"]["global"]
#    print arr["dbconfig"]["global"]["ip"]
#    print arr["dbconfig"]["global"]["port"]
#    print arr["dbconfig"]["global"]["MAC"]
    