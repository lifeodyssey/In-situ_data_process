from IADP import ay

path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.02.10/ay/'
# output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/'

Station1 = {'Sample': ['C0210S11', 'C0210S12'],
            'Before Blank': ['C0210B11', 'C0210B12'],
            'After Blank': ['C0210B21', 'C0210B22'], }
Station2 = {'Sample': ['C0210S21', 'C0210S21'],
            'Before Blank': ['C0210B11', 'C0210B12'],
            'After Blank': ['C0210B21', 'C0210B22'], }
Station3 = {'Sample': ['C0210S31', 'C0210S32'],
            'Before Blank': ['C0210B11', 'C0210B12'],
            'After Blank': ['C0210B21', 'C0210B22'], }
Station4 = {'Sample': ['C0210S41', 'C0210S42'],
            'Before Blank': ['C0210B11', 'C0210B12'],
            'After Blank': ['C0210B21', 'C0210B22'], }
# Station5 = {'Sample': ['C0210S51', 'C0210S52'],
#             'Before Blank': ['C0210B11', 'C0210B12'],
#             'After Blank': ['C0210B21', 'C0210B22'], }

Station6 = {'Sample': ['C0210S61', 'C0210S62'],
            'Before Blank': ['C0210B11', 'C0210B12'],
            'After Blank': ['C0210B21', 'C0210B22'], }

Station7 = {'Sample': ['C0210S71', 'C0210S72'],
            'Before Blank': ['C0210B11', 'C0210B12'],
            'After Blank': ['C0210B21', 'C0210B22'], }

# Station8 = {'Sample': ['C0210S71', 'C0210S72'],
#             'Before Blank': ['C0210B21', 'C0210B22'],
#             'After Blank': ['C0210B31', 'C0210B32'], }
Station9 = {'Sample': ['C0210S91', 'C0210S92'],
            'Before Blank': ['C0210B11', 'C0210B12'],
            'After Blank': ['C0210B21', 'C0210B22'], }
Station10 = {'Sample': ['C210S101', 'C210S102'],
            'Before Blank': ['C0210B11', 'C0210B12'],
            'After Blank': ['C0210B21', 'C0210B22'], }

Station11 = {'Sample': ['C210S111', 'C210S111'],
            'Before Blank': ['C0210B11', 'C0210B12'],
            'After Blank': ['C0210B21', 'C0210B22'], }

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

ay.ay_bacth(path, S_list, '0210ay', )
