#coding=utf-8
import logging,os
import ctypes
 
FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x09 # 0x01 text color contains blue. 
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED = 0x04 # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN
 
STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


class Logger(object):
    """description of class"""
    def __init__(self, path,clevel = logging.DEBUG,Flevel = logging.ERROR):
      self.logger = logging.getLogger(path)
      self.logger.setLevel(logging.DEBUG)
      smt = logging.Formatter('[%(asctime)s][%(levelname)s]>%(message)s', '%Y-%m-%d %H:%M:%S')
      #fmt = logging.Formatter('[%(filename)s line:%(lineno)d][%(asctime)s][%(levelname)s]: %(message)s', '%d %b %Y %H:%M:%S') 
      #设置CMD日志
      sh = logging.StreamHandler()
      sh.setFormatter(smt)
      sh.setLevel(clevel)
      #设置文件日志
      fh = logging.FileHandler(path)
      fh.setFormatter(smt)
      fh.setLevel(Flevel)
      self.logger.addHandler(sh)
      self.logger.addHandler(fh)
 
    #def debug(self,message):
    #   self.logger.debug(message)
    
    #def info(self,message):
    #   self.logger.info(message)
    
    #def war(self,message):
    #   self.logger.warn(message)
    
    #def error(self,message):
    #   self.logger.error(message)
    
    #def cri(self,message):
    #   self.logger.critical(message)

    def debug(self,message,color=FOREGROUND_BLUE):
        set_color(color)
        self.logger.debug(message)
        set_color(FOREGROUND_WHITE)
 
    def info(self,message,color=FOREGROUND_GREEN):
        set_color(color)
        self.logger.info(message)
        set_color(FOREGROUND_WHITE)
    
    def war(self,message,color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warn(message)
        set_color(FOREGROUND_WHITE)
        
    def error(self,message,color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(message)
        set_color(FOREGROUND_WHITE)
    
    def cri(self,message):
        self.logger.critical(message)





#if __name__ =='__main__':
#    logyyx = Logger.Logger('yyx.log',logging.INFO,logging.DEBUG)
#    logyyx.debug("一个debug信息")
#    logyyx.info('一个info信息')
#    logyyx.war('一个warning信息')
#    logyyx.error('一个error信息')
#    logyyx.cri('一个致命critical信息')