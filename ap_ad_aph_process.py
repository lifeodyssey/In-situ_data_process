import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd
from IADP import ap_ad_aph

ap_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.09.16/ap/'
ad_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.09.16/ad/'
output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.09.16/'

AP_S1 = {'Sample': ['A0916S11', 'A0916S12'],
         'Before Blank': ['A0916B11', 'A0916B12'],
         'After Blank': ['A0916B11', 'A0916B12'],
         'Vol': 50,
         'Diameter': [21.06, 21.45, 21.77]}


AP_S2 = {'Sample': ['A0916S21', 'A0916S22'],
         'Before Blank': ['A0916B75', 'A0916B76'],
         'After Blank': ['A0916B85', 'A0916B86'],
         'Vol': 100,
         'Diameter': [22.31, 21.98, 22.06]}


AP_S3 = {'Sample': ['A0916S31', 'A0916S32'],
         'Before Blank': ['A0916B51', 'A0916B52'],
         'After Blank': ['A0916B71', 'A0916B72'],
         'Vol': 250,
         'Diameter': [22.40, 21.98, 22.06]}

AP_S4 = {'Sample': ['A0916S41', 'A0916S42'],
         'Before Blank': ['A0916B71', 'A0916B72'],
         'After Blank': ['A0916B81', 'A0916B82'],
         'Vol': 250,
         'Diameter': [22.94, 22.81, 22.69]}


AP_S5 = {'Sample': ['A0916S51', 'A0916S52'],
         'Before Blank': ['A0916B81', 'A0916B82'],
         'After Blank': ['A0916B91', 'A0916B92'],
         'Vol': 200,
         'Diameter': [22.69, 22.71, 22.67]}

AP_S6 = {'Sample': ['A0916S61', 'A0916S62'],
         'Before Blank': ['A0916B7', 'A0916B8'],
         'After Blank': ['A0916B9', 'A0916B10'],
         'Vol': 150,
         'Diameter': [22.57, 22.70, 22.72]}

AP_S7 = {'Sample': ['A0916S71', 'A0916S71'],
         'Before Blank': ['A0916B9', 'A0916B10'],
         'After Blank': ['A0916B15', 'A0916B16'],
         'Vol': 150,
         'Diameter': [22.87, 22.69, 21.65]}

AP_S8 = {'Sample': ['A0916S81', 'A0916S83'],
         'Before Blank': ['A0916B25', 'A0916B26'],
         'After Blank': ['A0916B35', 'A0916B36'],
         'Vol': 150,
         'Diameter': [22.53, 22.27, 22.74]}


AD_S1 = {'Sample': ['D0916S11', 'D0916S12'],
         'Before Blank': ['D0916B11', 'D0916B11'],
         'After Blank': ['D0916B12', 'D0916B12'], }

AD_S2 = {'Sample': ['D0916S21', 'D0916S22'],
         'Before Blank': ['D0916B21', 'D0916B21'],
         'After Blank': ['D0916B22', 'D0916B22'], }

AD_S3 = {'Sample': ['D0916S31', 'D0916S32'],
         'Before Blank': ['D0916B31', 'D0916B31'],
         'After Blank': ['D0916B32', 'D0916B32'], }

AD_S4 = {'Sample': ['D0916S41', 'D0916S42'],
         'Before Blank': ['D0916B32', 'D0916B32'],
         'After Blank': ['D0916B41', 'D0916B41'], }

AD_S5 = {'Sample': ['D0916S51', 'D0916S52'],
         'Before Blank': ['D0916B41', 'D0916B41'],
         'After Blank': ['D0916B51', 'D0916B51'], }

AD_S6 = {'Sample': ['D0916S61', 'D0916S62'],
         'Before Blank': ['D0916B61', 'D0916B61'],
         'After Blank': ['D0916B62', 'D0916B62'], }

AD_S7 = {'Sample': ['D0916S71', 'D0916S72'],
         'Before Blank': ['D0916B71', 'D0916B71'],
         'After Blank': ['D0916B72', 'D0916B72'], }

AD_S8 = {'Sample': ['D0916S81', 'D0916S82'],
         'Before Blank': ['D0916B72', 'D0916B72'],
         'After Blank': ['D0916B82', 'D0916B82'], }


ap_list = [AP_S1,
           AP_S2,
           AP_S3,
           AP_S4,
           AP_S5,
           AP_S6,
           AP_S7,
           AP_S8, ]

ad_list = [AD_S1,
           AD_S2,
           AD_S3,
           AD_S4,
           AD_S5,
           AD_S6,
           AD_S7,
           AD_S8, ]

ap_bacth, area_list, vol_list = ap_ad_aph.ap_batch(ap_path=ap_path, aplist=ap_list, filename='0916ap')
ad_batch = ap_ad_aph.ad_batch(ad_path=ad_path, adlist=ad_list, filename='0916ad', area_list=area_list, vol_list=vol_list)
ap_ad_aph.aph_cal_plot(ap_batch=ap_bacth, ad_batch=ad_batch, savepath=ap_path, fname='0916aph')
