from setuptools import setup,setuptools 
#import py2exe

#setup(console=["LogtextArchived.py"])

#options = {"py2exe":{ "dll_excludes": [ "OLEAUT32.dll", "USER32.dll", "SHELL32.dll","ole32.dll","ADVAPI32.dll","CRYPT32.dll","WS2_32.dll","GDI32.dll","VERSION.dll","KERNEL32.dll"] }}  
#setup(
#    options = options, 
#    description = "LogtextArchived",  
#    console=[{"script": "LogtextArchived.py"}]
#    )
#list = []
#modules=[]
#Utils.GetFileList('./',list)
#for e in list:
#    if os.path.isfile(e) and (e.find('.py') >0 or e.find('.ini')) >0 :
#       if e.find('.pyc')>0:
#           pass
#       else:
#           module = e.split('/')[1].split('.')
#           modules.append(module[0])

#setup(  
#    name        ='DBTransfer',  
#    version     ='1.0.0',  
#    author      ='FR',  
#    packages=   setuptools.find_packages(exclude=['./']),
#    author_email='fanrong@iwanxin.cn',  
#    description ='A simple data transfer tool!' 
#    ) 

setup(

    packages = find_packages('src'), 
    package_dir = {'':'src'},   
    package_data = {
        '': ['*.ini'],
        'sensorsanalytics': ['*.pc'],
    }
)