from IADP import ay

path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.09.16/ay/'
# output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/'

Station1 = {'Sample': ['C0916S11', 'C0916S12'],
            'Before Blank': ['C0916B1', 'C0916B2'],
            'After Blank': ['C0916B3', 'C0916B4'], }
Station2 = {'Sample': ['C0916S21', 'C0916S22'],
            'Before Blank': ['C0916B1', 'C0916B2'],
            'After Blank': ['C0916B3', 'C0916B4'], }
Station3 = {'Sample': ['C0916S31', 'C0916S32'],
            'Before Blank': ['C0916B1', 'C0916B2'],
            'After Blank': ['C0916B3', 'C0916B4'], }
Station4 = {'Sample': ['C0916S41', 'C0916S42'],
            'Before Blank': ['C0916B1', 'C0916B2'],
            'After Blank': ['C0916B3', 'C0916B4'], }
Station5 = {'Sample': ['C0916S51', 'C0916S52'],
            'Before Blank': ['C0916B1', 'C0916B2'],
            'After Blank': ['C0916B3', 'C0916B4'], }

Station6 = {'Sample': ['C0916S61', 'C0916S62'],
            'Before Blank': ['C0916B1', 'C0916B2'],
            'After Blank': ['C0916B3', 'C0916B4'], }

Station7 = {'Sample': ['C0916S71', 'C0916S72'],
            'Before Blank': ['C0916B3', 'C0916B4'],
            'After Blank': ['C0916B5', 'C0916B6'], }

Station8 = {'Sample': ['C0916S81', 'C0916S82'],
            'Before Blank': ['C0916B3', 'C0916B4'],
            'After Blank': ['C0916B5', 'C0916B6'], }

S_list = [Station1,
          Station2,
          Station3,
          Station4,
          Station5,
          Station6,
          Station7,
          Station8, ]

ay.ay_bacth(path, S_list, '0916ay', )
