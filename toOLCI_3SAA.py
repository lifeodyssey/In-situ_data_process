import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''read in-situ data'''
Ariake = pd.read_excel('/Users/zhenjia/Desktop/Project/SSTfusion/field/lab_insitu/full_nozero june.xlsx',
                       sheet_name='Ariake', header=0)

Rrs_Ariake = Ariake.loc[:, 'In situ Rrs_Trios':'In situ Rrs_multi-spectral bands']
Rrs_Ariake = Rrs_Ariake.drop(columns='In situ Rrs_multi-spectral bands')
Rrs_Ariake.columns = Rrs_Ariake.iloc[0]
Rrs_Ariake = Rrs_Ariake.drop(labels=0)

Ise = pd.read_excel('/Users/zhenjia/Desktop/Project/SSTfusion/field/lab_insitu/full_nozero june.xlsx',
                    sheet_name='Ise', header=0)
# get_ipython().run_line_magic('matplotlib', 'inline')

Rrs_Ise = Ise.loc[:, 'In situ Rrs_Trios':'In situ Rrs_multi-spectral bands']
Rrs_Ise = Rrs_Ise.drop(columns='In situ Rrs_multi-spectral bands')
Rrs_Ise.columns = Rrs_Ise.iloc[0]
Rrs_Ise = Rrs_Ise.drop(labels=0)

ECS = pd.read_excel('/Users/zhenjia/Desktop/Project/SSTfusion/field/lab_insitu/full_nozero june.xlsx',
                    sheet_name='ECS', header=0)

Rrs_ECS_full_pd = ECS.loc[:, 'Rrs_380':'Rrs_683']

x_ad = np.arange(750, 349, -1)
x_aph = np.arange(750, 349, -1)
x_ay = np.arange(800, 299, -1)
find = lambda k, wavelength: np.abs(wavelength - k).argmin()  # Index of closest wavelength
key = lambda k, wavelength: wavelength[find(k, wavelength)]  # Value of closest wavelength
Rrs_wave = np.arange(350, 752, 2)
OLCI_wave_vis = [400, 412, 443, 490, 510, 560, 620, 665]

Rrs_A_full = Rrs_Ariake.to_numpy()

OLCI_Rrs_Ariake = np.asarray([Rrs_A_full[:, find(400, Rrs_wave)],
                              Rrs_A_full[:, find(412, Rrs_wave)],
                              Rrs_A_full[:, find(443, Rrs_wave)],
                              Rrs_A_full[:, find(490, Rrs_wave)],
                              Rrs_A_full[:, find(510, Rrs_wave)],
                              Rrs_A_full[:, find(560, Rrs_wave)],
                              Rrs_A_full[:, find(620, Rrs_wave)],
                              Rrs_A_full[:, find(665, Rrs_wave)],
                              ])
# OLCI_Rrs_Ariake = {'380': Rrs_Ariake[380.0],
#                    '412': Rrs_Ariake[412.0],
#                    '443': (Rrs_Ariake[442.0] + Rrs_Ariake[444.0]) / 2,
#                    '490': Rrs_Ariake[490.0],
#                    '530': Rrs_Ariake[530.0],
#                    '565': (Rrs_Ariake[564.0] + Rrs_Ariake[566.0]) / 2,
#                    '672': Rrs_Ariake[672.0],
#                    }
Rrs_I_full = Rrs_Ise.to_numpy()

OLCI_Rs_Ise = np.asarray([Rrs_I_full[:, find(400, Rrs_wave)],
                          Rrs_I_full[:, find(412, Rrs_wave)],
                          Rrs_I_full[:, find(443, Rrs_wave)],
                          Rrs_I_full[:, find(490, Rrs_wave)],
                          Rrs_I_full[:, find(510, Rrs_wave)],
                          Rrs_I_full[:, find(560, Rrs_wave)],
                          Rrs_I_full[:, find(620, Rrs_wave)],
                          Rrs_I_full[:, find(665, Rrs_wave)],
                          ])

Rrs_ECS_full = Rrs_ECS_full_pd.to_numpy()
ECS_wave = np.array([380, 412, 443, 465, 490, 510, 532, 555, 565, 589, 625, 665, 683])

OLCI_Rrs_ECS = np.asarray([Rrs_ECS_full[:, find(400, ECS_wave)],
                           Rrs_ECS_full[:, find(412, ECS_wave)],
                           Rrs_ECS_full[:, find(443, ECS_wave)],
                           Rrs_ECS_full[:, find(490, ECS_wave)],
                           Rrs_ECS_full[:, find(510, ECS_wave)],
                           Rrs_ECS_full[:, find(560, ECS_wave)],
                           Rrs_ECS_full[:, find(620, ECS_wave)],
                           Rrs_ECS_full[:, find(665, ECS_wave)],
                           ])
np.savetxt("ECS_OLCI.csv", OLCI_Rrs_ECS, delimiter=",")
np.savetxt("Ise_OLCI.csv", OLCI_Rs_Ise, delimiter=",")
np.savetxt("Ariake_OLCI.csv", OLCI_Rrs_Ariake, delimiter=",")