import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd
from IADP import ap_ad_aph

ap_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.08.24/IOP-20160824/ap/'
ad_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.08.24/IOP-20160824/ad/'
# output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.09.16/'

AP_S1 = {'Sample': ['S082411', 'S082412'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'],
         'Vol': 150,
         'Diameter': [21.87, 21.52, 21.94]}

AP_S2 = {'Sample': ['S082421', 'S082422'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'],
         'Vol': 150,
         'Diameter': [21.93, 21.65, 21.66]}

AP_S3 = {'Sample': ['S082431', 'S082432'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'],
         'Vol': 150,
         'Diameter': [21.80, 21.79, 21.80]}

AP_S4 = {'Sample': ['S082441', 'S082442'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'],
         'Vol': 150,
         'Diameter': [21.24, 21.70, 21.68]}

AP_S5 = {'Sample': ['S082451', 'S082452'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'],
         'Vol': 150,
         'Diameter': [21.43, 21.30, 21.75]}

AP_S6 = {'Sample': ['S082461', 'S082462'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'],
         'Vol': 150,
         'Diameter': [21.82, 21.84, 21.40]}

AP_S7 = {'Sample': ['S082471', 'S082472'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'],
         'Vol': 150,
         'Diameter': [21.40, 21.40, 21.42]}

AP_S8 = {'Sample': ['S082481', 'S082482'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'],
         'Vol': 150,
         'Diameter': [22.05, 22.36, 22.36]}

AP_S9 = {'Sample': ['S082491', 'S082492'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'],
         'Vol': 150,
         'Diameter': [22.36, 22.52, 22.47]}

AP_S12 = {'Sample': ['S0824121', 'S0824122'],
          'Before Blank': ['B0824-1', 'B0824-2'],
          'After Blank': ['B0824-3', 'B0824-4'],
          'Vol': 150,
          'Diameter': [21.96, 21.52, 21.50]}

AD_S1 = {'Sample': ['S082411', 'S082412'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'], }

AD_S2 = {'Sample': ['S082421', 'S082422'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'], }

AD_S3 = {'Sample': ['S082431', 'S082432'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'], }

AD_S4 = {'Sample': ['S082441', 'S082442'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'], }

AD_S5 = {'Sample': ['S082451', 'S082452'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'], }

AD_S6 = {'Sample': ['S082461', 'S082462'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'], }

AD_S7 = {'Sample': ['S082471', 'S082472'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'], }

AD_S8 = {'Sample': ['S082481', 'S082482'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'], }

AD_S9 = {'Sample': ['S082491', 'S082492'],
         'Before Blank': ['B0824-1', 'B0824-2'],
         'After Blank': ['B0824-3', 'B0824-4'], }

AD_S12 = {'Sample': ['S0824121', 'S0824122'],
          'Before Blank': ['B0824-1', 'B0824-2'],
          'After Blank': ['B0824-3', 'B0824-4'], }

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

ap_list = [
    AP_S1,
    AP_S2,
    AP_S3,
    AP_S4,
    AP_S5,
    AP_S12,
    AP_S6,
    AP_S9,
    AP_S7,
    AP_S12,
    AP_S8,
]

ad_list = [
    AD_S1,
    AD_S2,
    AD_S3,
    AD_S4,
    AD_S5,
    AD_S12,
    AD_S6,
    AD_S9,
    AD_S7,
    AD_S12,
    AD_S8,

]

ap_bacth, area_list, vol_list = ap_ad_aph.ap_batch(ap_path=ap_path, aplist=ap_list, filename='0824ap')
ad_batch = ap_ad_aph.ad_batch(ad_path=ad_path, adlist=ad_list, filename='0824ad', area_list=area_list,
                              vol_list=vol_list)
ap_ad_aph.aph_cal_plot(ap_batch=ap_bacth, ad_batch=ad_batch, savepath=ap_path, fname='0824aph')
