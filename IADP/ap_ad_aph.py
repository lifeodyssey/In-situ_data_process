import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pandas as pd


def ASC_read(path, name):
    f = path + name + '.ASC'
    ASC = pd.read_csv(f, names=['wave', 'data'])
    data = ASC['data'].to_numpy()
    return data


def ap_ad_single(B1, B2, B3, B4, S1, S2, vol, area):
    b_tot = np.asarray([B1, B2, B3, B4])
    Mean_blank = np.mean(b_tot, axis=0)
    ap_tot = np.asarray([S1, S2])
    OD_pmean = np.mean(ap_tot, axis=0)
    OD_p = OD_pmean - Mean_blank
    OD_f = OD_p - OD_p[0]
    OD_ps = 0.378 * OD_f + 0.523 * (OD_f ** 2)
    a = 2.303 * OD_ps * area / vol
    ## Need to notice the unit
    return a


def ap_batch(ap_path, aplist, filename):
    ap_bacth = []
    area_list = []
    vol_list = []
    for station in aplist:
        apB1 = ASC_read(ap_path, station['Before Blank'][0])
        apB2 = ASC_read(ap_path, station['Before Blank'][1])
        apB3 = ASC_read(ap_path, station['After Blank'][0])
        apB4 = ASC_read(ap_path, station['After Blank'][1])

        apS1 = ASC_read(ap_path, station['Sample'][0])
        apS2 = ASC_read(ap_path, station['Sample'][1])
        Diameter =station['Diameter']
        vol = station['Vol']
        area = np.pi * (np.mean(Diameter) ** 2) / 4
        area_list.append(area)
        vol_list.append(vol)
        ap_bacth.append(ap_ad_single(apB1, apB2, apB3, apB4, apS1, apS2, vol, area))

    ap_bacth = np.asarray(ap_bacth)
    f = ap_path + filename + '.csv'
    appd = pd.DataFrame(ap_bacth.T)
    appd.to_csv(f)
    return ap_bacth, area_list, vol_list


def ad_batch(ad_path, adlist, filename, area_list, vol_list):
    ad_bacth = []
    for i in range(len(area_list)):
        station = adlist[i]
        adB1 = ASC_read(ad_path, station['Before Blank'][0])
        adB2 = ASC_read(ad_path, station['Before Blank'][1])
        adB3 = ASC_read(ad_path, station['After Blank'][0])
        adB4 = ASC_read(ad_path, station['After Blank'][1])

        adS1 = ASC_read(ad_path, station['Sample'][0])
        adS2 = ASC_read(ad_path, station['Sample'][1])

        vol = vol_list[i]
        area = area_list[i]

        ad_bacth.append(ap_ad_single(adB1, adB2, adB3, adB4, adS1, adS2, vol, area))

    ad_bacth = np.asarray(ad_bacth)
    f = ad_path + filename + '.csv'
    adpd = pd.DataFrame(ad_bacth.T)
    adpd.to_csv(f)
    return ad_bacth


def aph_cal_plot(ap_batch, ad_batch, savepath, fname):
    wave = np.arange(750, 349, -1)
    assert np.shape(ap_batch)[1] == np.shape(wave)[0], "AP Wrong dimension"
    assert np.shape(ad_batch)[1] == np.shape(wave)[0], "AD Wrong dimension"
    l = np.shape(ap_batch)[0]
    aph_batch = ap_batch - ad_batch
    for i in range(l):
        plt.plot(wave, ap_batch[i, :], label='ap')
        plt.plot(wave, ad_batch[i, :], label='ad')
        plt.plot(wave, aph_batch[i, :], label='aph')
        plt.legend()
        plt.title(i + 1)
        plt.show()
    f = savepath + fname + '.csv'
    aphpd = pd.DataFrame(aph_batch.T)
    aphpd.to_csv(f)
