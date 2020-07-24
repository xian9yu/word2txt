import os
import subprocess

url = '/home/yayaya/Desktop/wps/old/'   #old files path

for root, dirs, fileName in os.walk(url):   #打印当前目录所有文件名(输出是一个切片)
    
    for i in fileName:
        oldName = os.path.basename(i)   #获取old name
        
        content = subprocess.check_output(["antiword",url + oldName])   #get old files binary bytes
       
        rellName=os.path.splitext(i)[0] #获取真文件名

        filePrefix = rellName   #文件前缀
        fileSuffix = '.txt'     #文件后缀
        fileNum = len(fileName) #文件个数

        fileName = '/home/yayaya/Desktop/wps/txt/' + filePrefix + fileSuffix    #new file path and name
       
        open(fileName,"w").write(fileName + '\n' + str(content))    #create file and write content