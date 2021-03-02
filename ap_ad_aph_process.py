import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd

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

