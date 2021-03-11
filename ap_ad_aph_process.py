import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd
from IADP import ap_ad_aph

ap_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2019/Data&Results/IOPs/ap/'
# ad_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2017/0128/ad/'
# output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.09.16/'


AP_Isk3 = {'Sample': ['A0731', 'A0732'],
           'Before Blank': ['A07B1', 'A07B2'],
           'After Blank': ['A07B3', 'A07B4'],
           'Vol': 30,
           'Diameter': [21.73, 21.46, 21.63]}

AP_Isk4 = {'Sample': ['A0741', 'A0742'],
           'Before Blank': ['A07B1', 'A07B2'],
           'After Blank': ['A07B3', 'A07B4'],
           'Vol': 30,
           'Diameter': [21.57, 21.67, 22.04]}

AP_Isk5 = {'Sample': ['A0751', 'A0752'],
           'Before Blank': ['A07B1', 'A07B2'],
           'After Blank': ['A07B3', 'A07B4'],
           'Vol': 30,
           'Diameter': [21.22, 21.67, 21.60]}

AP_Isk15 = {'Sample': ['A07151', 'A07152'],
            'Before Blank': ['A07B1', 'A07B2'],
            'After Blank': ['A07B3', 'A07B4'],
            'Vol': 30,
            'Diameter': [20.81, 21.35, 21.52]}


AP_Isk6 = {'Sample': ['A0761', 'A0762'],
           'Before Blank': ['A07B1', 'A07B2'],
           'After Blank': ['A07B3', 'A07B4'],
           'Vol': 40,
           'Diameter': [21.62, 21.47, 21.58]}

AP_Isk7 = {'Sample': ['A0771', 'A0772'],
           'Before Blank': ['A07B1', 'A07B2'],
           'After Blank': ['A07B3', 'A07B4'],
           'Vol': 40,
           'Diameter': [21.45, 21.59, 21.31]}

AP_Isk8 = {'Sample': ['A0781', 'A0782'],
         'Before Blank': ['A07B1', 'A07B2'],
         'After Blank': ['A07B3', 'A07B4'],
         'Vol': 40,
         'Diameter': [21.52, 21.34, 21.50]}

# AP_S9 = {'Sample': ['A0791', 'A0792'],
#          'Before Blank': ['A07B1', 'A07B2'],
#          'After Blank': ['A07B3', 'A07B4'],
#          'Vol': 40,
#          'Diameter': [22.36, 22.52, 22.47]}
#
# AP_S12 = {'Sample': ['A07121', 'A07122'],
#           'Before Blank': ['A07-1', 'A07-2'],
#           'After Blank': ['A07-3', 'A07-4'],
#           'Vol': 150,
#           'Diameter': [21.96, 21.52, 21.50]}
#
# AD_S1 = {'Sample': ['A0711', 'A0712'],
#          'Before Blank': ['A07-1', 'A07-2'],
#          'After Blank': ['A07-3', 'A07-4'], }
#
# AD_S2 = {'Sample': ['A0721', 'A0722'],
#          'Before Blank': ['A07-1', 'A07-2'],
#          'After Blank': ['A07-3', 'A07-4'], }
#
# AD_S3 = {'Sample': ['A0731', 'A0732'],
#          'Before Blank': ['A07-1', 'A07-2'],
#          'After Blank': ['A07-3', 'A07-4'], }
#
# AD_S4 = {'Sample': ['A0741', 'A0742'],
#          'Before Blank': ['A07-1', 'A07-2'],
#          'After Blank': ['A07-3', 'A07-4'], }
#
# AD_S5 = {'Sample': ['A0751', 'A0752'],
#          'Before Blank': ['A07-1', 'A07-2'],
#          'After Blank': ['A07-3', 'A07-4'], }
#
# AD_S6 = {'Sample': ['A0761', 'A0762'],
#          'Before Blank': ['A07-1', 'A07-2'],
#          'After Blank': ['A07-3', 'A07-4'], }
#
# AD_S7 = {'Sample': ['A0771', 'A0772'],
#          'Before Blank': ['A07-1', 'A07-2'],
#          'After Blank': ['A07-3', 'A07-4'], }
#
# AD_S8 = {'Sample': ['A0781', 'A0782'],
#          'Before Blank': ['A07-1', 'A07-2'],
#          'After Blank': ['A07-3', 'A07-4'], }
#
# AD_S9 = {'Sample': ['A0791', 'A0792'],
#          'Before Blank': ['A07-1', 'A07-2'],
#          'After Blank': ['A07-3', 'A07-4'], }
#
# AD_S12 = {'Sample': ['A07121', 'A07122'],
#           'Before Blank': ['A07-1', 'A07-2'],
#           'After Blank': ['A07-3', 'A07-4'], }

'''
顺序

Station ISZK
 1        1
 2        2
 3        3
 4        4
 5        5
 6        12
 7        6
 8        9
 9        7
 10       8
 前面标记的StationXXX实际上是ISZK XXX
 表里的顺序是按照ISZK的上面的那个顺序（而非标号的顺序）来的
'''

ap_list = [AP_Isk3,
           AP_Isk4,
           AP_Isk5,
           AP_Isk15,
           AP_Isk6,
           AP_Isk7,
           AP_Isk8
]

# ad_list = [
#     AD_S1,
#     AD_S2,
#     AD_S3,
#     AD_S4,
#     AD_S5,
#     AD_S12,
#     AD_S6,
#     AD_S9,
#     AD_S7,
#     AD_S8,
#
# ]

ap_bacth, area_list, vol_list = ap_ad_aph.ap_batch(ap_path=ap_path, aplist=ap_list, filename='0128ap')
# ad_batch = ap_ad_aph.ad_batch(ad_path=ad_path, adlist=ad_list, filename='0128ad', area_list=area_list,
#                               vol_list=vol_list)
# ap_ad_aph.aph_cal_plot(ap_batch=ap_bacth, ad_batch=ad_batch, savepath=ap_path, fname='0128aph')
