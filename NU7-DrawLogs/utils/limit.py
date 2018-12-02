"""
define the test limit.
"""

"""
LimitItems = [
    "Left_Mic_FR_Smoothing",
    "Left_Mic_Seal_Delta",
    "Left_Mic_THD",
    "Middle_Mic_FR_Smoothing",
    "Middle_Mic_Seal_Delta",
    "Middle_Mic_THD",
    "Right_Mic_FR_Smoothing",
    "Right_Mic_Seal_Delta",
    "Right_Mic_THD",
    "Spk_FR_Smoothing",
    "Spk_Rub&Buzz",
    "Spk_THD"
]
"""

limit = {
    # sPK
    "Spk_Response_Upper_Limit": "null,null,null,null,null,null,null,null,null,null,null,null,102.2,103.9,105.4,106.8,108.1,109.4,110.5,111.5,112.2,112.9,113.4,113.7,114,114.3,114.5,114.8,115,115.4,115.8,116.2,116.5,116.7,117,117.6,118.1,118.5,118.6,118.6,118.7,119,119.2,119,118.4,117.3,115.8,115.1,115.6,116.3,116.5,116.4,116.2,116.2,118.3,121.7,124.1,125.2,125.3,128.7,127.4,125.1,121.3,116.6,115.2,115.6,115.6,116.4,117.6,118.2,117.9,116.6,114.9,112.9,111.2,111.3,111.7,111,108.6,105.1,106.3,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null",
    "Spk_Response_Lower_Limit": "null,null,null,null,null,null,null,null,null,null,null,null,90.2,91.9,93.4,94.8,96.1,97.4,98.5,99.5,100.2,100.9,101.4,101.7,102,102.3,102.5,102.8,103,103.4,103.8,104.2,104.5,104.7,105,105.6,106.1,106.5,106.6,106.6,106.7,107,107.2,107,106.4,105.3,103.8,103.1,103.6,104.3,104.5,104.4,104.2,104.2,106.3,109.7,112.1,113.2,113.3,108.7,107.4,105.1,101.3,96.6,95.2,95.6,95.6,96.4,97.6,98.2,97.9,96.6,94.9,92.9,91.2,91.3,91.7,91,88.6,85.1,86.3,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null",

    "Spk_THD_Upper_Limit": "null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,10,null,null,null,null,null,null,null,null,null,null,null,null,null,7.5,null,null,null,null,null,null,null,null,null,null,null,5,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null",

    "Spk_Rub&Buzz_Upper_Limiit": "2,null,null,null,null,null,null,null,null,null,null,null,2,null,null,null,null,null,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null",


    # Mic L
    "Mic_L_Response_Upper_Limit": "-32.9,-32.7,-32.6,-32.4,-32.3,-32.2,-32.3,-32.3,-32.4,-32.4,-32.4,-32.4,-32.4,-32.4,-32.4,-32.4,-32.3,-32.3,-32.3,-32.3,-32.3,-32.3,-32.3,-32.3,-32.3,-32.3,-32.3,-32.2,-32.2,-32.2,-32.2,-32.2,-32.2,-32.1,-32.1,-32,-32,-32,-32,-32,-32.1,-32.4,-32.7,-33.2,-33.6,-33.7,-33.1,-32.4,-31.9,-31.8,-32,-32.1,-32,-31.9,-31.9,-32,-32.1,-32.2,-32.2,-31.8,-31.1,-30.6,-30.6,-31,-31.2,-31.3,-31.3,-31.3,-31.1,-30.8,-30.4,-29.9,-29.7,-30,-30.6,-30.7,-29.9,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null",
    "Mic_L_Response_Lower_Limit": "-42.9,-42.7,-42.6,-42.4,-42.3,-42.2,-42.3,-42.3,-42.4,-42.4,-42.4,-42.4,-42.4,-42.4,-42.4,-42.4,-42.3,-42.3,-42.3,-42.3,-42.3,-42.3,-42.3,-42.3,-42.3,-42.3,-42.3,-42.2,-42.2,-42.2,-42.2,-42.2,-42.2,-42.1,-42.1,-42,-42,-42,-42,-42,-42.1,-42.4,-42.7,-43.2,-43.6,-43.7,-43.1,-42.4,-41.9,-41.8,-42,-42.1,-42,-41.9,-41.9,-42,-42.1,-42.2,-42.2,-41.8,-41.1,-40.6,-40.6,-41,-41.2,-41.3,-41.3,-41.3,-41.1,-40.8,-40.4,-39.9,-39.7,-40,-40.6,-40.7,-39.9,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null",

    "Mic_L_THD_Upper_Limit": "null,null,null,null,null,null,null,null,null,null,null,null,6,null,null,null,4,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,4,null,null,null,null,6,null,null,null,null,null,null,null,null,null,null,null,6,null,4,null,null,null,null,null,null,null,null,null,null,null,null,null,4",

    "Mic_L_Seal_Upper_Limit": "",
    "Mic_L_Seal_Lower_Limit": "",


    # Mic M
    "Mic_M_Response_Upper_Limit": "-32.8,-32.6,-32.5,-32.3,-32.1,-32,-31.9,-31.9,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-31.9,-31.9,-31.9,-31.9,-31.9,-31.9,-31.9,-31.8,-31.8,-31.7,-31.7,-31.6,-31.6,-31.6,-31.7,-31.8,-32,-32.4,-32.9,-33.4,-33.5,-33.1,-32.4,-31.9,-31.8,-31.9,-32,-32,-32,-31.9,-31.8,-31.8,-31.7,-31.7,-31.2,-30.4,-29.8,-29.6,-29.9,-30.5,-31.3,-31.8,-31.6,-31.1,-30.6,-30.4,-30,-29.6,-29.5,-29.9,-30.3,-29.9,-28.5,-27,-26,-25.7,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null",
    "Mic_M_Response_Lower_Limit": "42.8,-42.6,-42.5,-42.3,-42.1,-42,-41.9,-41.9,-42,-42,-42,-42,-42,-42,-42,-42,-42,-42,-42,-42,-42,-42,-42,-42,-42,-41.9,-41.9,-41.9,-41.9,-41.9,-41.9,-41.9,-41.8,-41.8,-41.7,-41.7,-41.6,-41.6,-41.6,-41.7,-41.8,-42,-42.4,-42.9,-43.4,-43.5,-43.1,-42.4,-41.9,-41.8,-41.9,-42,-42,-42,-41.9,-41.8,-41.8,-41.7,-41.7,-41.2,-40.4,-39.8,-39.6,-39.9,-40.5,-41.3,-41.8,-41.6,-41.1,-40.6,-40.4,-40,-39.6,-39.5,-39.9,-40.3,-39.9,-38.5,-37,-36,-35.7,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null",

    "Mic_M_THD_Upper_Limit": "null,null,null,null,null,null,null,null,null,null,null,null,6,null,null,null,4,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,4,null,null,null,null,6,null,null,null,null,null,null,null,null,null,null,null,6,null,4,null,null,null,null,null,null,null,null,null,null,null,null,null,4",

    "Mic_M_Seal_Upper_Limit": "",
    "Mic_M_Seal_Lower_Limit": "",


    # Mic R
    "Mic_R_Response_Upper_Limit": "-32.5,-32.4,-32.3,-32.1,-32,-32,-32.1,-32.3,-32.4,-32.4,-32.4,-32.4,-32.3,-32.3,-32.3,-32.3,-32.3,-32.3,-32.2,-32.2,-32.2,-32.2,-32.2,-32.2,-32.2,-32.1,-32.1,-32.1,-32.1,-32.1,-32,-32,-32,-31.9,-31.9,-31.8,-31.8,-31.8,-31.8,-31.8,-31.9,-32.2,-32.5,-33,-33.3,-33.3,-32.8,-32.1,-31.7,-31.7,-31.8,-31.8,-31.7,-31.5,-31.5,-31.7,-32,-32.1,-31.9,-31.5,-30.9,-30.5,-30.3,-30.2,-30,-30.1,-30.5,-31,-31.1,-30.7,-30.2,-29.9,-29.8,-30.3,-30.9,-30.9,-29.7,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null",
    "Mic_R_Response_Lower_Limit": "-42.5,-42.4,-42.3,-42.1,-42,-42,-42.1,-42.3,-42.4,-42.4,-42.4,-42.4,-42.3,-42.3,-42.3,-42.3,-42.3,-42.3,-42.2,-42.2,-42.2,-42.2,-42.2,-42.2,-42.2,-42.1,-42.1,-42.1,-42.1,-42.1,-42,-42,-42,-41.9,-41.9,-41.8,-41.8,-41.8,-41.8,-41.8,-41.9,-42.2,-42.5,-43,-43.3,-43.3,-42.8,-42.1,-41.7,-41.7,-41.8,-41.8,-41.7,-41.5,-41.5,-41.7,-42,-42.1,-41.9,-41.5,-40.9,-40.5,-40.3,-40.2,-40,-40.1,-40.5,-41,-41.1,-40.7,-40.2,-39.9,-39.8,-40.3,-40.9,-40.9,-39.7,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null",

    "Mic_R_THD_Upper_Limit": "null,null,null,null,null,null,null,null,null,null,null,null,6,null,null,null,4,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,4,null,null,null,null,6,null,null,null,null,null,null,null,null,null,null,null,6,null,4,null,null,null,null,null,null,null,null,null,null,null,null,null,4",

    "Mic_R_Seal_Upper_Limit": "",
    "Mic_R_Seal_Lower_Limit": "",


}