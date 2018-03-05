#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 15:18:24 2018

"""
import numpy as np
from numpy import abs as abs
from numpy import size as size
from numpy import cov as cove

def covmap(ma,mb):
    l = np.shape(ma)[0]
    covmtx = np.empty((2*l-1,2*l-1))
    for delta_x in range(-l+1,l):
        for delta_y in range(-l+1,l):
            if delta_x<=0 and delta_y<=0:
                slidea = ma[:l-abs(delta_x),:l-abs(delta_y)].flatten()
                slideb = mb[abs(delta_x):,abs(delta_y):].flatten()
            if delta_x<0 and delta_y>0:
                slidea = ma[:l-abs(delta_x),delta_y:].flatten()
                slideb = mb[abs(delta_x):,:l-delta_y].flatten()
            if delta_x>0 and delta_y<0:
                slidea = ma[delta_x:,:l-abs(delta_y)].flatten()
                slideb = mb[:l-delta_x,abs(delta_y):].flatten()
            if delta_x>=0 and delta_y>=0:
                slidea = ma[delta_x:,delta_y:].flatten()
                slideb = mb[:l-delta_x,:l-delta_y].flatten()
            if size(slidea)>1:
                temp = np.stack((slidea,slideb)) 
                covmtx[l-1+delta_x,l-1+delta_y] = cov(temp)[0,1]
            else :
                covmtx[l-1+delta_x,l-1+delta_y] = 0
#    covmtx /= covmtx.max()                   
    return covmtx
              
h = fits.open('xslos_20180222.fits')
xslos = h[0].data

#nor_xslos = np.empty((6000,7,7))
#for i in range(6000):
#    temp = xslos[i]
#    temp[xind,yind] -= temp[xind,yind].mean()
#    nor_xslos[i] = temp
#fits.writeto('nor_xslos_20180222.fits',nor_xslos,overwrite='True')

step = 10
allcovmtx = np.empty((6000-step,13,13))
for i in range(6000-step):
    ma = xslos[i]
    mb = xslos[i+step]
    allcovmtx[i] = covmap(ma,mb)
    
a = np.mean(allcovmtx,axis=0)   
plt.imshow(a) 
        