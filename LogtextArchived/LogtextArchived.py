#coding=utf-8
import os
import logging
import time
import Func
import Log
import Monitor

def run(interval, command):
     Log.info("*"*51)
     #log.print_ts("Command %s"%command)
     Log.info("Run every %s seconds."%interval)
     Log.info("*"*51)
     main = Func.Func()
     monitor = Monitor.Monitor()
     while True:
         try:
             # sleep for the remaining seconds of interval
             time_remaining = interval-time.time()%interval
             Log.info("Sleeping until %s(%.3f seconds).."%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime((time.time()+time_remaining))), time_remaining))
             time.sleep(time_remaining)
             Log.info("-"*51)
             #log.print_ts("Starting command.")
             Log.info("Starting Run...")
             # execute the command
             main.Run()
             monitor.Run()
             Log.info("Stop...")
             #status = os.system(command)
             Log.info("-"*51)
             #log.print_ts("Command status = %s."%status)
         except Exception as e:
             Log.error("LogtextArchived.run() error code: %s"%(str(e)))

#if __name__=="__main__":
#    interval = 1
#    command = r'ifconfig'
#    run(interval, command)
#    #Func.Run()

