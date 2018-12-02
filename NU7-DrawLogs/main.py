# -*- coding:utf-8 -*-

"""
# dev: python2/3
# @Bean.Wei
#
# Read the Logs, make the json data files. Then open the html in browser!
"""

import os
import shutil
import re
import threading
import random

from utils.colors import colors
from utils.limit import limit

import logging
logging.basicConfig(level = logging.INFO, format = "[%(asctime)s]%(levelname)s : %(message)s")
logger = logging.getLogger(__name__)

# define the json file template
jsonTemp = '{"name": "%s","type":"line","smooth":1,"symbol":"none","itemStyle":{"normal":{"color":"%s"}},"data":[%s]}'

# choose wether need to add the Limit in the lines
AddLimit = True
# define the limit line Color
LimitColor = "#000000"

# logs dir: save the logs
Logs_Dir = "./Logs"
# make json dir: ending create the json data file
MakeJson_Dir = "./jsonData"
# target html: open the main html in browser
Target_Html = "NU7.html"

# logs item is the logs txt name.
LOGS_ITEM = [
    "Left_Mic_FR_Smoothing",
    "Left_Mic_Fundamental",
    "Left_Mic_Seal_Delta",
    "Left_Mic_Seal_FR_Smoothing",
    "Left_Mic_THD",
    "Middle_Mic_FR_Smoothing",
    "Middle_Mic_Fundamental",
    "Middle_Mic_Seal_Delta",
    "Middle_Mic_Seal_FR_Smoothing",
    "Middle_Mic_THD",
    "Right_Mic_FR_Smoothing",
    "Right_Mic_Fundamental",
    "Right_Mic_Seal_Delta",
    "Right_Mic_Seal_FR_Smoothing",
    "Right_Mic_THD",
    "Spk_FR_Smoothing",
    "Spk_Fundamental",
    "Spk_Rub&Buzz",
    "Spk_THD",
    "Ultrasound_Level_Adjusted",
    "Ultrasound_SN_Calculated",
    "Ultrasound_Spectrum_Noise_Power_Sum"
]

# some items test values is from max to min, we need reverse it, so we must to define which item need it
NeedReverseItems = [
    "Left_Mic_FR_Smoothing",
    "Left_Mic_Fundamental",
    "Left_Mic_Seal_FR_Smoothing",
    "Middle_Mic_FR_Smoothing",
    "Middle_Mic_Fundamental",
    "Middle_Mic_Seal_FR_Smoothing",
    "Right_Mic_FR_Smoothing",
    "Right_Mic_Fundamental",
    "Right_Mic_Seal_FR_Smoothing",
    "Spk_FR_Smoothing",
    "Spk_Fundamental",
]

def main():
    init()
    logger.info("Start Read the Logs")
    logs = os.listdir(Logs_Dir)
    if not logs:
        logger.info("NOT FOUND THE LOGS, WILL EXIST")
        os._exit(0)
    logSet = setLogs(logs)  
    # TODO: use the threading
    for k, v in logSet.items():
        makeJsonFiles(k, v)

def init():
    """check all the Dirs
    let we can continue anyway.
    """

    if os.path.exists(Logs_Dir):
        logger.info("check the Logs Dir whether exist: YES ")
    else:
        logger.info("check the Logs Dir whether exist: NO ")  
        logger.info("No logs Dir! Will exit")  
        os._exit(0)    
    if os.path.exists(MakeJson_Dir):
        shutil.rmtree(MakeJson_Dir)
    os.makedirs(MakeJson_Dir)
    if not os.path.exists(Target_Html):    
        # TODO: Make a html if no exist
        pass
    logger.info("Init OK!")    

def setLogs(logsnamelist):
    """
    get the logs file set. 
    eg: {"Left_Mic_THD": ["Left_Mic_THD_2018_11_07.txt", Left_Mic_THD_2018_11_05.txt]}

    args:
        the logs name list
    return:
        the dict set    
    """
    logs = ",".join(logsnamelist)
    logsDic = dict()
    for item in LOGS_ITEM:
        val = re.findall(r'%s.*?.txt' % item, logs)
        if val:
            logsDic[item] = val 
    if not logsDic:
        logger.info("Not Found the test Logs in the Logs folder, Will exit!")
        os._exit(0)
    return logsDic    

