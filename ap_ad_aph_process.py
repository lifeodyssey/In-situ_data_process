import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd
from IADP import ap_ad_aph

ap_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.03.08/ap/'
ad_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.03.08/ad/'
# output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.09.16/'

AP_S1 = {'Sample': ['C0308S11', 'C0308S12'],
         'Before Blank': ['B0308_B1', 'A0308_B2'],
         'After Blank': ['C0308B3', 'C0308B4'],
         'Vol': 150.20,
         'Diameter': [22.07, 22.22, 22.37]}

AP_S2 = {'Sample': ['C0308S21', 'C0308S22'],
         'Before Blank': ['C0308B3', 'C0308B4'],
         'After Blank': ['C0308B5', 'C0308B6'],
         'Vol': 150.50,
         'Diameter': [22.63, 22.41, 22.56]}

AP_S3 = {'Sample': ['C0308S31', 'C0308S32'],
         'Before Blank': ['C0308B7', 'C0308B8'],
         'After Blank': ['C0308B9', 'C308B10'],
         'Vol': 150.30,
         'Diameter': [22.54, 22.09, 22.22]}

AP_S4 = {'Sample': ['C0308S41', 'C0308S42'],
         'Before Blank': ['C0308B7', 'C0308B8'],
         'After Blank': ['C0308B9', 'C308B10'],
         'Vol': 150,
         'Diameter': [22.31, 22.50, 22.57]}

AP_S5 = {'Sample': ['C0308S52', 'C0308S52'],
         'Before Blank': ['C0308B7', 'C0308B8'],
         'After Blank': ['C0308B9', 'C308B10'],
         'Vol': 150,
         'Diameter': [22.38, 22.36, 22.73]}

AP_S6 = {'Sample': ['C0308S61', 'C0308S62'],
         'Before Blank': ['C0308B9', 'C308B10'],
         'After Blank': ['C308B11', 'C308B12'],
         'Vol': 100,
         'Diameter': [22.71, 22.67, 22.38]}

AP_S7 = {'Sample': ['C308S71', 'C0308S72'],
         'Before Blank': ['C308B21', 'C308B22'],
         'After Blank': ['C308B31', 'C308B32'],
         'Vol': 200,
         'Diameter': [21.98, 22.08, 22.39]}

AP_S9 = {'Sample': ['C0308S91', 'C0308S92'],
         'Before Blank': ['C308B21', 'C308B22'],
         'After Blank': ['C308B31', 'C308B32'],
         'Vol': 100,
         'Diameter': [22.42, 22.22, 22.18]}

AP_S10 = {'Sample': ['C308S101', 'C308S102'],
          'Before Blank': ['C308B21', 'C308B22'],
          'After Blank': ['C308B31', 'C308B32'],
          'Vol': 150,
          'Diameter': [22.17, 22.30, 22.24]}

AP_S11 = {'Sample': ['C308S111', 'C308S112'],
          'Before Blank': ['C308B21', 'C308B22'],
          'After Blank': ['C308B31', 'C308B32'],
          'Vol': 100,
          'Diameter': [22.35, 22.29, 22.04]}

AD_S1 = {'Sample': ['D0308S11', 'D0308S12'],
         'Before Blank': ['D0308B11', 'D0308B12'],
         'After Blank': ['D0308B21', 'D0308B22'], }

AD_S2 = {'Sample': ['D0308S21', 'D0308S22'],
         'Before Blank': ['D0308B11', 'D0308B12'],
         'After Blank': ['D0308B21', 'D0308B22'], }

AD_S3 = {'Sample': ['D0308S31', 'D0308S32'],
         'Before Blank': ['D0308B11', 'D0308B12'],
         'After Blank': ['D0308B21', 'D0308B22'], }

AD_S4 = {'Sample': ['D0308S41', 'D0308S42'],
         'Before Blank': ['D0308B21', 'D0308B22'],
         'After Blank': ['D0308B31', 'D0308B32'], }

AD_S5 = {'Sample': ['D0308S51', 'D0308S52'],
         'Before Blank': ['D0308B31', 'D0308B32'],
         'After Blank': ['D0308B51', 'D0308B52'], }

AD_S6 = {'Sample': ['D0308S61', 'D0308S62'],
         'Before Blank': ['D0308B31', 'D0308B32'],
         'After Blank': ['D0308B51', 'D0308B52'], }

AD_S7 = {'Sample': ['D0308S71', 'D0308S72'],
         'Before Blank': ['D0308B31', 'D0308B32'],
         'After Blank': ['D0308B51', 'D0308B52'], }
#
# AD_S8 = {'Sample': ['D0308S81', 'D0308S82'],
#          'Before Blank': ['D0308B72', 'D0308B72'],
#          'After Blank': ['D0308B82', 'D0308B82'], }

AD_S9 = {'Sample': ['D0308S91', 'D0308S92'],
         'Before Blank': ['D0308B61', 'D0308B62'],
         'After Blank': ['D0308B71', 'D0308B72'], }

AD_S10 = {'Sample': ['D308S101', 'D308S102'],
          'Before Blank': ['D0308B61', 'D0308B62'],
          'After Blank': ['D0308B71', 'D0308B72'], }
AD_S11 = {'Sample': ['D308S111', 'D308S112'],
          'Before Blank': ['D0308B61', 'D0308B62'],
          'After Blank': ['D0308B71', 'D0308B72'], }

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

ap_bacth, area_list, vol_list = ap_ad_aph.ap_batch(ap_path=ap_path, aplist=ap_list, filename='0308ap')
ad_batch = ap_ad_aph.ad_batch(ad_path=ad_path, adlist=ad_list, filename='0308ad', area_list=area_list,
                              vol_list=vol_list)
ap_ad_aph.aph_cal_plot(ap_batch=ap_bacth, ad_batch=ad_batch, savepath=ap_path, fname='0308aph')
