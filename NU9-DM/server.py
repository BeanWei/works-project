'''服务器端'''

from threading import Lock

import time
toDay = time.strftime("%Y%m%d")

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
# from flask_pymongo import PyMongo
import pymongo

async_mode = None

app = Flask(__name__) 
#使用默认的mongodb的配置 
# mongo = PyMongo(app)

with app.app_context():
    conn= pymongo.MongoClient('localhost', 27017)
    db = conn.test

socketio = SocketIO(app, async_mode=async_mode)

thread = None
thread_lock = Lock()


def call_data():
    '''从数据库中获取数据推送至前台'''
    count = 0
    series = []
    while True:
        #缓冲时间
        socketio.sleep(10)
        count += 1
        #获取y轴的数据
        for result in db.result.find({"date": toDay}):
            if time.strftime("%H%m") == "0000":
                series = []
            sn = result["sn"]
            logtime = result["logtime"]
            #data = db.data.find_one({"sn": sn, "logtime": logtime})            #TODO:logtime可能存在不等的情况
            data = db.data.find_one({"sn": sn})
            if data: 
                yaxis = data["yaxis"]
                series.append({
                    "name": sn,
                    "symbol":'none', 
                    "type": "line", 
                    "smooth": True, 
                    "lineStyle": {"color": "#00CD00"}, 
                    "data": yaxis
                    #TODO:增加辅助线（LIMMIT）
                    # "markLine": {
                    #     "name": "limmit",
                    #     "lineStyle": {"color": "red"}, 
                    #     "xAxis": {
                    #         "data": [100.000,106.000,112.000,118.000,125.000,132.000,140.000,150.000,160.000,170.000,180.000,190.000,200.000,212.000,224.000,236.000,250.000,265.000,280.000,300.000,315.000,335.000,355.000,375.000,400.000,425.000,450.000,475.000,500.000,530.000,560.000,600.000,630.000,670.000,710.000,750.000,800.000,850.000,900.000,950.000,1000.000,1060.000,1120.000,1180.000,1250.000,1320.000,1400.000,1500.000,1600.000,1700.000,1800.000,1900.000,2000.000]
                    #     },
                    #     "yAxis": {
                    #         "data": [0.224,0.199,0.303,0.353,0.299,0.652,0.586,0.618,0.632,0.469,0.370,0.403,0.367,0.312,0.249,0.236,0.252,0.188,0.172,0.118,0.143,0.093,0.077,0.070,0.044,0.056,0.040,0.062,0.041,0.052,0.041,0.025,0.046,0.035,0.030,0.029,0.030,0.032,0.023,0.026,0.018,0.028,0.028,0.024,0.026,0.029,0.040,0.010,0.021,0.022,0.009,0.011,0.006]
                    #     }
                    #     # "data": [
                    #     #     {
                    #     #         "xAxis": [100.000,106.000,112.000,118.000,125.000,132.000,140.000,150.000,160.000,170.000,180.000,190.000,200.000,212.000,224.000,236.000,250.000,265.000,280.000,300.000,315.000,335.000,355.000,375.000,400.000,425.000,450.000,475.000,500.000,530.000,560.000,600.000,630.000,670.000,710.000,750.000,800.000,850.000,900.000,950.000,1000.000,1060.000,1120.000,1180.000,1250.000,1320.000,1400.000,1500.000,1600.000,1700.000,1800.000,1900.000,2000.000],
                    #     #         "yAxis": [0.224,0.199,0.303,0.353,0.299,0.652,0.586,0.618,0.632,0.469,0.370,0.403,0.367,0.312,0.249,0.236,0.252,0.188,0.172,0.118,0.143,0.093,0.077,0.070,0.044,0.056,0.040,0.062,0.041,0.052,0.041,0.025,0.046,0.035,0.030,0.029,0.030,0.032,0.023,0.026,0.018,0.028,0.028,0.024,0.026,0.029,0.040,0.010,0.021,0.022,0.009,0.011,0.006]
                    #     #     }
                    #     # ]
                    # }
                })
            else:
                continue

        #获取当天的产量和Spk RB 的fail数量 TODO:提供日期的范围查询
        total = db.result.find({"date": toDay}).count()
        fail = db.result.find({"date": toDay, "result": "FAIL"}).count()
        socketio.emit(
            "my_response",
            {"data":{"todayTotal": total, "todayFail": fail, "yaxis": series}, "count": count},
            namespace='/show'
        )

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


'''与前端建立socket连接后，启动后台线程'''
@socketio.on('connect', namespace='/show')
def toconnect():
    global thread
    with thread_lock:
        if thread is None:
            thread =socketio.start_background_task(target=call_data)
    emit("my_response", {"data": 'Connected', "count": 0})


if __name__ == "__main__":
    socketio.run(app, debug=True)