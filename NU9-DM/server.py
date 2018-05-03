'''服务器端'''

from threading import Lock

import time
toDay = time.strftime("%Y%m%d")

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
from flask_pymongo import PyMongo

async_mode = None

app = Flask(__name__) 
#使用默认的mongodb的配置 
mongo = PyMongo(app)

socketio = SocketIO(app, async_mode=async_mode)

thread = None
thread_lock = Lock()


def call_data():
    '''从数据库中获取数据推送至前台'''
    series = []
    while True:
        #缓冲时间
        socketio.sleep(300)
        #获取y轴的数据
        for result in mongo.db.result.find({"date": toDay}):
            if time.strftime("%H%m") == "0000":
                series = []
            sn = result.sn
            logtime = result.logtime
            data = mongo.db.data.find_one({"sn": sn, "logtime": logtime})            #TODO:logtime可能存在不等的情况
            yaxis = data.yaxis
            series.append({"name": sn,"type": "line", "data": yaxis})

        #获取当天的产量和Spk RB 的fail数量 TODO:提供日期的范围查询
        total = mongo.db.result.find({"date": toDay}).count()
        fail = mongo.db.result.find({"date": toDay, "result": "FAIL"}).count()

        socketio.emit(
            "server_response",
            {"todayTotal": total, "todayFail": fail, "logs": series},
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


if __name__ == "__main__":
    socketio.run(app, debug=True)