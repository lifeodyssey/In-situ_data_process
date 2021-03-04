from IADP import ay

path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.01.27/ay/'
# output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/'

Station1 = {'Sample': ['C0127S11', 'C0127S12'],
            'Before Blank': ['C0127B11', 'C0127B12'],
            'After Blank': ['C0127B21', 'C0127B22'], }
Station2 = {'Sample': ['C0127S21', 'C0127S21'],
            'Before Blank': ['C0127B11', 'C0127B12'],
            'After Blank': ['C0127B21', 'C0127B22'], }
Station3 = {'Sample': ['C0127S31', 'C0127S32'],
            'Before Blank': ['C0127B21', 'C0127B22'],
            'After Blank': ['C0127B31', 'C0127B32'], }
Station4 = {'Sample': ['C0127S41', 'C0127S42'],
            'Before Blank': ['C0127B21', 'C0127B22'],
            'After Blank': ['C0127B31', 'C0127B32'], }
Station5 = {'Sample': ['C0127S51', 'C0127S52'],
            'Before Blank': ['C0127B21', 'C0127B22'],
            'After Blank': ['C0127B31', 'C0127B32'], }

Station6 = {'Sample': ['C0127S61', 'C0127S62'],
            'Before Blank': ['C0127B21', 'C0127B22'],
            'After Blank': ['C0127B31', 'C0127B32'], }

Station7 = {'Sample': ['C0127S71', 'C0127S72'],
            'Before Blank': ['C0127B21', 'C0127B22'],
            'After Blank': ['C0127B31', 'C0127B32'], }

# Station8 = {'Sample': ['C0127S71', 'C0127S72'],
#             'Before Blank': ['C0127B21', 'C0127B22'],
#             'After Blank': ['C0127B31', 'C0127B32'], }
Station9 = {'Sample': ['C0127S91', 'C0127S92'],
            'Before Blank': ['C0127B21', 'C0127B22'],
            'After Blank': ['C0127B31', 'C0127B32'], }
Station10 = {'Sample': ['C127S101', 'C127S102'],
            'Before Blank': ['C0127B21', 'C0127B22'],
            'After Blank': ['C0127B31', 'C0127B32'], }

S_list = [Station1,
          Station2,
          Station3,
          Station4,
          Station5,
          Station6,
          Station7,
          # Station8,
          Station9,
          Station10,]

ay.ay_bacth(path, S_list, '0127ay', )
