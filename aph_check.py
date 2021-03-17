import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''read in-situ data'''
all = pd.read_excel('/Users/zhenjia/Desktop/Project/SSTfusion/field/lab_insitu/2015-2019Ariake R3.xlsx',
                           sheet_name='Sheet1', header=0)


Rrs=all.loc[:,'In situ Rrs_Trios':'In situ ap']
Rrs_all=Rrs.drop(columns='In situ ap')
Rrs_all.columns = Rrs_all.iloc[0]
Rrs_all = Rrs_all.drop(labels=0)
#Rrs_all=Rrs_all.to_numpy()
ap=all.loc[:,'In situ ap':'In situ ad']
ap_all=ap.drop(columns='In situ ad')
ap_all.columns = ap_all.iloc[0]
ap_all = ap_all.drop(labels=0)
#ap_all=ap_all.to_numpy()
ad=all.loc[:,'In situ ad':'In situ aph']
ad_all=ad.drop(columns='In situ aph')
ad_all.columns = ad_all.iloc[0]
ad_all = ad_all.drop(labels=0)
#ad_all=ad_all.to_numpy()
aph=all.loc[:,'In situ aph':'In situ ay']
aph_all=aph.drop(columns='In situ ay')
aph_all.columns = aph_all.iloc[0]
aph_all = aph_all.drop(labels=0)
#aph_all=aph_all.to_numpy()
ay=all.loc[:,'In situ ay':,]
ay_all=ay
ay_all.columns = ay_all.iloc[0]
ay_all = ay_all.drop(labels=0)
#ay_all=ay_all.to_numpy()
Chla=all.loc[:,'Unnamed: 9']
Chla_all=Chla
Chla_all.columns = Chla_all.iloc[0]
Chla_all = Chla_all.drop(labels=0)
Chla_all=Chla_all.to_numpy()

TSM=all.loc[:,'Unnamed: 10']
TSM_all=TSM
TSM_all.columns = TSM_all.iloc[0]
TSM_all = TSM_all.drop(labels=0)
TSM_all=TSM_all.to_numpy()
StID=all.loc[:,'Unnamed: 1']

StID.columns = StID.iloc[0]
StID = StID.drop(labels=0)
StID=StID.to_list()

Date=all.loc[:,'Unnamed: 4']
Date.columns = Date.iloc[0]
Date = Date.drop(labels=0)
Date=Date.to_list()

aph_numpy = aph_all.to_numpy()
ad_numpy = ad_all.to_numpy()
ay_numpy = ay_all.to_numpy()
ap_numpy = ap_all.to_numpy()

x_ad = np.arange(750, 349, -1)
x_aph = np.arange(750, 349, -1)
x_ay = np.arange(800, 299, -1)
find = lambda k, wavelength: np.abs(wavelength - k).argmin()  # Index of closest wavelength
key = lambda k, wavelength: wavelength[find(k, wavelength)]  # Value of closest wavelength
Rrs_wave = np.arange(350, 752, 2)
hyper_Rrs = []
hyper_aph = []
hyper_ad = []
hyper_ay = []
hyper_ap = []
for wave in Rrs_wave:
    hyper_Rrs.append(Rrs_all[wave])
    hyper_aph.append(aph_numpy[:, find(wave, x_aph)])
    hyper_ad.append(ad_numpy[:, find(wave, x_ad)])
    hyper_ay.append(ay_numpy[:, find(wave, x_ay)])
    hyper_ap.append(ap_numpy[:, find(wave, x_ad)])

hyper_Rrs = np.asarray(hyper_Rrs)
hyper_aph = np.asarray(hyper_aph)
hyper_ad = np.asarray(hyper_ad)
hyper_ay = np.asarray(hyper_ay)
hyper_ap = np.asarray(hyper_ap)
l=np.shape(hyper_aph)[1]
for i in range(l):
    plt.figure(figsize=(10,8))
    plt.plot(Rrs_wave,hyper_aph[:,i],label='aph',c='g')
    plt.plot(Rrs_wave,hyper_ad[:,i],label='ad',c='C1')
    plt.plot(Rrs_wave,hyper_ap[:,i],label='ap',C='k')
    plt.xlabel('Wavelength(nm)',fontdict={'fontsize':'20'})
    plt.ylabel('$a(m^{-1})$',fontdict={'fontsize':'20'})
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(prop={'size': 20})
    # plt.show()
    # j = input("Save(1) or Not(0): ")
    # j=int(j)
    # if j:
    plt.savefig(str(Date[i])+str(StID[i])+'.png')
    print(100*i/l)