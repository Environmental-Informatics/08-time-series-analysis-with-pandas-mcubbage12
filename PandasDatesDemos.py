#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:14:29 2020
This script provides code that was learned from the online tutorial "Time Series Analysis with Pandas"
@author: mcubbage (Marissa Cubbage)
"""
#import neccessary packages
import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt


#import the data
!wget http://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/monthly.ao.index.b50.current.ascii
ao = np.loadtxt('monthly.ao.index.b50.current.ascii')

#shape of array
ao.shape


#create as many elements as time stamps we have in data using month as the stamp and Jan 1950 as the start (this info is from the dataframe)
dates = pd.date_range('1950-01', periods=ao.shape[0], freq='M')

#shape of array
dates.shape


#create dataframe that syncs the data index to values 
AO = Series(ao[:,2], index=dates)
AO

#plot the entire time series 
AO.plot()
#save AO as PDF
plt.savefig('AO_plot.pdf')  


#pther plots or just parts of the time series
AO['1980':'1990'].plot()
AO['1980-05':'1981-03'].plot()


#accessing values by numbers or by index
AO[120]
AO['1960-01']
AO['1960']

#import additional data
!wget http://www.cpc.ncep.noaa.gov/products/precip/CWlink/pna/norm.nao.monthly.b5001.current.ascii
nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')

#create time series with as many eelements as there are dates 
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')
NAO = Series(nao[:,2], index=dates_nao)

#check to see if AO ad NAO data have same length time series data
dates.shape

aonao.corr()


dates_nao.shape


#create data frame with both NAO and AO data 
aonao = DataFrame({'AO' : AO, 'NAO' : NAO})

#check shape of new data frames. any NAN are becasue the data frames are not the same size
aonao.shape

#plot the data
aonao.plot(subplots=True)

#look a the first few rows of data
aonao.head()

#reference just NAO data using its name
aonao['NAO']
#reference data using data frame variable
aonao.NAO

#add columns and delete columns
aonao['Diff'] = aonao['AO'] - aonao['NAO']
aonao.head()
del aonao['Diff']
aonao.tail()

#select just a few rows of data (slicing)
aonao['1981-01':'1981-03']

#use slicing to graph only some of the data
import datetime
aonao.loc[(aonao.AO > 0) & (aonao.NAO < 0) 
        & (aonao.index > datetime.datetime(1980,1,1)) 
        & (aonao.index < datetime.datetime(1989,1,1)),
        'NAO'].plot(kind='barh')

#statistics(minimum, maximum, mean, median) by coloumn
aonao.mean()
aonao.max()
aonao.min()

#statistics by row
aonao.mean(1)

#most base statistics all at once
aonao.describe()

#graph time series data based on a different time scale using a statistic(mean, median, etc) (resampling)
AO_mm = AO.resample("A").mean()
AO_mm.plot(style='g--')

AO_mm = AO.resample("A").median()
ax= AO_mm.plot()
ax.set_xlabel('Year')
ax.set_ylabel('Annual median values for AO')
plt.savefig('AOmm_plot.pdf') 


AO_mm = AO.resample("3A").apply(np.max)
AO_mm.plot()

AO_mm = AO.resample("A").apply(['mean', np.min, np.max])
AO_mm['1900':'2020'].plot(subplots=True)
AO_mm['1900':'2020'].plot()

#moving/rolling statistics (mean, correllation, )
aonao.rolling(window=12, center=False).mean().plot(style='-g')

ax=aonao.AO.rolling(window=120).corr(other=aonao.NAO).plot(style='-g')
ax.set_xlabel('Year')
ax.set_ylabel('Rolling mean for both AO and NAO ')
plt.savefig('Rollingmean_plot.pdf') 


#to get correllation coefficients
aonao.corr()











