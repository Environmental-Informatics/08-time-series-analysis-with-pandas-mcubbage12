#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:31:58 2020
#this file uses USGS gage data to graph long term CFS over the years 2015 and 2016
@author: mcubbage (marissa cubbage)
"""
#import packages 
import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt


#read in data
river_data= pd.read_table( 'WabashRiver_DailyDischarge_20150317-20160324.txt', skiprows=[0,23,25], header=[24], parse_dates=[[2,3]])

#create time series data 
datesr = pd.date_range('2015-03-17 04:30:00', periods=river_data.shape[0], freq='15min')
datesr.shape
CFS = Series(river_data['23100'].values, index=datesr)


#resample to get mean daily CFS
CFS_mm = CFS.resample("D").mean()

#plot mean daily CFS
ax= CFS_mm.plot()
ax.set_xlabel('Time')
ax.set_ylabel('Daily Average Streamflow')
plt.savefig('Day_AVE_Streamflow.pdf') 

#find 10 days in data with highest daily average stream flow 
CFS_mm.sort_values(ascending=False)

#plot top 10 discharge days
ax=CFS_mm[0:9].plot(style='g^')
ax.set_xlabel('Time')
ax.set_ylabel('Top 10 daily average streamflow')
plt.savefig('top_10Day_AVE_Streamflow.pdf') 

#resample to get monthly average streamflow
CFS_month = CFS.resample("M").mean()

#plot mean monthly streamflow
ax= CFS_month.plot()
ax.set_xlabel('Time')
ax.set_ylabel('Monthly Average Streamflow')
plt.savefig('Month_AVE_Streamflow.pdf') 
