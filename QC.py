#!/usr/bin/env python
# coding: utf-8

# # Read Data

# ## Read Ariake

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''read in-situ data'''
Ariake = pd.read_excel('/Users/zhenjia/Desktop/Project/SSTfusion/field/lab_insitu/full_nozero2.xlsx',
                       sheet_name='Ariake', header=0)

Rrs_Ariake = Ariake.loc[:, 'In situ Rrs_Trios':'In situ Rrs_multi-spectral bands']
Rrs_Ariake = Rrs_Ariake.drop(columns='In situ Rrs_multi-spectral bands')
Rrs_Ariake.columns = Rrs_Ariake.iloc[0]
Rrs_Ariake = Rrs_Ariake.drop(labels=0)
# Rrs_Ariake=Rrs_Ariake.to_numpy()
ap = Ariake.loc[:, 'In situ ap':'In situ ad']
ap_Ariake = ap.drop(columns='In situ ad')
ap_Ariake.columns = ap_Ariake.iloc[0]
ap_Ariake = ap_Ariake.drop(labels=0)
# ap_Ariake=ap_Ariake.to_numpy()
ad = Ariake.loc[:, 'In situ ad':'In situ aph']
ad_Ariake = ad.drop(columns='In situ aph')
ad_Ariake.columns = ad_Ariake.iloc[0]
ad_Ariake = ad_Ariake.drop(labels=0)
# ad_Ariake=ad_Ariake.to_numpy()
aph = Ariake.loc[:, 'In situ aph':'In situ ay']
aph_Ariake = aph.drop(columns='In situ ay')
aph_Ariake.columns = aph_Ariake.iloc[0]
aph_Ariake = aph_Ariake.drop(labels=0)
# aph_Ariake=aph_Ariake.to_numpy()
ay = Ariake.loc[:, 'In situ ay':, ]
ay_Ariake = ay
ay_Ariake.columns = ay_Ariake.iloc[0]
ay_Ariake = ay_Ariake.drop(labels=0)
# ay_Ariake=ay_Ariake.to_numpy()
Chla = Ariake.loc[:, 'Unnamed: 9']
Chla_Ariake = Chla
Chla_Ariake.columns = Chla_Ariake.iloc[0]
Chla_Ariake = Chla_Ariake.drop(labels=0)
Chla_Ariake = Chla_Ariake.to_numpy()
TSM = Ariake.loc[:, 'Unnamed: 10']
TSM_Ariake = TSM
TSM_Ariake.columns = TSM_Ariake.iloc[0]
TSM_Ariake = TSM_Ariake.drop(labels=0)
TSM_Ariake = TSM_Ariake.to_numpy()

StID = Ariake.loc[:, 'Unnamed: 1']

StID.columns = StID.iloc[0]
StID = StID.drop(labels=0)
StID_Ariake = StID.to_numpy()

Date = Ariake.loc[:, 'Unnamed: 4']
Date.columns = Date.iloc[0]
Date = Date.drop(labels=0)
Date_Ariake = Date.to_numpy()

Lat = Ariake.loc[:, 'Unnamed: 2']
Lat.columns = Lat.iloc[0]
Lat = Lat.drop(labels=0)
Lat_Ariake = Lat.to_numpy()

Lon = Ariake.loc[:, 'Unnamed: 3']
Lon.columns = Lon.iloc[0]
Lon = Lon.drop(labels=0)
Lon_Ariake = Lon.to_numpy()

# ## Read Ise

# In[2]:


Ise = pd.read_excel('/Users/zhenjia/Desktop/Project/SSTfusion/field/lab_insitu/full_nozero2.xlsx',
                    sheet_name='Ise', header=0)
# get_ipython().run_line_magic('matplotlib', 'inline')

Rrs_Ise = Ise.loc[:, 'In situ Rrs_Trios':'In situ Rrs_multi-spectral bands']
Rrs_Ise = Rrs_Ise.drop(columns='In situ Rrs_multi-spectral bands')
Rrs_Ise.columns = Rrs_Ise.iloc[0]
Rrs_Ise = Rrs_Ise.drop(labels=0)
# Rrs_Ise=Rrs_Ise.to_numpy()
ap = Ise.loc[:, 'In situ ap':'In situ ad']
ap_Ise = ap.drop(columns='In situ ad')
ap_Ise.columns = ap_Ise.iloc[0]
ap_Ise = ap_Ise.drop(labels=0)
# ap_Ise=ap_Ise.to_numpy()
ad = Ise.loc[:, 'In situ ad':'In situ aph']
ad_Ise = ad.drop(columns='In situ aph')
ad_Ise.columns = ad_Ise.iloc[0]
ad_Ise = ad_Ise.drop(labels=0)
# ad_Ise=ad_Ise.to_numpy()
aph = Ise.loc[:, 'In situ aph':'In situ ay']
aph_Ise = aph.drop(columns='In situ ay')
aph_Ise.columns = aph_Ise.iloc[0]
aph_Ise = aph_Ise.drop(labels=0)
# aph_Ise=aph_Ise.to_numpy()
ay = Ise.loc[:, 'In situ ay':, ]
ay_Ise = ay
ay_Ise.columns = ay_Ise.iloc[0]
ay_Ise = ay_Ise.drop(labels=0)
# ay_Ise=ay_Ise.to_numpy()
Chla = Ise.loc[:, 'Unnamed: 9']
Chla_Ise = Chla
Chla_Ise.columns = Chla_Ise.iloc[0]
Chla_Ise = Chla_Ise.drop(labels=0)
Chla_Ise = Chla_Ise.to_numpy()
TSM = Ise.loc[:, 'Unnamed: 10']
TSM_Ise = TSM
TSM_Ise.columns = TSM_Ise.iloc[0]
TSM_Ise = TSM_Ise.drop(labels=0)
TSM_Ise = TSM_Ise.to_numpy()

StID = Ise.loc[:, 'Unnamed: 1']

StID.columns = StID.iloc[0]
StID = StID.drop(labels=0)
StID_Ise = StID.to_numpy()

Date = Ise.loc[:, 'Unnamed: 4']
Date.columns = Date.iloc[0]
Date = Date.drop(labels=0)
Date_Ise = Date.to_numpy()

Lat = Ise.loc[:, 'Unnamed: 2']
Lat.columns = Lat.iloc[0]
Lat = Lat.drop(labels=0)
Lat_Ise = Lat.to_numpy()

Lon = Ise.loc[:, 'Unnamed: 3']
Lon.columns = Lon.iloc[0]
Lon = Lon.drop(labels=0)
Lon_Ise = Lon.to_numpy()

# ## Read ECS

# In[3]:


ECS = pd.read_excel('/Users/zhenjia/Desktop/Project/SSTfusion/field/lab_insitu/full_nozero2.xlsx',
                    sheet_name='ECS', header=0)

# In[4]:

Rrs_ECS_full_pd = ECS.loc[:, 'Rrs_380':'Rrs_683']
ap_ECS_full = ECS.loc[:, 'ap_380':'ap_683']
ad_ECS_full = ECS.loc[:, 'ad_380':'ad_683']
aph_ECS_full = ECS.loc[:, 'aph_380':'aph_683']
ay_ECS_full = ECS.loc[:, 'ay_380':'ay_683']

Rrs_ms_ECS = ECS.loc[:, 'Rrs_SGLI_380':'Rrs_SGLI_673.5']
# ap_ECS = ECS.loc[:, 'ap_SGLI_380':'ap_SGLI_673.5']
# ad_ECS = ECS.loc[:, 'ad_SGLI_380':'ad_SGLI_673.5']
# aph_ECS = ECS.loc[:, 'aph_SGLI_380':'aph_SGLI_673.5']
# ay_ECS = ECS.loc[:, 'ay_SGLI_380':'ay_SGLI_673.5']
Chla_ECS = ECS.loc[:, 'Chla_Fluor.(mg/m^3)']
TSM_ECS = ECS.loc[:, 'TSM (g m-3)']
StID_ECS = ECS.loc[:, 'StID']
Date_ECS = ECS.loc[:, 'DATE(GMT)']
Lat_ECS = ECS.loc[:, 'Lat(N)']
Lon_ECS = ECS.loc[:, 'Long(E)']

# In[5]:


# Chla_ECS.to_numpy()

# In[6]:


# np.where(Chla_ECS.to_numpy() == np.nan)

# ## Sort into numpy

# In[7]:


x_ad = np.arange(750, 349, -1)
x_aph = np.arange(750, 349, -1)
x_ay = np.arange(800, 299, -1)
find = lambda k, wavelength: np.abs(wavelength - k).argmin()  # Index of closest wavelength
key = lambda k, wavelength: wavelength[find(k, wavelength)]  # Value of closest wavelength
Rrs_wave = np.arange(350, 752, 2)
SGLI_wave_vis = [380, 412, 443, 490, 530, 565, 672]

# ### Hyperspectral

# In[8]:


aph_numpy = aph_Ariake.to_numpy()
ad_numpy = ad_Ariake.to_numpy()
ay_numpy = ay_Ariake.to_numpy()
ap_numpy = ap_Ariake.to_numpy()

Ariake_hyper_Rrs = []
Ariake_hyper_aph = []
Ariake_hyper_ad = []
Ariake_hyper_ay = []
Ariake_hyper_ap = []
for wave in Rrs_wave:
    Ariake_hyper_Rrs.append(Rrs_Ariake[wave])
    Ariake_hyper_aph.append(aph_numpy[:, find(wave, x_aph)])
    Ariake_hyper_ad.append(ad_numpy[:, find(wave, x_ad)])
    Ariake_hyper_ay.append(ay_numpy[:, find(wave, x_ay)])
    Ariake_hyper_ap.append(ap_numpy[:, find(wave, x_ad)])

Ariake_hyper_Rrs = np.asarray(Ariake_hyper_Rrs)
Ariake_hyper_aph = np.asarray(Ariake_hyper_aph)
Ariake_hyper_ad = np.asarray(Ariake_hyper_ad)
Ariake_hyper_ay = np.asarray(Ariake_hyper_ay)
Ariake_hyper_ap = np.asarray(Ariake_hyper_ap)


# In[9]:


aph_numpy = aph_Ise.to_numpy()
ad_numpy = ad_Ise.to_numpy()
ay_numpy = ay_Ise.to_numpy()
ap_numpy = ap_Ise.to_numpy()

Ise_hyper_Rrs = []
Ise_hyper_aph = []
Ise_hyper_ad = []
Ise_hyper_ay = []
Ise_hyper_ap = []
for wave in Rrs_wave:
    Ise_hyper_Rrs.append(Rrs_Ise[wave])
    Ise_hyper_aph.append(aph_numpy[:, find(wave, x_aph)])
    Ise_hyper_ad.append(ad_numpy[:, find(wave, x_ad)])
    Ise_hyper_ay.append(ay_numpy[:, find(wave, x_ay)])
    Ise_hyper_ap.append(ap_numpy[:, find(wave, x_ad)])

Ise_hyper_Rrs = np.asarray(Ise_hyper_Rrs)
Ise_hyper_aph = np.asarray(Ise_hyper_aph)
Ise_hyper_ad = np.asarray(Ise_hyper_ad)
Ise_hyper_ay = np.asarray(Ise_hyper_ay)
Ise_hyper_ap = np.asarray(Ise_hyper_ap)

# ### multispectral

# In[10]:


SGLI_Rrs_Ariake = {'380': Rrs_Ariake[380.0],
                   '412': Rrs_Ariake[412.0],
                   '443': (Rrs_Ariake[442.0] + Rrs_Ariake[444.0]) / 2,
                   '490': Rrs_Ariake[490.0],
                   '530': Rrs_Ariake[530.0],
                   '565': (Rrs_Ariake[564.0] + Rrs_Ariake[566.0]) / 2,
                   '672': Rrs_Ariake[672.0],
                   }
SGLI_Rrs_Ariake = pd.DataFrame(SGLI_Rrs_Ariake)
SGLI_Rrs_Ariake = SGLI_Rrs_Ariake.to_numpy()
aph_measu_SGLI_Ariake = np.asarray([Ariake_hyper_aph[find(380, Rrs_wave), :],
                                    Ariake_hyper_aph[find(412, Rrs_wave), :],
                                    Ariake_hyper_aph[find(443, Rrs_wave), :],
                                    Ariake_hyper_aph[find(490, Rrs_wave), :],
                                    Ariake_hyper_aph[find(530, Rrs_wave), :],
                                    Ariake_hyper_aph[find(565, Rrs_wave), :],
                                    Ariake_hyper_aph[find(672, Rrs_wave), :],
                                    ])

ad_measu_SGLI_Ariake = np.asarray([Ariake_hyper_ad[find(380, Rrs_wave), :],
                                   Ariake_hyper_ad[find(412, Rrs_wave), :],
                                   Ariake_hyper_ad[find(443, Rrs_wave), :],
                                   Ariake_hyper_ad[find(490, Rrs_wave), :],
                                   Ariake_hyper_ad[find(530, Rrs_wave), :],
                                   Ariake_hyper_ad[find(565, Rrs_wave), :],
                                   Ariake_hyper_ad[find(672, Rrs_wave), :],
                                   ])

ay_measu_SGLI_Ariake = np.asarray([Ariake_hyper_ay[find(380, Rrs_wave), :],
                                   Ariake_hyper_ay[find(412, Rrs_wave), :],
                                   Ariake_hyper_ay[find(443, Rrs_wave), :],
                                   Ariake_hyper_ay[find(490, Rrs_wave), :],
                                   Ariake_hyper_ay[find(530, Rrs_wave), :],
                                   Ariake_hyper_ay[find(565, Rrs_wave), :],
                                   Ariake_hyper_ay[find(672, Rrs_wave), :],
                                   ])

ap_measu_SGLI_Ariake = np.asarray([Ariake_hyper_ap[find(380, Rrs_wave), :],
                                   Ariake_hyper_ap[find(412, Rrs_wave), :],
                                   Ariake_hyper_ap[find(443, Rrs_wave), :],
                                   Ariake_hyper_ap[find(490, Rrs_wave), :],
                                   Ariake_hyper_ap[find(530, Rrs_wave), :],
                                   Ariake_hyper_ap[find(565, Rrs_wave), :],
                                   Ariake_hyper_ap[find(672, Rrs_wave), :],
                                   ])

# In[11]:


SGLI_Rrs_Ise = {'380': Rrs_Ise[380.0],
                '412': Rrs_Ise[412.0],
                '443': (Rrs_Ise[442.0] + Rrs_Ise[444.0]) / 2,
                '490': Rrs_Ise[490.0],
                '530': Rrs_Ise[530.0],
                '565': (Rrs_Ise[564.0] + Rrs_Ise[566.0]) / 2,
                '672': Rrs_Ise[672.0],
                }
SGLI_Rrs_Ise = pd.DataFrame(SGLI_Rrs_Ise)
SGLI_Rrs_Ise = SGLI_Rrs_Ise.to_numpy()
aph_measu_SGLI_Ise = np.asarray([Ise_hyper_aph[find(380, Rrs_wave), :],
                                 Ise_hyper_aph[find(412, Rrs_wave), :],
                                 Ise_hyper_aph[find(443, Rrs_wave), :],
                                 Ise_hyper_aph[find(490, Rrs_wave), :],
                                 Ise_hyper_aph[find(530, Rrs_wave), :],
                                 Ise_hyper_aph[find(565, Rrs_wave), :],
                                 Ise_hyper_aph[find(672, Rrs_wave), :],
                                 ])

ad_measu_SGLI_Ise = np.asarray([Ise_hyper_ad[find(380, Rrs_wave), :],
                                Ise_hyper_ad[find(412, Rrs_wave), :],
                                Ise_hyper_ad[find(443, Rrs_wave), :],
                                Ise_hyper_ad[find(490, Rrs_wave), :],
                                Ise_hyper_ad[find(530, Rrs_wave), :],
                                Ise_hyper_ad[find(565, Rrs_wave), :],
                                Ise_hyper_ad[find(672, Rrs_wave), :],
                                ])

ay_measu_SGLI_Ise = np.asarray([Ise_hyper_ay[find(380, Rrs_wave), :],
                                Ise_hyper_ay[find(412, Rrs_wave), :],
                                Ise_hyper_ay[find(443, Rrs_wave), :],
                                Ise_hyper_ay[find(490, Rrs_wave), :],
                                Ise_hyper_ay[find(530, Rrs_wave), :],
                                Ise_hyper_ay[find(565, Rrs_wave), :],
                                Ise_hyper_ay[find(672, Rrs_wave), :],
                                ])

ap_measu_SGLI_Ise = np.asarray([Ise_hyper_ap[find(380, Rrs_wave), :],
                                Ise_hyper_ap[find(412, Rrs_wave), :],
                                Ise_hyper_ap[find(443, Rrs_wave), :],
                                Ise_hyper_ap[find(490, Rrs_wave), :],
                                Ise_hyper_ap[find(530, Rrs_wave), :],
                                Ise_hyper_ap[find(565, Rrs_wave), :],
                                Ise_hyper_ap[find(672, Rrs_wave), :],
                                ])

# In[12]:


SGLI_Rrs_Ariake_full = {'380': Rrs_Ariake[380.0],
                        '412': Rrs_Ariake[412.0],
                        '443': (Rrs_Ariake[442.0] + Rrs_Ariake[444.0]) / 2,
                        '490': Rrs_Ariake[490.0],
                        '530': Rrs_Ariake[530.0],
                        '565': (Rrs_Ariake[564.0] + Rrs_Ariake[566.0]) / 2,
                        '672': Rrs_Ariake[672.0],
                        '763': (Rrs_Ariake[762.0] + Rrs_Ariake[764.0]) / 2,
                        '869': (Rrs_Ariake[868.0] + Rrs_Ariake[870.0]) / 2
                        }
SGLI_Rrs_Ariake_full = pd.DataFrame(SGLI_Rrs_Ariake_full)
SGLI_Rrs_Ariake_full = SGLI_Rrs_Ariake_full.to_numpy()

SGLI_Rrs_Ise_full = {'380': Rrs_Ise[380.0],
                     '412': Rrs_Ise[412.0],
                     '443': (Rrs_Ise[442.0] + Rrs_Ise[444.0]) / 2,
                     '490': Rrs_Ise[490.0],
                     '530': Rrs_Ise[530.0],
                     '565': (Rrs_Ise[564.0] + Rrs_Ise[566.0]) / 2,
                     '672': Rrs_Ise[672.0],
                     '763': (Rrs_Ise[762.0] + Rrs_Ise[764.0]) / 2,
                     '869': (Rrs_Ise[868.0] + Rrs_Ise[870.0]) / 2
                     }
SGLI_Rrs_Ise_full = pd.DataFrame(SGLI_Rrs_Ise_full)
SGLI_Rrs_Ise_full = SGLI_Rrs_Ise_full.to_numpy()

# In[13]:


Rrs_ECS_full = Rrs_ECS_full_pd.to_numpy()
ap_measu_ECS_full = ap_ECS_full.to_numpy()
ad_measu_ECS_full = ad_ECS_full.to_numpy()
ay_measu_ECS_full = ay_ECS_full.to_numpy()
aph_measu_ECS_full = aph_ECS_full.to_numpy()
SGLI_wave_full = np.array([380, 412, 443, 490, 530, 565, 672])
ECS_wave = np.array([380, 412, 443, 465, 490, 510, 532, 555, 565, 589, 625, 665, 683])

Rrs_measu_SGLI_ECS = np.asarray([Rrs_ECS_full[:, find(380, ECS_wave)],
                                 Rrs_ECS_full[:, find(412, ECS_wave)],
                                 Rrs_ECS_full[:, find(443, ECS_wave)],
                                 Rrs_ECS_full[:, find(490, ECS_wave)],
                                 Rrs_ECS_full[:, find(530, ECS_wave)],
                                 Rrs_ECS_full[:, find(565, ECS_wave)],
                                 Rrs_ECS_full[:, find(672, ECS_wave)],
                                 ])

aph_measu_SGLI_ECS = np.asarray([aph_measu_ECS_full[:, find(380, ECS_wave)],
                                 aph_measu_ECS_full[:, find(412, ECS_wave)],
                                 aph_measu_ECS_full[:, find(443, ECS_wave)],
                                 aph_measu_ECS_full[:, find(490, ECS_wave)],
                                 aph_measu_ECS_full[:, find(530, ECS_wave)],
                                 aph_measu_ECS_full[:, find(565, ECS_wave)],
                                 aph_measu_ECS_full[:, find(672, ECS_wave)],
                                 ])

ad_measu_SGLI_ECS = np.asarray([ad_measu_ECS_full[:, find(380, ECS_wave)],
                                ad_measu_ECS_full[:, find(412, ECS_wave)],
                                ad_measu_ECS_full[:, find(443, ECS_wave)],
                                ad_measu_ECS_full[:, find(490, ECS_wave)],
                                ad_measu_ECS_full[:, find(530, ECS_wave)],
                                ad_measu_ECS_full[:, find(565, ECS_wave)],
                                ad_measu_ECS_full[:, find(672, ECS_wave)],
                                ])

ay_measu_SGLI_ECS = np.asarray([ay_measu_ECS_full[:, find(380, ECS_wave)],
                                ay_measu_ECS_full[:, find(412, ECS_wave)],
                                ay_measu_ECS_full[:, find(443, ECS_wave)],
                                ay_measu_ECS_full[:, find(490, ECS_wave)],
                                ay_measu_ECS_full[:, find(530, ECS_wave)],
                                ay_measu_ECS_full[:, find(565, ECS_wave)],
                                ay_measu_ECS_full[:, find(672, ECS_wave)],
                                ])

ap_measu_SGLI_ECS = np.asarray([ap_measu_ECS_full[:, find(380, ECS_wave)],
                                ap_measu_ECS_full[:, find(412, ECS_wave)],
                                ap_measu_ECS_full[:, find(443, ECS_wave)],
                                ap_measu_ECS_full[:, find(490, ECS_wave)],
                                ap_measu_ECS_full[:, find(530, ECS_wave)],
                                ap_measu_ECS_full[:, find(565, ECS_wave)],
                                ap_measu_ECS_full[:, find(672, ECS_wave)],
                                ])

# print(np.shape(SGLI_Rrs_ECS))
# # QA score

# ## Ariake

# In[14]:


# 412, 443, 488, 551 and 670
SGLI_5wave = np.array([412, 443, 488, 551, 670])
SGLI_5Rrs_Ariake = {
    '412': Rrs_Ariake[412.0],
    '443': (Rrs_Ariake[442.0] + Rrs_Ariake[444.0]) / 2,
    '490': Rrs_Ariake[490.0],

    '565': (Rrs_Ariake[564.0] + Rrs_Ariake[566.0]) / 2,
    '672': Rrs_Ariake[672.0]}
SGLI_5Rrs_Ariake = pd.DataFrame(SGLI_5Rrs_Ariake).astype(float)
SGLI_5Rrs_Ariake = SGLI_5Rrs_Ariake.to_numpy()

from L2wei_QA import QAscores_5Bands

maxCos_Ariake, cos_Ariake, clusterID_Ariake, totScore_Ariake = QAscores_5Bands(SGLI_5Rrs_Ariake, SGLI_5wave)

# In[15]:


plt.hist(totScore_Ariake)
plt.xlabel('Score', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.figure(figsize=(8, 10))

# In[16]:


plt.hist(clusterID_Ariake)
plt.xlabel('Cluster ID', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.figure(figsize=(8, 10))

# ## Ise

# In[17]:


SGLI_5Rrs_Ise = {
    '412': Rrs_Ise[412.0],
    '443': (Rrs_Ise[442.0] + Rrs_Ise[444.0]) / 2,
    '490': Rrs_Ise[490.0],

    '565': (Rrs_Ise[564.0] + Rrs_Ise[566.0]) / 2,
    '672': Rrs_Ise[672.0]}
SGLI_5Rrs_Ise = pd.DataFrame(SGLI_5Rrs_Ise).astype(float)
SGLI_5Rrs_Ise = SGLI_5Rrs_Ise.to_numpy()

from L2wei_QA import QAscores_5Bands

maxCos_Ise, cos_Ise, clusterID_Ise, totScore_Ise = QAscores_5Bands(SGLI_5Rrs_Ise, SGLI_5wave)

# In[18]:


plt.hist(totScore_Ise)
plt.xlabel('Score', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.figure(figsize=(8, 10))

# In[19]:


plt.hist(clusterID_Ise)
plt.xlabel('Cluster ID', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.figure(figsize=(8, 10))

# ## ECS

# In[20]:


# Rrs_ECS.columns

# In[21]:


SGLI_5Rrs_ECS = {
    '412': Rrs_ECS_full_pd['Rrs_412'],
    '443': Rrs_ECS_full_pd['Rrs_412'],
    '490': Rrs_ECS_full_pd['Rrs_490'],
    '565': Rrs_ECS_full_pd['Rrs_565'],
    '672': (Rrs_ECS_full_pd['Rrs_665'] + Rrs_ECS_full_pd['Rrs_683']) / 2}
SGLI_5Rrs_ECS = pd.DataFrame(SGLI_5Rrs_ECS).astype(float)
SGLI_5Rrs_ECS = SGLI_5Rrs_ECS.to_numpy()

from L2wei_QA import QAscores_5Bands

maxCos_ECS, cos_ECS, clusterID_ECS, totScore_ECS = QAscores_5Bands(SGLI_5Rrs_ECS, SGLI_5wave)
plt.hist(totScore_ECS)
plt.xlabel('Score', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.figure(figsize=(8, 10))

# In[22]:


plt.hist(clusterID_ECS)
plt.xlabel('Cluster ID', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.figure(figsize=(8, 10))

# # Properties

# ## Map

# In[23]:

id_Ariake = np.where(totScore_Ariake > 0.5)[0]
id_Ise = np.where(totScore_Ise > 0.5)[0]
id_ECS = np.where(totScore_ECS > 0.5)[0]

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

import numpy as np

# read in data to use for plotted points

plt.figure(figsize=(14, 11))
# determine range to print based on min, max lat and lon of the data
margin = 2  # buffer to add to the range
lat_min = 28
lat_max = 37
lon_min = 126
lon_max = 138

# create map using BASEMAP
m = Basemap(llcrnrlon=lon_min,
            llcrnrlat=lat_min,
            urcrnrlon=lon_max,
            urcrnrlat=lat_max,
            lat_0=(lat_max - lat_min) / 2,
            lon_0=(lon_max - lon_min) / 2,
            projection='merc',
            resolution='f',
            area_thresh=10000.,
            )

m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightgray')
m.drawrivers()
# convert lat and lon to map projection coordinates
# lons, lats = m(lon, lat)
# # plot points as red dots


parallels = np.arange(lat_min, lat_max, 2)
meridians = np.arange(lon_min, lon_max, 2)

lons_A, lats_A = m(Lon_Ariake[id_Ariake], Lat_Ariake[id_Ariake])
lons_I, lats_I = m(Lon_Ise[id_Ise], Lat_Ise[id_Ise])
lons_E, lats_E = m(Lon_ECS.to_numpy()[id_ECS], Lat_ECS.to_numpy()[id_ECS])
###The four positions are [left, right, top, bottom]
m.drawmeridians(meridians, fontsize=28, labels=[0, 0, 0, 1])
m.drawparallels(parallels, fontsize=28, labels=[1, 0, 0, 0])
m.scatter(lons_A, lats_A, marker='o', color='r', zorder=5, s=3)
m.scatter(lons_I, lats_I, marker='o', color='g', zorder=5, s=8)
m.scatter(lons_E, lats_E, marker='o', color='b', zorder=5, s=8)
plt.show()

# ## Mean,min,max,median,ratio
#
# # In[24]:
#
#
# len(Chla_ECS)
#
# # In[25]:
#
#
# np.min(Chla_ECS)
#
# # In[26]:
#
#
# np.max(Chla_ECS)
#
# # In[27]:
#
#
# np.min(aph_measu_SGLI_ECS[2, :])
#
# # In[28]:
#
#
# np.max(aph_measu_SGLI_ECS[2, :])
#
# # In[29]:
#
#
# Date_ECS

# ## Spectra Plot

# In[30]:


plt.figure(1, figsize=(16, 9))
plt.subplot(221)
plt.plot(SGLI_wave_vis, SGLI_Rrs_Ariake[id_Ariake, :].T)
plt.ylabel('$Rrs(sr^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('Rrs', fontsize=16)

plt.subplot(222)
plt.plot(SGLI_wave_vis, aph_measu_SGLI_Ariake[:, id_Ariake])
plt.ylabel('$a(m^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('$a_{ph}$', fontsize=16)

plt.subplot(223)
plt.plot(SGLI_wave_vis, ad_measu_SGLI_Ariake[:, id_Ariake])
plt.xlabel('Wavelength(nm)', fontdict={'fontsize': '16'})
plt.ylabel('$a(m^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('$a_{d}$', fontsize=16)

plt.subplot(224)
plt.plot(SGLI_wave_vis, ay_measu_SGLI_Ariake[:, id_Ariake])
plt.xlabel('Wavelength(nm)', fontdict={'fontsize': '16'})
plt.ylabel('$a(m^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('$a_{y}$', fontsize=16)

plt.suptitle('Ariake Sea', fontsize=16)
plt.show()

# In[ ]:


plt.figure(2, figsize=(16, 9))
plt.subplot(221)
plt.plot(SGLI_wave_vis, SGLI_Rrs_Ise[id_Ise, :].T)
plt.ylabel('$Rrs(sr^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('Rrs', fontsize=16)

plt.subplot(222)
plt.plot(SGLI_wave_vis, aph_measu_SGLI_Ise[:, id_Ise])
plt.ylabel('$a(m^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('$a_{ph}$', fontsize=16)

plt.subplot(223)
plt.plot(SGLI_wave_vis, ad_measu_SGLI_Ise[:, id_Ise])
plt.xlabel('Wavelength(nm)', fontdict={'fontsize': '16'})
plt.ylabel('$a(m^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('$a_{d}$', fontsize=16)

plt.subplot(224)
plt.plot(SGLI_wave_vis, ay_measu_SGLI_Ise[:, id_Ise])
plt.xlabel('Wavelength(nm)', fontdict={'fontsize': '16'})
plt.ylabel('$a(m^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('$a_{y}$', fontsize=16)

plt.suptitle('Ise-Mikawa Bay', fontsize=16)
plt.show()
# In[ ]:


plt.figure(3, figsize=(16, 9))
plt.subplot(221)
plt.plot(SGLI_wave_vis, Rrs_measu_SGLI_ECS[:, id_ECS])
plt.ylabel('$Rrs(sr^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('Rrs', fontsize=16)

plt.subplot(222)
plt.plot(SGLI_wave_vis, aph_measu_SGLI_ECS[:, id_ECS])
plt.ylabel('$a(m^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('$a_{ph}$', fontsize=16)

plt.subplot(223)
plt.plot(SGLI_wave_vis, ad_measu_SGLI_ECS[:, id_ECS])
plt.xlabel('Wavelength(nm)', fontdict={'fontsize': '16'})
plt.ylabel('$a(m^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('$a_{d}$', fontsize=16)

plt.subplot(224)
plt.plot(SGLI_wave_vis, ay_measu_SGLI_ECS[:, id_ECS])
plt.xlabel('Wavelength(nm)', fontdict={'fontsize': '16'})
plt.ylabel('$a(m^{-1})$', fontdict={'fontsize': '16'})
plt.xticks(SGLI_wave_vis, fontsize=16)
plt.yticks(fontsize=16)
plt.title('$a_{y}$', fontsize=16)

plt.suptitle('East China Sea', fontsize=16)
plt.show()
# In[ ]:


# # Save

# In[ ]:


import inspect, re


def varname(p):
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
        return m.group(1)


# In[ ]:


def save_file(path, filename, variable):
    np.save(path + filename, variable)


# In[ ]:


# import shelve

# T='Hiya'
# val=[1,2,3]

# filename=path+'QC0319.out'
# my_shelf = shelve.open(filename,'n') # 'n' for new

# for key in dir():
#     try:
#         my_shelf[key] = globals()[key]
#     except TypeError:
#         #
#         # __builtins__, my_shelf, and imported modules can not be shelved.
#         #
#         print('ERROR shelving: {0}'.format(key))
# my_shelf.close()


# In[ ]:


path = '/Users/zhenjia/Desktop/Project/SSTfusion/field/lab_insitu/April26/'
save_file(path, varname(Ariake_hyper_ad), Ariake_hyper_ad[:, id_Ariake])
save_file(path, varname(Ariake_hyper_ap), Ariake_hyper_ap[:, id_Ariake])
save_file(path, varname(Ariake_hyper_aph), Ariake_hyper_aph[:, id_Ariake])
save_file(path, varname(Ariake_hyper_ay), Ariake_hyper_ay[:, id_Ariake])
save_file(path, varname(Ariake_hyper_Rrs), Ariake_hyper_Rrs[:, id_Ariake])
save_file(path, varname(Rrs_wave), Rrs_wave)

save_file(path, varname(SGLI_Rrs_Ariake), SGLI_Rrs_Ariake[id_Ariake, :])
save_file(path, varname(ap_measu_SGLI_Ariake), ap_measu_SGLI_Ariake[:, id_Ariake])
save_file(path, varname(aph_measu_SGLI_Ariake), aph_measu_SGLI_Ariake[:, id_Ariake])
save_file(path, varname(ad_measu_SGLI_Ariake), ad_measu_SGLI_Ariake[:, id_Ariake])
save_file(path, varname(ay_measu_SGLI_Ariake), ay_measu_SGLI_Ariake[:, id_Ariake])
save_file(path, varname(SGLI_wave_vis), SGLI_wave_vis)

save_file(path, varname(Lon_Ariake), Lon_Ariake[id_Ariake])
save_file(path, varname(Lat_Ariake), Lat_Ariake[id_Ariake])

save_file(path, varname(Date_Ariake), Date_Ariake[id_Ariake])
save_file(path, varname(StID_Ariake), StID_Ariake[id_Ariake])
save_file(path, varname(Chla_Ariake), Chla_Ariake[id_Ariake])
save_file(path, varname(TSM_Ariake), TSM_Ariake[id_Ariake])

# In[ ]:


save_file(path, varname(Ise_hyper_ad), Ise_hyper_ad[:, id_Ise])
save_file(path, varname(Ise_hyper_ap), Ise_hyper_ap[:, id_Ise])
save_file(path, varname(Ise_hyper_aph), Ise_hyper_aph[:, id_Ise])
save_file(path, varname(Ise_hyper_ay), Ise_hyper_ay[:, id_Ise])
save_file(path, varname(Ise_hyper_Rrs), Ise_hyper_Rrs[:, id_Ise])

save_file(path, varname(SGLI_Rrs_Ise), SGLI_Rrs_Ise[id_Ise, :])
save_file(path, varname(ap_measu_SGLI_Ise), ap_measu_SGLI_Ise[:, id_Ise])
save_file(path, varname(aph_measu_SGLI_Ise), aph_measu_SGLI_Ise[:, id_Ise])
save_file(path, varname(ad_measu_SGLI_Ise), ad_measu_SGLI_Ise[:, id_Ise])
save_file(path, varname(ay_measu_SGLI_Ise), ay_measu_SGLI_Ise[:, id_Ise])

save_file(path, varname(Lon_Ise), Lon_Ise[id_Ise])
save_file(path, varname(Lat_Ise), Lat_Ise[id_Ise])

save_file(path, varname(Date_Ise), Date_Ise[id_Ise])
save_file(path, varname(StID_Ise), StID_Ise[id_Ise])
save_file(path, varname(Chla_Ise), Chla_Ise[id_Ise])
save_file(path, varname(TSM_Ise), TSM_Ise[id_Ise])

# In[ ]:


save_file(path, varname(SGLI_Rrs_Ise_full), SGLI_Rrs_Ise_full[id_Ise, :])
save_file(path, varname(SGLI_Rrs_Ariake_full), SGLI_Rrs_Ariake_full[id_Ariake, :])

# In[ ]:


SGLI_wave_full = [380, 412, 443, 490, 530, 565, 672]
save_file(path, varname(SGLI_wave_full), SGLI_wave_full)
save_file(path, varname(Rrs_wave), Rrs_wave)
save_file(path, varname(SGLI_wave_vis), SGLI_wave_vis)
save_file(path, varname(ECS_wave), ECS_wave)

# In[ ]:


# save_file(path,varname(ECS_hyper_ad),ECS_hyper_ad)
# save_file(path,varname(ECS_hyper_ap),ECS_hyper_ad)
# save_file(path,varname(ECS_hyper_aph),ECS_hyper_aph)
# save_file(path,varname(ECS_hyper_ay),ECS_hyper_ay)
# save_file(path,varname(ECS_hyper_Rrs),ECS_hyper_Rrs)


save_file(path, varname(Rrs_ECS_full), Rrs_ECS_full[id_ECS, :])
save_file(path, varname(ap_measu_ECS_full), ap_measu_ECS_full[id_ECS, :])
save_file(path, varname(aph_measu_ECS_full), aph_measu_ECS_full[id_ECS, :])
save_file(path, varname(ad_measu_ECS_full), ad_measu_ECS_full[id_ECS, :])
save_file(path, varname(ay_measu_ECS_full), ay_measu_ECS_full[id_ECS, :])

save_file(path, varname(Rrs_measu_SGLI_ECS), Rrs_measu_SGLI_ECS[:, id_ECS])
save_file(path, varname(ap_measu_SGLI_ECS), ap_measu_SGLI_ECS[:, id_ECS])
save_file(path, varname(aph_measu_SGLI_ECS), aph_measu_SGLI_ECS[:, id_ECS])
save_file(path, varname(ad_measu_SGLI_ECS), ad_measu_SGLI_ECS[:, id_ECS])
save_file(path, varname(ay_measu_SGLI_ECS), ay_measu_SGLI_ECS[:, id_ECS])

save_file(path, varname(Lon_ECS), Lon_ECS[id_ECS])
save_file(path, varname(Lat_ECS), Lat_ECS[id_ECS])

save_file(path, varname(Date_ECS), Date_ECS[id_ECS])
save_file(path, varname(StID_ECS), StID_ECS[id_ECS])
save_file(path, varname(Chla_ECS), Chla_ECS[id_ECS])
save_file(path, varname(TSM_ECS), TSM_ECS[id_ECS])


