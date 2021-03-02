import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd
from IADP import ap_ad_aph

ap_path='/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/ap/'
ad_path='/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/ad/'


AP_S1={'Sample':['A0806S11','A0806S12'],
            'Before Blank':['A0806_B1','A0806_B2'],
            'After Blank':['A0806_B3','A0806_B5'],
         'Vol':200,
         'Diameter':[22.41,22.44,21.45]}
AP_S2={'Sample':['A0806S11','A0806S12'],
            'Before Blank':['A0806_B1','A0806_B2'],
            'After Blank':['A0806_B3','A0806_B5'],
         'Vol':200,
         'Diameter':[22.41,22.44,21.45]}
AP_S3={'Sample':['A0806S11','A0806S12'],
            'Before Blank':['A0806_B1','A0806_B2'],
            'After Blank':['A0806_B3','A0806_B5'],
         'Vol':200,
         'Diameter':[22.41,22.44,21.45]}
AP_S4={'Sample':['A0806S11','A0806S12'],
            'Before Blank':['A0806_B1','A0806_B2'],
            'After Blank':['A0806_B3','A0806_B5'],
         'Vol':200,
         'Diameter':[22.41,22.44,21.45]}
AP_S5={'Sample':['A0806S11','A0806S12'],
            'Before Blank':['A0806_B1','A0806_B2'],
            'After Blank':['A0806_B3','A0806_B5'],
         'Vol':200,
         'Diameter':[22.41,22.44,21.45]}
AP_S6={'Sample':['A0806S11','A0806S12'],
            'Before Blank':['A0806_B1','A0806_B2'],
            'After Blank':['A0806_B3','A0806_B5'],
         'Vol':200,
         'Diameter':[22.41,22.44,21.45]}
AP_S7={'Sample':['A0806S11','A0806S12'],
            'Before Blank':['A0806_B1','A0806_B2'],
            'After Blank':['A0806_B3','A0806_B5'],
         'Vol':200,
         'Diameter':[22.41,22.44,21.45]}
AP_S8={'Sample':['A0806S11','A0806S12'],
            'Before Blank':['A0806_B1','A0806_B2'],
            'After Blank':['A0806_B3','A0806_B5'],
         'Vol':200,
         'Diameter':[22.41,22.44,21.45]}

AD_S1={'Sample':['D0806-S1','D0806-S2'],
            'Before Blank':['D0806-B1','D0806-B2'],
            'After Blank':['D0806-B3','D0806-B4'],}
AD_S2={'Sample':['D0806-S1','D0806-S2'],
            'Before Blank':['D0806-B1','D0806-B2'],
            'After Blank':['D0806-B3','D0806-B4'],}
AD_S3={'Sample':['D0806-S1','D0806-S2'],
            'Before Blank':['D0806-B1','D0806-B2'],
            'After Blank':['D0806-B3','D0806-B4'],}
AD_S4={'Sample':['D0806-S1','D0806-S2'],
            'Before Blank':['D0806-B1','D0806-B2'],
            'After Blank':['D0806-B3','D0806-B4'],}
AD_S5={'Sample':['D0806-S1','D0806-S2'],
            'Before Blank':['D0806-B1','D0806-B2'],
            'After Blank':['D0806-B3','D0806-B4'],}
AD_S6={'Sample':['D0806-S1','D0806-S2'],
            'Before Blank':['D0806-B1','D0806-B2'],
            'After Blank':['D0806-B3','D0806-B4'],}
AD_S7={'Sample':['D0806-S1','D0806-S2'],
            'Before Blank':['D0806-B1','D0806-B2'],
            'After Blank':['D0806-B3','D0806-B4'],}
AD_S8={'Sample':['D0806-S1','D0806-S2'],
            'Before Blank':['D0806-B1','D0806-B2'],
            'After Blank':['D0806-B3','D0806-B4'],}


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

ap_bacth,area_list,vol_list=ap_ad_aph.ap_batch(ap_path=ap_path,aplist=ap_list,filename='test')
ad_batch=ap_ad_aph.ad_batch(ad_path=ad_path,adlist=ad_list,filename='test',area_list=area_list,vol_list=vol_list)
ap_ad_aph.aph_cal_plot(ap_batch=ap_bacth,ad_batch=ad_batch,savepath=ap_path,fname='aphtest')