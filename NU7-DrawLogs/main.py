# -*- coding:utf-8 -*-

"""
# dev: python2
# @Bean.Wei
#
# Read the Logs, make the json data files. Then open the html in browser!
"""

import os

import logging
logging.basicConfig(level = logging.INFO, format = "[%(asctime)s]%(levelname)s : %(message)s")
logger = logging.getLogger(__name__)

# logs dir: save the logs
# make json dir: ending create the json data file
# target html: open the main html in browser
Logs_Dir = "./Logs"
MakeJson_Dir = "./jsonData"
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
    for log in logs:
        #with open  
        pass  

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
    if not os.path.exists(MakeJson_Dir):
        os.makedirs(MakeJson_Dir)
    if not os.path.exists(Target_Html):    
        # TODO: Make a html if no exist
        pass
    logger.info("Init OK!")    

def checkLogs(logsnamelist):
    logs = ",".join(logsnamelist)
    for item in LOGS_ITEM:
        pass


if __name__ == '__main__':
    main()
    
