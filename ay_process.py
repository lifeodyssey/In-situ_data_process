from IADP import ay

path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.03.08/ay/'
# output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/'

Station1 = {'Sample': ['C0308S11', 'C0308S12'],
            'Before Blank': ['C0308_B1', 'C0308_B2'],
            'After Blank': ['C0308_R3', 'C0308_R4'], }
Station2 = {'Sample': ['C0308S21', 'C0308S21'],
            'Before Blank': ['C0308_B1', 'C0308_B2'],
            'After Blank': ['C0308_R3', 'C0308_R4'], }
Station3 = {'Sample': ['C0308S31', 'C0308S32'],
            'Before Blank': ['C0308_B1', 'C0308_B2'],
            'After Blank': ['C0308_R3', 'C0308_R4'], }
Station4 = {'Sample': ['C0308S41', 'C0308S42'],
            'Before Blank': ['C0308_B1', 'C0308_B2'],
            'After Blank': ['C0308_R3', 'C0308_R4'], }
Station5 = {'Sample': ['C0308S51', 'C0308S52'],
            'Before Blank': ['C0308_B1', 'C0308_B2'],
            'After Blank': ['C0308_R3', 'C0308_R4'], }

Station6 = {'Sample': ['C0308S61', 'C0308S62'],
            'Before Blank': ['C0308_B1', 'C0308_B2'],
            'After Blank': ['C0308_R3', 'C0308_R4'], }

Station7 = {'Sample': ['C0308S71', 'C0308S72'],
            'Before Blank': ['C0308_B1', 'C0308_B2'],
            'After Blank': ['C0308_R3', 'C0308_R4'], }

# Station8 = {'Sample': ['C0308S71', 'C0308S72'],
#             'Before Blank': ['C0308B21', 'C0308B22'],
#             'After Blank': ['C0308B31', 'C0308B32'], }
Station9 = {'Sample': ['C0308S91', 'C0308S92'],
            'Before Blank': ['C0308_B1', 'C0308_B2'],
            'After Blank': ['C0308_R3', 'C0308_R4'], }
Station10 = {'Sample': ['C0308101', 'C0308102'],
             'Before Blank': ['C0308_B1', 'C0308_B2'],
             'After Blank': ['C0308_R3', 'C0308_R4'], }

Station11 = {'Sample': ['C0308111', 'C0308112'],
             'Before Blank': ['C0308_B1', 'C0308_B2'],
             'After Blank': ['C0308_R3', 'C0308_R4'], }

S_list = [Station1,
          Station2,
          Station3,
          Station4,
          # Station5,
          Station6,
          Station7,
          # Station8,
          Station9,
          Station10,
          Station11,
          ]

ay.ay_bacth(path, S_list, '0308ay', )