def readSingleLog(file_path):
    """raed the log, get the test value
    args:
        file_path: the log path
    return:
        a dict, {sn_title: test_value}    
    """    
    # TODO: need to check the test values length?
    with open(file_path) as fp:
        f = fp.readlines()
        if len(f) < 3:
            return None
        # remove the fist line=> yaxis infos, and the second line=> xaxis infos
        f = f[2:]
        logInfoDic = dict()
        for line in f:
            cut = line.strip(",").split(",,")
            if len(cut) == 2:
                sn_title, values = cut
                logInfoDic[sn_title] = values    
            else:
                print("this line can't match", line)   
        return logInfoDic    


def makeJsonFiles(output_filename, input_logsname_list):
    """
    read the logs, create the json files.
    args:
        output_filename: the json file name
        input_logsname: the list of same item logs
    return:    
    """
    jsonContainStr = "["
    for logname in input_logsname_list:
        logInfoDic = readSingleLog(os.path.join(Logs_Dir, logname))
        if not logInfoDic:
            continue
        for sninfo, testvalue in logInfoDic.items():
            if output_filename in NeedReverseItems:
                ts = testvalue.split(",")
                ts.reverse()
                testvalue = ",".join(ts)
            item = jsonTemp % (sninfo, random.choice(colors.values()), testvalue)
            jsonContainStr += item + ","    
    # Add the limit
    if AddLimit:
        if output_filename == "Left_Mic_FR_Smoothing":
            upper_limit_name = "Mic_L_Response_Upper_Limit"
            lower_limit_name = "Mic_L_Response_Lower_Limit"
            jsonContainStr += jsonTemp % (upper_limit_name, LimitColor, limit[upper_limit_name]) + ","
            jsonContainStr += jsonTemp % (lower_limit_name, LimitColor, limit[lower_limit_name]) + ","
        elif output_filename == "Left_Mic_THD":
            upper_limit_name = "Mic_L_THD_Upper_Limit"
            jsonContainStr += jsonTemp % (upper_limit_name, LimitColor, limit[upper_limit_name]) + ","
        elif output_filename == "Middle_Mic_FR_Smoothing":
            upper_limit_name = "Mic_M_Response_Upper_Limit"
            lower_limit_name = "Mic_M_Response_Lower_Limit"
            jsonContainStr += jsonTemp % (upper_limit_name, LimitColor, limit[upper_limit_name]) + ","
            jsonContainStr += jsonTemp % (lower_limit_name, LimitColor, limit[lower_limit_name]) + ","
        elif output_filename == "Middle_Mic_THD":
            upper_limit_name = "Mic_M_THD_Upper_Limit"
            jsonContainStr += jsonTemp % (upper_limit_name, LimitColor, limit[upper_limit_name]) + ","
        elif output_filename == "Right_Mic_FR_Smoothing":
            upper_limit_name = "Mic_R_Response_Upper_Limit"
            lower_limit_name = "Mic_R_Response_Lower_Limit"
            jsonContainStr += jsonTemp % (upper_limit_name, LimitColor, limit[upper_limit_name]) + ","
            jsonContainStr += jsonTemp % (lower_limit_name, LimitColor, limit[lower_limit_name]) + ","
        elif output_filename == "Right_Mic_THD":
            upper_limit_name = "Mic_R_THD_Upper_Limit"
            jsonContainStr += jsonTemp % (upper_limit_name, LimitColor, limit[upper_limit_name]) + ","    
        elif output_filename == "Spk_FR_Smoothing":
            upper_limit_name = "Spk_Response_Upper_Limit"
            lower_limit_name = "Spk_Response_Lower_Limit"
            jsonContainStr += jsonTemp % (upper_limit_name, LimitColor, limit[upper_limit_name]) + ","
            jsonContainStr += jsonTemp % (lower_limit_name, LimitColor, limit[lower_limit_name]) + ","
        elif output_filename == "Spk_THD":
            upper_limit_name = "Spk_THD_Upper_Limit"
            jsonContainStr += jsonTemp % (upper_limit_name, LimitColor, limit[upper_limit_name]) + ","
        elif output_filename == "Spk_Rub&Buzz":
            upper_limit_name = "Spk_Rub&Buzz_Upper_Limiit"
            jsonContainStr += jsonTemp % (upper_limit_name, LimitColor, limit[upper_limit_name]) + ","          

    jsonContainStr = jsonContainStr.rstrip(",") + "]"
    # TODO: Need to check this way is OK?
    opt_fn = os.path.join(MakeJson_Dir, output_filename)
    with open(opt_fn , 'w') as fp:
        fp.write(jsonContainStr)
    os.rename(opt_fn, opt_fn + ".json")


if __name__ == '__main__':
    main()
    
