import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


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
    assert np.shape(ay)[0] == np.shape(wave)[0], "Wrong dimension"
    l = np.shape(ay)[1]
    for i in range(l):
        plt.plot(wave, ay[:, i], label=i + 1)
        plt.legend()
    plt.show()


def ay_bacth(path, list, filename):
    ay_bacth = []

    for station in list:
        B1 = path + station['Before Blank'][0] + '.ASC'
        B2 = path + station['Before Blank'][1] + '.ASC'

        B3 = path + station['After Blank'][0] + '.ASC'
        B4 = path + station['After Blank'][1] + '.ASC'

        S1 = path + station['Sample'][0] + '.ASC'
        S2 = path + station['Sample'][1] + '.ASC'
        ay_bacth.append(ay_single(B1, B2, B3, B4, S1, S2))
    wave = np.arange(800, 299, -1)
    ay_bacth = np.asarray(ay_bacth)
    multiple_plot(ay_bacth.T, wave)
    f = path + filename + '.csv'
    aypd = pd.DataFrame(ay_bacth.T)
    aypd.to_csv(f)
