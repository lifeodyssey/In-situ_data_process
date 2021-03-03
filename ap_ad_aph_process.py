import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd
from IADP import ap_ad_aph

ap_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/ap/'
ad_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/ad/'
output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/'

AP_S1 = {'Sample': ['A0806S11', 'A0806S12'],
         'Before Blank': ['A0806_B1', 'A0806_B2'],
         'After Blank': ['A0806_B3', 'A0806_B4'],
         'Vol': 100,
         'Diameter': [22.28, 22.47, 21.42]}
AP_S2 = {'Sample': ['A0806S21', 'A0806S22'],
         'Before Blank': ['A0806_B5', 'A0806_B6'],
         'After Blank': ['A0806_B7', 'A0806_B8'],
         'Vol': 100,
         'Diameter': [21.97, 22.14, 22.22]}
AP_S3 = {'Sample': ['A0806S31', 'A0806S32'],
         'Before Blank': ['A0806_B7', 'A0806_B8'],
         'After Blank': ['A0806_B9', 'A0806B10'],
         'Vol': 200,
         'Diameter': [22.41, 22.44, 21.45]}

AP_S4 = {'Sample': ['A0806S41', 'A0806S42'],
         'Before Blank': ['A0806_B9', 'A0806B10'],
         'After Blank': ['A0806B11', 'A0806B12'],
         'Vol': 200,
         'Diameter': [22.39, 22.42, 21.40]}

AP_S5 = {'Sample': ['A0806S51', 'A0806S52'],
         'Before Blank': ['A0806B11', 'A0806B12'],
         'After Blank': ['A0806B13', 'A0806B14'],
         'Vol': 200,
         'Diameter': [22.48, 22.47, 21.53]}

AP_S6 = {'Sample': ['A0806S61', 'A0806S62'],
         'Before Blank': ['A0806B13', 'A0806B14'],
         'After Blank': ['A0806B15', 'A0806B16'],
         'Vol': 200,
         'Diameter': [22.42, 22.37, 21.39]}

AP_S7 = {'Sample': ['A0806S71', 'A0806S72'],
         'Before Blank': ['A0806B15', 'A0806B16'],
         'After Blank': ['A0806B17', 'A0806B18'],
         'Vol': 200,
         'Diameter': [22.36, 22.40, 21.44]}

AP_S8 = {'Sample': ['A0806S81', 'A0806S82'],
         'Before Blank': ['A0806B17', 'A0806B18'],
         'After Blank': ['A0806B19', 'A0806B20'],
         'Vol': 80,
         'Diameter': [22.35, 22.42, 21.36]}


AD_S1 = {'Sample': ['D0806-S1', 'D0806-S2'],
         'Before Blank': ['D0806-B1', 'D0806-B2'],
         'After Blank': ['D0806-B3', 'D0806-B4'], }

AD_S2 = {'Sample': ['D0806S21', 'D0806S22'],
         'Before Blank': ['D0806-B5', 'B0806-B6'],
         'After Blank': ['D0806B7', 'D0806B8'], }

AD_S3 = {'Sample': ['D0806S31', 'D0806S32'],
         'Before Blank': ['D0806B7', 'D0806B8'],
         'After Blank': ['D0806-B9', 'D0806B10'], }
AD_S4 = {'Sample': ['D0806S41', 'D0806S42'],
         'Before Blank': ['D0806B11', 'D0806B12'],
         'After Blank': ['D0806B13', 'D0806B14'], }

AD_S5 = {'Sample': ['D0806S53', 'D0806S54'],
         'Before Blank': ['D0806B15', 'D0806B16'],
         'After Blank': ['D0806B17', 'D0806B18'], }

AD_S6 = {'Sample': ['D0806S63', 'D0806S64'],
         'Before Blank': ['D0806B19', 'D0806B20'],
         'After Blank': ['D0806B21', 'D0806B22'], }

AD_S7 = {'Sample': ['D0806S71', 'D0806S72'],
         'Before Blank': ['D0806B23', 'D0806B24'],
         'After Blank': ['D0806B25', 'D0806B26'], }

AD_S8 = {'Sample': ['D0806S81', 'D0806S82'],
         'Before Blank': ['D0806B25', 'D0806B26'],
         'After Blank': ['D0806B27', 'D0806B28'], }


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

ap_bacth, area_list, vol_list = ap_ad_aph.ap_batch(ap_path=ap_path, aplist=ap_list, filename='0806ap')
ad_batch = ap_ad_aph.ad_batch(ad_path=ad_path, adlist=ad_list, filename='0806ad', area_list=area_list, vol_list=vol_list)
ap_ad_aph.aph_cal_plot(ap_batch=ap_bacth, ad_batch=ad_batch, savepath=ap_path, fname='0806aph')
