import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd

path = '/Users/zhenjia/Desktop/Airka_Reprocess/Ariake/2015/2015.08.06/ay/'
Station1 = {'Sample': ['C0806-S1.ASC', 'C0806-S2.ASC'],
            'Before Blank': ['C0806-B3', 'C0806-B4'],
            'After Blank': ['C0806-B5', 'C0806-B6'], }
Station2 = {'Sample': ['C0806-S3.ASC', 'C0806-S4.ASC'],
            'Before Blank': ['C0806-B3', 'C0806-B4'],
            'After Blank': ['C0806-B5', 'C0806-B6'], }
Station3 = {'Sample': ['C0806-S5.ASC', 'C0806-S6.ASC'],
            'Before Blank': ['C0806-B3', 'C0806-B4'],
            'After Blank': ['C0806-B5', 'C0806-B6'], }
Station4 = {'Sample': ['C0806-S7.ASC', 'C0806-S8.ASC'],
            'Before Blank': ['C0806-B3', 'C0806-B4'],
            'After Blank': ['C0806-B5', 'C0806-B6'], }
Station5 = {'Sample': ['C0806-S9.ASC', 'C0806-S10.ASC'],
            'Before Blank': ['C0806-B3', 'C0806-B4'],
            'After Blank': ['C0806-B5', 'C0806-B6'], }
Station6 = {'Sample': ['C0806-S11.ASC', 'C0806-S12.ASC'],
            'Before Blank': ['C0806-B3', 'C0806-B4'],
            'After Blank': ['C0806-B5', 'C0806-B6'], }
Station7 = {'Sample': ['C0806-S13.ASC', 'C0806-S14.ASC'],
            'Before Blank': ['C0806-B3', 'C0806-B4'],
            'After Blank': ['C0806-B5', 'C0806-B6'], }
Station8 = {'Sample': ['C0806-S15.ASC', 'C0806-S16.ASC'],
            'Before Blank': ['C0806-B3', 'C0806-B4'],
            'After Blank': ['C0806-B5', 'C0806-B6'], }

S_list = [Station1,
          Station2,
          Station3,
          Station4,
          Station5,
          Station6,
          Station7,
          Station8, ]


def ay_bacth(list, filename):
    ay_bacth = []

    for station in list:
        B1 = path + station['Before Blank'][0]
        B2 = path + station['Before Blank'][1]

        B3 = path + station['After Blank'][0]
        B4 = path + station['After Blank'][1]

        S1 = path + station['Sample'][0]
        S2 = path + station['Sample'][1]

        ay_bacth.append(ay_single(B1,B2,B3,B4,S1,S2))
    wave=np.arange(800,299,-1)
    multiple_plot(ay_bacth,wave)

def ay_single(B1, B2, B3, B4, S1, S2):
    b1 = pd.read_csv(B1, names=['wave', 'Blank'])
    b2 = pd.read_csv(B2, names=['wave', 'Blank'])
    b3 = pd.read_csv(B3, names=['wave', 'Blank'])
    b4 = pd.read_csv(B4, names=['wave', 'Blank'])
    Blank1 = b1['Blank'].to_numpy()
    Blank2 = b2['Blank'].to_numpy()
    Blank3 = b3['Blank'].to_numpy()
    Blank4 = b4['Blank'].to_numpy()
    s1 = pd.read_csv(S1,
                     names=['wave', 'data'])
    Sample1 = s1['data'].to_numpy()
    s2 = pd.read_csv(S2,
                     names=['wave', 'data'])
    Sample2 = s2['data'].to_numpy()
    b_tot = np.asarray([Blank1, Blank2, Blank3, Blank4])
    Mean_blank = np.mean(b_tot, axis=0)
    S1b = Sample1 - Mean_blank
    S2b = Sample2 - Mean_blank
    ay1 = (2.303 / 0.1) * (S1b - S1b[50])
    ay2 = (2.303 / 0.1) * (S2b - S2b[50])
    ay = np.mean([ay1, ay2], axis=0)
    return ay


def multiple_plot(ay, wave):
    assert np.shape(ay)[0] == np.shape(wave), "Wrong dimension"
    l = np.shape(ay)[1]
    for i in range(l):
        plt.plot(wave, ay[:, i], lable=id)
        plt.legend()
    plt.show()
