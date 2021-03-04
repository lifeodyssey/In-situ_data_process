import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd
from IADP import ap_ad_aph

ap_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.01.27/ap/'
ad_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.01.27/ad/'
# output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.09.16/'

# AP_S1 = {'Sample': ['A0127S11', 'A0127S12'],
#          'Before Blank': ['A0127B11', 'A0127B12'],
#          'After Blank': ['A0127B11', 'A0127B12'],
#          'Vol': 50,
#          'Diameter': [21.06, 21.45, 21.77]}

# AP_S2 = {'Sample': ['A0127S21', 'A0127S22'],
#          'Before Blank': ['A0127B75', 'A0127B76'],
#          'After Blank': ['A0127B85', 'A0127B86'],
#          'Vol': 200,
#          'Diameter': [22.31, 21.98, 22.06]}

# AP_S3 = {'Sample': ['A0127S31', 'A0127S32'],
#          'Before Blank': ['A0127B51', 'A0127B52'],
#          'After Blank': ['A0127B71', 'A0127B72'],
#          'Vol': 200,
#          'Diameter': [22.40, 21.98, 22.06]}

AP_S4 = {'Sample': ['A0127S41', 'A0127S42'],
         'Before Blank': ['A0127B11', 'A0127B12'],
         'After Blank': ['A0127B21', 'A0127B22'],
         'Vol': 200,
         'Diameter': [21.95, 21.88, 21.64]}

AP_S5 = {'Sample': ['A0127S51', 'A0127S52'],
         'Before Blank': ['A0127B11', 'A0127B12'],
         'After Blank': ['A0127B21', 'A0127B22'],
         'Vol': 200,
         'Diameter': [22.25, 22.24, 22.33]}

AP_S6 = {'Sample': ['A0127S61', 'A0127S62'],
         'Before Blank': ['A0127B11', 'A0127B12'],
         'After Blank': ['A0127B21', 'A0127B22'],
         'Vol': 200,
         'Diameter': [21.72, 21.16, 21.19]}

AP_S7 = {'Sample': ['A0127S71', 'A0127S71'],
         'Before Blank': ['A0127B11', 'A0127B12'],
         'After Blank': ['A0127B21', 'A0127B22'],
         'Vol': 150,
         'Diameter': [21.98, 22.08, 21.77]}

AP_S9 = {'Sample': ['A0127S91', 'A0127S92'],
         'Before Blank': ['A0127B11', 'A0127B12'],
         'After Blank': ['A0127B21', 'A0127B22'],
         'Vol': 50,
         'Diameter': [22.04, 22.10, 22.33]}

AP_S10 = {'Sample': ['A127S101', 'A127S102'],
          'Before Blank': ['A0127B11', 'A0127B12'],
          'After Blank': ['A0127B21', 'A0127B22'],
          'Vol': 150,
          'Diameter': [21.57, 21.30, 21.66]}
#
# AD_S1 = {'Sample': ['D0127S11', 'D0127S12'],
#          'Before Blank': ['D0127B1', 'D0127B2'],
#          'After Blank': ['D0127B5', 'D0127B6'], }
#
# AD_S2 = {'Sample': ['D0127S21', 'D0127S22'],
#          'Before Blank': ['D0127B21', 'D0127B21'],
#          'After Blank': ['D0127B22', 'D0127B22'], }
#
# AD_S3 = {'Sample': ['D0127S31', 'D0127S32'],
#          'Before Blank': ['D0127B31', 'D0127B31'],
#          'After Blank': ['D0127B32', 'D0127B32'], }

AD_S4 = {'Sample': ['D0127S41', 'D0127S42'],
         'Before Blank': ['D0127B1', 'D0127B2'],
         'After Blank': ['D0127B3', 'D0127B4'], }

AD_S5 = {'Sample': ['D0127S51', 'D0127S52'],
         'Before Blank': ['D0127B1', 'D0127B2'],
         'After Blank': ['D0127B3', 'D0127B4'], }

AD_S6 = {'Sample': ['D0127S61', 'D0127S62'],
         'Before Blank': ['D0127B1', 'D0127B2'],
         'After Blank': ['D0127B3', 'D0127B4'], }

AD_S7 = {'Sample': ['D0127S71', 'D0127S72'],
         'Before Blank': ['D0127B1', 'D0127B2'],
         'After Blank': ['D0127B3', 'D0127B4'], }
#
# AD_S8 = {'Sample': ['D0127S81', 'D0127S82'],
#          'Before Blank': ['D0127B72', 'D0127B72'],
#          'After Blank': ['D0127B82', 'D0127B82'], }

AD_S9 = {'Sample': ['D0127S91', 'D0127S92'],
         'Before Blank': ['D0127B5', 'D0127B6'],
         'After Blank': ['D0127B7', 'D0127B8'], }

AD_S10 = {'Sample': ['D127S101', 'D127S102'],
          'Before Blank': ['D0127B5', 'D0127B6'],
          'After Blank': ['D0127B7', 'D0127B8'], }

ap_list = [
    # AP_S1,
    #        AP_S2,
    #        AP_S3,
    AP_S4,
    AP_S5,
    AP_S6,
    AP_S7,
    AP_S9,
    AP_S10,
]

ad_list = [
    # AD_S1,
    #        AD_S2,
    #        AD_S3,
    AD_S4,
    AD_S5,
    AD_S6,
    AD_S7,
    AD_S9,
    AD_S10,
]

ap_bacth, area_list, vol_list = ap_ad_aph.ap_batch(ap_path=ap_path, aplist=ap_list, filename='0127ap')
ad_batch = ap_ad_aph.ad_batch(ad_path=ad_path, adlist=ad_list, filename='0127ad', area_list=area_list,
                              vol_list=vol_list)
ap_ad_aph.aph_cal_plot(ap_batch=ap_bacth, ad_batch=ad_batch, savepath=ap_path, fname='0127aph')
