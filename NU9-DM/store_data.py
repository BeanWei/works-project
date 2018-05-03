import pymongo

import os
import shutil
import time

server_path = ""

#获取当前时间来分类文件
toDay = time.strftime("%Y%m%d")

def get_data():
    '''操作server上的log并获取数据
    '''
    for (root, dirs, files) in os.walk(server_path):
        if toDay not in dirs:
            os.mkdir(toDay)
        for f in files:
            sn = f.split('_')[3]
            logtime = f.split('_')[-1]
            path = os.path.join(server_path,f)
            with open(path) as fp:
                try:
                    content = fp.readlines()
                    if "Result" in f:
                        handle_result(content, sn, logtime)
                    elif "Data" in f:
                        handle_data(content, sn, logtime)
                except:
                    shutil.move(path, os.path.join(server_path,toDay))
            #移动文件至今日建立的文件夹
            shutil.move(path, os.path.join(server_path,toDay))



def handle_result(content, sn, logtime):
    '''处理result'''
    c_content = list(zip(*content))   #行列转置
    #TODO: log中的具体行列
    if c_content[0].count("FAIL") == 1 and c_content[0][0] == "FAIL":
        result = "FAIL"
    else:
        result = "PASS"

    if db.result.find_one({"sn": sn}):
        return 
    db.result.save({"date": toDay, "sn": sn, "logtime": logtime, "result": result})



def handle_data(content, sn, logtime):
    '''处理data'''
    if "Spk Rub&Buzz" in content[0]:
        yaxis = content[0 + 2]

        db.data.save({"sn": sn, "logtime": logtime, "yaxis": yaxis})

conn = pymongo.MongoClient("127.0.0.1", 27017)
db = conn.test
get_data()