#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 19:20:01 2018

"""
mask = fits.open('mask.fits')[0].data
allslopes = fits.open('trnslos_20180222.fits')[0].data

xind, yind = np.where(mask==1)
xslos = np.zeros((6000,7,7))
yslos = np.zeros((6000,7,7))
for i in range(6000):
    xslos[i,:,:][yind,xind] = allslopes[i,:36]
    yslos[i,:,:][yind,xind] = allslopes[i,36:72]
    
header = fits.Header()
header["r_0"] = str([0.16])
header["WINDSPD"] = str([5])
header["WINDDIR"] = str([0])
header["ITERS"] = str([6000])
header['ITERTIME'] = str([0.012])
header['SLODIR'] = 'x'
header["SAVETIME"] = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
fits.writeto("xslos_20180222.fits",xslos,header,overwrite=True)
header['SLODIR'] = 'y'
fits.writeto("yslos_20180222.fits",yslos,header,overwrite=True)
    


    
    