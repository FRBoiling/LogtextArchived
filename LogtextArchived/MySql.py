#coding=utf-8
import pymysql
import time
import Log

class MySql(object):
    error_code = '' #MySQL错误号码
    error_msg = ''#错误信息
    _instance = None #本类的实例
    _conn = None # 数据库conn
    _cur = None #游标
    _TIMEOUT = 30 #默认超时30秒
    _timecount = 0   
    def __init__(self, dbconfig):
    #'构造器：根据数据库连接参数，创建MySQL连接'
        try:
        	self._conn =pymysql.connect(host=dbconfig['host'],
        								 port=dbconfig['port'], 
        								 user=dbconfig['user'],
        								 passwd=dbconfig['passwd'],
        								 db=dbconfig['db'],
        								 charset=dbconfig['charset'])
        except pymysql.Error as e:
        	self.error_code = e.args[0]
        	error_msg = 'MySQL error! ', e.args[0], e.args[1]
        	#print error_msg

        	if self._timecount < self._TIMEOUT:
        	   interval = 5
        	   self._timecount += interval
        	   time.sleep(interval)
        	   return self.__init__(dbconfig)
        	else:
        		raise Exception(error_msg)
      
        self._cur = self._conn.cursor()
        self._instance = pymysql 
        
    def query(self,sql):
        #'执行 SELECT 语句'	 
        try:
            self._cur.execute("SET NAMES utf8mb4") 
            result = self._cur.execute(sql)
        except pymysql.Error as e:
            self.error_code = e.args[0]
            if self.error_code == 2006:
               self.reConn()
               self.query(sql)
           
            #print "数据库错误代码:",e.args[0],e.args[1]
            self.error_msg = str(e)
            Log.error("Mysql qurery Error: \n  %s"%self.error_msg)
            result = False
        return result

    def update(self,sql):
        #'执行 UPDATE 及 DELETE 语句'
        try:
            self._cur.execute("SET NAMES utf8") 
            result = self._cur.execute(sql)
            self._conn.commit()
        except pymysql.Error as e:
               self.error_code = e.args[0]
               #print "数据库错误代码:",e.args[0],e.args[1]
               self.error_msg = str(e)
               Log.error("Mysql update Error: \n  %s"%self.error_msg)
               result = False
        return result

    def insert(self,sql):
        #'执行 INSERT 语句。如主键为自增长int，则返回新生成的ID'
        try:
            self._cur.execute("SET NAMES utf8")
            self._cur.execute(sql)
            self._conn.commit()
            return self._conn.insert_id()
        except pymysql.Error as e:
            self.error_code = e.args[0]
            self.error_msg = str(e)
            Log.error("Mysql update Error: \n  %s"%self.error_msg)
            return False

    def insertParam(self,sql,params):
        try:
            self._cur.execute("SET NAMES utf8")
            self._cur.execute(sql,params)
            lastrowid = self._cur.lastrowid
            self._conn.commit()
            return lastrowid
        #except Exception as e:
        #    return False
        except pymysql.Error as e:
            self.error_code = e.args[0]
            self.error_msg = str(e)
            if self.error_code == 2006 or self.error_code == 2003:
               self.reConn()
               self.insertParam(sql,params)
            Log.error("Mysql insert Error: \n  %s\n  %s"%self.error_msg,sql)
            return False
        pass

    def fetchAllRows(self):
        #'返回结果列表'
        return self._cur.fetchall()

    def fetchOneRow(self):
        #'返回一行结果，然后游标指向下一行。到达最后一行以后，返回None'
        return self._cur.fetchone()
 
    def getRowCount(self):
        #'获取结果行数'
        return self._cur.rowcount

    def commit(self):
        #'数据库commit操作'
        self._conn.commit()

    def rollback(self):
        #'数据库回滚操作'
        self._conn.rollback()#
    
    def __del__(self):
        #'释放资源（系统GC自动调用）'
        try:
            self._cur.close()
            self._conn.close()
        except:
            pass

    def  close(self):
        #'关闭数据库连接'
        self.__del__()


    def conn (self):  
        try:  
            self.__init__(dbconfig)  
            return True  
        except :  
            return False  

    def reConn (self):   
        status = True  
        while status:  
            try:  
                self._conn.ping(True)       #cping 校验连接是否异常  
                status = False  
            except:  
                if self.conn()==True: #重新连接,成功退出  
                    status = False  
                    break   
                time.sleep(3)      #连接不成功,休眠3秒钟,继续循环


if __name__ == '__main__':
	'''使用样例'''
	import MySql  
	#数据库连接参数  
	dbconfig = {'host':'localhost', 
				'port': 3306, 
				'user':'root', 
				'passwd':'root', 
				'db':'mytestdb', 
				'charset':'utf8'}
	#连接数据库，创建这个类的实例
	db = MySql.MySql(dbconfig)
	#操作数据库
	#sql = "SELECT * FROM `sample_table`"
	sql = '''insert into '''+'''test'''+''' values(%s,%s)'''
	#db.query(sql);
	db.insertParam(sql,[1,None]);
	#获取结果列表
	#result = db.fetchAllRows();
	#相当于php里面的var_dump
	print (result)
	#对行进行循环
	for row in result:
		#使用下标进行取值
		#print row[0]
		#对列进行循环
		for colum in row:
			print (colum)

	#关闭数据库
	db.close()