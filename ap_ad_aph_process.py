import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd
from IADP import ap_ad_aph

ap_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.02.10/ap/'
ad_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.02.10/ad/'
# output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.09.16/'

AP_S1 = {'Sample': ['A0210S11', 'A0210S12'],
         'Before Blank': ['A0210B11', 'A0210B12'],
         'After Blank': ['A0210B21', 'A0210B22'],
         'Vol': 50,
         'Diameter': [22.16, 22.61, 22.08]}

AP_S2 = {'Sample': ['A0210S21', 'A0210S22'],
         'Before Blank': ['A0210B11', 'A0210B12'],
         'After Blank': ['A0210B21', 'A0210B22'],
         'Vol': 50,
         'Diameter': [22.31, 22.02, 22.21]}

AP_S3 = {'Sample': ['A0210S31', 'A0210S32'],
         'Before Blank': ['A0210B11', 'A0210B12'],
         'After Blank': ['A0210B21', 'A0210B22'],
         'Vol': 75,
         'Diameter': [22.21, 22.46, 22.18]}

AP_S4 = {'Sample': ['A0210S41', 'A0210S42'],
         'Before Blank': ['A0210B11', 'A0210B12'],
         'After Blank': ['A0210B21', 'A0210B22'],
         'Vol': 100,
         'Diameter': [22.13, 22.25, 22.33]}

AP_S5 = {'Sample': ['A0210S51', 'A0210S52'],
         'Before Blank': ['A0210B11', 'A0210B12'],
         'After Blank': ['A0210B21', 'A0210B22'],
         'Vol': 150,
         'Diameter': [22.53, 22.43, 22.92]}

AP_S6 = {'Sample': ['A0210S61', 'A0210S62'],
         'Before Blank': ['A0210B51', 'A0210B52'],
         'After Blank': ['A0210B61', 'A0210B62'],
         'Vol': 50,
         'Diameter': [22.29, 22.31, 22.38]}

AP_S7 = {'Sample': ['A0210S71', 'A0210S71'],
         'Before Blank': ['A0210B51', 'A0210B52'],
         'After Blank': ['A0210B61', 'A0210B62'],
         'Vol': 100,
         'Diameter': [22.49, 22.17, 22.53]}

AP_S9 = {'Sample': ['A0210S91', 'A0210S92'],
         'Before Blank': ['A0210B51', 'A0210B52'],
         'After Blank': ['A0210B61', 'A0210B62'],
         'Vol': 30,
         'Diameter': [21.22, 21.66, 22.01]}

AP_S10 = {'Sample': ['A210101', 'A210S102'],
          'Before Blank': ['A0210B51', 'A0210B52'],
          'After Blank': ['A0210B61', 'A0210B62'],
          'Vol': 100,
          'Diameter': [21.97, 21.41, 21.86]}

AP_S11 = {'Sample': ['A210S111', 'A210S112'],
          'Before Blank': ['A0210B51', 'A0210B52'],
          'After Blank': ['A0210B61', 'A0210B62'],
          'Vol': 30,
          'Diameter': [21.69, 21.02, 21.47]}

AD_S1 = {'Sample': ['D0210S11', 'D0210S12'],
         'Before Blank': ['D0210B11', 'D0210B12'],
         'After Blank': ['D0210B21', 'D0210B22'], }

AD_S2 = {'Sample': ['D0210S21', 'D0210S22'],
         'Before Blank': ['D0210B11', 'D0210B12'],
         'After Blank': ['D0210B21', 'D0210B22'], }

AD_S3 = {'Sample': ['D0210S31', 'D0210S32'],
         'Before Blank': ['D0210B11', 'D0210B12'],
         'After Blank': ['D0210B21', 'D0210B22'], }

AD_S4 = {'Sample': ['D0210S41', 'D0210S42'],
         'Before Blank': ['D0210B31', 'D0210B32'],
         'After Blank': ['D0210B41', 'D0210B42'], }

AD_S5 = {'Sample': ['D0210S51', 'DO210S52'],
         'Before Blank': ['D0210B31', 'D0210B32'],
         'After Blank': ['D0210B41', 'D0210B42'], }

AD_S6 = {'Sample': ['D0210S61', 'D0210S62'],
         'Before Blank': ['D0210B31', 'D0210B32'],
         'After Blank': ['D0210B41', 'D0210B42'], }

AD_S7 = {'Sample': ['D0210S71', 'D0210S72'],
         'Before Blank': ['D0210B61', 'D0210B62'],
         'After Blank': ['D0210B71', 'D0210B72'], }
#
# AD_S8 = {'Sample': ['D0210S81', 'D0210S82'],
#          'Before Blank': ['D0210B72', 'D0210B72'],
#          'After Blank': ['D0210B82', 'D0210B82'], }

AD_S9 = {'Sample': ['D0210S91', 'D0210S92'],
         'Before Blank': ['D0210B61', 'D0210B62'],
         'After Blank': ['D0210B71', 'D0210B72'], }

AD_S10 = {'Sample': ['D210S101', 'D210S102'],
          'Before Blank': ['D0210B61', 'D0210B62'],
          'After Blank': ['D0210B71', 'D0210B72'], }
AD_S11 = {'Sample': ['D210S111', 'D210112'],
          'Before Blank': ['D0210B61', 'D0210B62'],
          'After Blank': ['D0210B71', 'D0210B72'], }

ap_list = [
    AP_S1,
    AP_S2,
    AP_S3,
    AP_S4,
    AP_S5,
    AP_S6,
    AP_S7,
    AP_S9,
    AP_S10,
AP_S11,
]

ad_list = [
    AD_S1,
    AD_S2,
    AD_S3,
    AD_S4,
    AD_S5,
    AD_S6,
    AD_S7,
    AD_S9,
    AD_S10,
AD_S11,
]

ap_bacth, area_list, vol_list = ap_ad_aph.ap_batch(ap_path=ap_path, aplist=ap_list, filename='0210ap')
ad_batch = ap_ad_aph.ad_batch(ad_path=ad_path, adlist=ad_list, filename='0210ad', area_list=area_list,
                              vol_list=vol_list)
ap_ad_aph.aph_cal_plot(ap_batch=ap_bacth, ad_batch=ad_batch, savepath=ap_path, fname='0210aph')
