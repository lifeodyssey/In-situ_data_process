from IADP import ay

path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/ay/'
Station1={'Sample':['C0806-S1','C0806-S2'],
            'Before Blank':['C0806-B3','C0806-B4'],
            'After Blank':['C0806-B5','C0806-B6'],}
Station2={'Sample':['C0806-S3','C0806-S4'],
            'Before Blank':['C0806-B3','C0806-B4'],
            'After Blank':['C0806-B5','C0806-B6'],}
Station3={'Sample':['C0806-S5','C0806-S6'],
            'Before Blank':['C0806-B3','C0806-B4'],
            'After Blank':['C0806-B5','C0806-B6'],}
Station4={'Sample':['C0806-S7','C0806-S8'],
            'Before Blank':['C0806-B3','C0806-B4'],
            'After Blank':['C0806-B5','C0806-B6'],}
Station5={'Sample':['C0806-S9','C0806S10'],
            'Before Blank':['C0806-B3','C0806-B4'],
            'After Blank':['C0806-B5','C0806-B6'],}
Station6={'Sample':['C0806S11','C0806S12'],
            'Before Blank':['C0806-B3','C0806-B4'],
            'After Blank':['C0806-B5','C0806-B6'],}
Station7={'Sample':['C0806S13','C0806S14'],
            'Before Blank':['C0806-B3','C0806-B4'],
            'After Blank':['C0806-B5','C0806-B6'],}
Station8={'Sample':['C0806S15','C0806S16'],
            'Before Blank':['C0806-B3','C0806-B4'],
            'After Blank':['C0806-B5','C0806-B6'],}

S_list = [Station1,
          Station2,
          Station3,
          Station4,
          Station5,
          Station6,
          Station7,
          Station8, ]

ay.ay_bacth(path,S_list,'test',)