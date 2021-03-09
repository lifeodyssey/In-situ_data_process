from IADP import ay

path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2016/2016.08.24/IOP-20160824/ay/'
# output_path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/'

Station1 = {'Sample': ['CISZK11', 'CISZK12'],
            'Before Blank': ['R0826_1', 'R0826_2'],
            'After Blank': ['R0826_3', 'R0826_4'], }
Station2 = {'Sample': ['CISZK21', 'CISZK21'],
            'Before Blank': ['R0826_1', 'R0826_2'],
            'After Blank': ['R0826_3', 'R0826_4'], }
Station3 = {'Sample': ['CISZK31', 'CISZK32'],
            'Before Blank': ['R0826_1', 'R0826_2'],
            'After Blank': ['R0826_3', 'R0826_4'], }
Station4 = {'Sample': ['CISZK41', 'CISZK42'],
            'Before Blank': ['R0826_1', 'R0826_2'],
            'After Blank': ['R0826_3', 'R0826_4'], }
Station5 = {'Sample': ['CISZK51', 'CISZK52'],
            'Before Blank': ['R0826_1', 'R0826_2'],
            'After Blank': ['R0826_3', 'R0826_4'], }

Station6 = {'Sample': ['CISZK121', 'CISZK122'],
            'Before Blank': ['R0826_1', 'R0826_2'],
            'After Blank': ['R0826_3', 'R0826_4'], }

Station7 = {'Sample': ['CISZK61', 'CISZK62'],
            'Before Blank': ['R0826_1', 'R0826_2'],
            'After Blank': ['R0826_3', 'R0826_4'], }

Station8 = {'Sample': ['CISZK91', 'CISZK92'],
            'Before Blank': ['R0826_1', 'R0826_2'],
            'After Blank': ['R0826_3', 'R0826_4'], }

Station9 = {'Sample': ['CISZK71', 'CISZK72'],
            'Before Blank': ['R0826_1', 'R0826_2'],
            'After Blank': ['R0826_3', 'R0826_4'], }

Station10 = {'Sample': ['CISZK81', 'CISZK82'],
             'Before Blank': ['R0826_1', 'R0826_2'],
             'After Blank': ['R0826_3', 'R0826_4'], }
#
# Station11 = {'Sample': ['CISZK111', 'CISZK112'],
#              'Before Blank': ['CISZK_B1', 'CISZK_B2'],
#              'After Blank': ['CISZK_R3', 'CISZK_R4'], }

S_list = [Station1,
          Station2,
          Station3,
          Station4,
          Station5,
          Station6,
          Station7,
          Station8,
          Station9,
          Station10,
          ]

ay.ay_bacth(path, S_list, 'ISZKay', )
