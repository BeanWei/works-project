# -*- coding:utf-8 -*-

"""
# dev: python2
# @Bean.Wei
#
# Read the Logs, make the json data files. Then open the html in browser!
"""

import os
import shutil
import re
import threading

import logging
logging.basicConfig(level = logging.INFO, format = "[%(asctime)s]%(levelname)s : %(message)s")
logger = logging.getLogger(__name__)

# define the json file template
jsonTemp = '{"name": "%s","type": "line","symbol": "circle","symbolSize": 4,"itemStyle": {"normal": {"color": "%s"}},"data": [%s]}'

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

def main():
    init()
    logger.info("Start Read the Logs")
    logs = os.listdir(Logs_Dir)
    if not logs:
        logger.info("NOT FOUND THE LOGS, WILL EXIST")
        os._exit(0)
    logSet = setLogs(logs)  
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
    # TODO: Protece the code: out off the range, check the test values length.
    with open(file_path) as fp:
        f = fp.readlines()
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
        for sninfo, testvalue in logInfoDic.items():
            # TODO: make the random color to the line
            item = jsonTemp % (sninfo, "green", testvalue)
            jsonContainStr += item + ","    
    jsonContainStr = jsonContainStr.rstrip(",") + "]"
    # TODO: Need to check this way is OK?
    opt_fn = os.path.join(MakeJson_Dir, output_filename)
    with open(opt_fn , 'w') as fp:
        fp.write(jsonContainStr)
    os.rename(opt_fn, opt_fn + ".json")


if __name__ == '__main__':
    main()
    
