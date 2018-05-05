# -*- coding: utf-8 -*-
# bulid by Bean_Wei/ 2018/1/18 8:24

from pyecharts import Line,Page,Grid
import numpy as np
import pandas as pd
import csv,os,shutil,time


def blend_files(all_logs_path):
    global files_number
    file_name_list=os.listdir(all_logs_path)
    if len(file_name_list) != 0:
        out_file=open("logs.txt",'w+')
        for file_name in file_name_list:
            try:
                if file_name.lower().endswith('.txt'):
                    log_info=file_name.split('_')[2]+'('+file_name.split('_')[3]+'-'+file_name.split('_')[4].split('.')[0]+')'
                    with open(all_logs_path+file_name,'rb') as fp:
                        out_file.write(log_info+'\n')
                        out_file.write(fp.read())
                else:
                    print u"%s文件后缀不是[.txt],并移至[error]文件夹中"%file_name
                    shutil.move(all_logs_path+file_name,"./error/")
            except Exception as e:
                print e,u"%s文件写入出错(请检查该文件名格式或文件类型),并移至[error]文件夹中"%file_name
                shutil.move(all_logs_path+file_name,"./error/")
        out_file.close()
        error_files=len(os.listdir("./error/"))
        files_number=len(os.listdir(all_logs_path))
        if files_number !=0 :
            print u"全部log已处理完毕,[Error]文件%s个并移至[error]文件夹中,[OK]文件%s个并已成功写入logs.txt中" % (error_files,files_number)
            return True
        else:
            print u"全部log已处理完毕,没有可以绘制的Log,请检查Log类型"
            return False
    else:
        print u"Log为空，请存放需要绘制的log至该文件夹然后再运行此程序"
        return False

def get_division():
    i=0
    head=""
    for cr in csv.reader(open("logs.txt",'r') ):
        if i==0:
            head=cr[0][:3]
        else:
            if cr[0][:3]==head:
                return i
                break
        i+=1

def get_data(data_path):
    with open(data_path,'rb') as fp:
        read_file=csv.reader(fp)
        data_list=[]
        for line in read_file:
            dt=93-len(line)
            if dt != 0:
                line=line+['NaN']*dt
            data_list.append(line)
        change_data_list=map(list,zip(*data_list))
        data=pd.DataFrame(change_data_list)
        return data

def get_limit_data(title,limit_path):
    limit_data=get_data(limit_path)
    dic_limit={}
    for col in range((limit_data.shape[1])/3):
        limit_title=[t[3*col] for t in limit_data.values][0]
        dic_limit[limit_title]=3*col
    title_Upper=title+" "+"margin Upper Limit"
    title_Lower=title+" "+"margin Lower Limit"
    #print title_Lower,title_Upper
    x_Upper=None
    y_Upper=None
    x_Lower=None
    y_Lower=None
    index_title_Upper=dic_limit.get(title_Upper)
    index_title_Lower=dic_limit.get(title_Lower)
    if index_title_Upper  != None:
        x_Upper=[i[index_title_Upper+1] for i in limit_data.values]
        while 'NaN' in x_Upper:
            x_Upper.remove('NaN')
        y_Upper=[i[index_title_Upper+2] for i in limit_data.values]
        while 'NaN' in y_Upper:
            y_Upper.remove('NaN')
    if index_title_Lower != None:
        x_Lower=[i[index_title_Lower+1] for i in limit_data.values]
        while 'NaN' in x_Lower:
            x_Lower.remove('NaN')
        y_Lower=[i[index_title_Lower+2] for i in limit_data.values]
        while 'NaN' in y_Lower:
            y_Lower.remove('NaN')
    return x_Upper,y_Upper,x_Lower,y_Lower

def get_pic_html():
    data=get_data("logs.txt")
    #获取DataFrame的行数
    rows=data.shape[0]
    #获取DataFrame的列数
    columns=data.shape[1]
    #绘制多幅图在一个页面，实例Page
    page=Page()
    #两个相同类型的曲线图间隔的列数
    # division=get_division()
    division = (int(columns)/int(files_number))
    for index in range((division-1)/3):
        type=[i[3*index+1] for i in data.values]
        title=type[0]
        subtitle=type[11]
        if "Sensitivity" not in title:
            line_pic=Line(title,subtitle)
            for compare in range(files_number):
                #添加曲线的limit
                if OK_Limit == True:
                    limit_path="./limit/%s" % (station+".txt")
                    x_Upper,y_Upper,x_Lower,y_Lower=get_limit_data(title,limit_path)
                    if x_Upper != None and y_Upper != None:
                        line_pic.add("Upper Limit",x_Upper,y_Upper,is_legend_show=False)
                    if x_Lower != None and y_Lower != None:
                        line_pic.add("Lower Limit",x_Lower,y_Lower,is_legend_show=False)

                x=[i[3*index+2+compare*division] for i in data.values]
                while 'NaN' in x:
                    x.remove('NaN')
                y=[i[3*index+3+compare*division] for i in data.values]
                while 'NaN' in y:
                    y.remove('NaN')
                if int(float(x[0])) > int(float(x[1])):
                    x.reverse()
                    y.reverse()
                sn_info=[i[compare*division] for i in data.values][0]
                #print sn_info,x,y
                #line_pic=Line(title,subtitle)
                line_pic.add(sn_info,x,y,is_smooth=True,is_legend_show=False,is_more_utils=True)
            page.add(line_pic)
    page.render('log.html')
    print u"Log图完成绘制，并生成log.html文件，请用浏览器打开"
    print u"Tips:每幅图都可以查看每条曲线的SN并进行图片下载"

start_time=int(time.time())
#检查所需文件目录是否存在，如果不存在则创建
print u"检查文件目录是否存在"
if os.path.exists("./log"):
    print u"存放log文件的目录[./log]存在，OK"
else:
    print u"存放log的目录不存在,正在创建./log文件夹"
    os.mkdir("./log")
    print u"创建成功并即将退出程序，请存放需要绘制的log至该文件夹然后再运行此程序"
    os._exit()
if os.path.exists("./error"):
    print u"存放Erro文件的目录[./error]存在，OK"
    for error_file in os.listdir("./error"):
        os.remove("./error/"+error_file)
else:
    print u"存放Erro文件的目录不存在,正在创建./error文件夹"
    os.mkdir("./error")
all_logs_path="./log/"
print u"开始整合Log"
if blend_files(all_logs_path):
    print u"整合Log完成，开始绘图"
    station=os.listdir(all_logs_path)[0].split('_')[0]
    print u"所画站点为%s" % station
    OK_Limit=False
    try:
        if station+".txt" in os.listdir("./limit"):
            OK_Limit=True
            print u"在limit文件夹中找到该站Limit并将绘制于图形中"
        else:
            print u"在limit文件夹中没有找到该站的Limit故图形中将不绘制limit"
    except Exception as e:
        print e,u"没有找到limit文件夹故图形中将不绘制limit"
    if os.path.isfile("logs.txt"):
        get_pic_html()
    else:
        print u"没有找到生成的logs.txt文件,请重新运行本程序"
else:
    print u"程序即将退出"
end_time=int(time.time())
print "======"*6
print u"------------耗时%sS---------------"%(end_time-start_time)
print "============T-H-E , E-N-D==========="


