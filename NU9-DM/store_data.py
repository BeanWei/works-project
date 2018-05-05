import pymongo

import os
import shutil
import time

server_path = ".\\logs"

#获取当前时间来分类文件
toDay = time.strftime("%Y%m%d")

def get_data():
    '''操作server上的log并获取数据
    '''
    while True:
        for (root, dirs, files) in os.walk(server_path, topdown=False):
            
            if toDay not in dirs:
                try:
                    os.mkdir(server_path+"\\"+toDay)
                except OSError:
                        pass
        if files:
            for f in files:
                sn = f.split('_')[2]
                logtime = (f.split('_')[-1]).split('.')[0]
                path = os.path.join(server_path,f)
                with open(path) as fp:
                    try:
                        content = []
                        for l in fp.readlines():
                            content.append(l.split(','))
                        if "Result" in f:
                            handle_result(content, sn, logtime)
                        elif "Data" in f:
                            handle_data(content, sn, logtime)
                    except:
                        shutil.move(path, os.path.join(server_path,toDay))
                        print("异常文件%s已被移动" % f)
                        continue
                #移动文件至今日建立的文件夹
                shutil.move(path, os.path.join(server_path,toDay))
                print("%s处理成功并移至当日文件夹" % f)
        else:
            pass    



def handle_result(content, sn, logtime):
    '''处理result'''
    content = list(zip(*content))
    if content[3].count("FAIL") == 1 and content[3][3] == "FAIL":
        result = "FAIL"
    else:
        result = "PASS"
    if db.result.find_one({"sn": sn}):
        return 
    db.result.save({"date": toDay, "sn": sn, "logtime": logtime, "result": result})
    


def handle_data(content, sn, logtime):
    '''处理data'''
    if "Spk Rub" in content[9][0]:
        yaxis = content[11][0:53]
        db.data.save({"sn": sn, "logtime": logtime, "yaxis": yaxis})
        

conn = pymongo.MongoClient("127.0.0.1", 27017)
db = conn.test
get_data()