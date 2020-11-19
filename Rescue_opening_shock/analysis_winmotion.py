################################
# Loger reader
# 16/11/2020
# Fred
################################

#%% imports

#%% Import lib
import math
import os
import pickle
import glob
import string
import sys
import time
import traceback
from datetime import date, timedelta
from importlib import reload

import holoviews as hv
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import seaborn as sns


# %% [markdown]
# ### Preparing data
#%% Setting Param

print(" --- Start ----")
start_general = time.time()

cwd = os.path.dirname(os.path.abspath(__file__))
print('cwd:' + cwd)
data_folder_path = os.path.join(cwd, "Data","proceed" )
print('data Folder_path:' + data_folder_path)

all_files = glob.glob(data_folder_path + "/*.txt")

all_files.sort()
li = []

for filename in all_files:
    df = pd.read_csv(filename,sep="\t", index_col=None, skiprows=[0])
    df["filename"]=filename
    li.append(df)

dfi = pd.concat(li, axis=0, ignore_index=True)


dfi.columns = map(str.lower, dfi.columns)

# %% clean 

interesting_col = ["time(s)",
                   "chiptime",
                   "ax(g)",  
                   "ay(g)",  
                   "az(g)",
                   "q0",
                   "q1",
                   "q2",
                   "q3",
                   "filename"]

                    
df = dfi[interesting_col]

df.columns = df.columns.str.replace("(g)","", regex=False)
df.columns = df.columns.str.replace("(s)","", regex=False)

df['chiptime'] = pd.to_datetime(df['chiptime'])
df['time'] = pd.to_datetime(df['time'])

print(df.info())
#%% Check the order of the file 
df.groupby('filename')['chiptime'].describe().sort_values(by=['first'])
df['chiptime'].plot()

#%% exploring
def total_accel ( df) :
    return math.sqrt( df['ax']**2 + df['ay']**2 +df['az']**2 )

# df['accel']= df.apply(total_accel)

df['accel'] = df.apply(lambda row: (math.sqrt( row['ax']**2 + row['ay']**2 +row['az']**2 )),
                                   axis=1)
#%% set chiptime to index
df.set_index('chiptime',inplace=True)

#%% set flag alarm
df['flag_max']=0
df.loc[(df['ax']>15.5) | (df['ay']>15.5) | (df['az']>15.5), ['flag_max']] = -1
#%% Plot

ax = df['accel'].plot()
ax = df['flag_max'].plot()



ax.axhline(y=1,color='m', ls='--', alpha=0.5)
""" ax.grid(b=True, which='minor', color='p', linestyle='--', alpha=0.3) """
ax.grid(b=True, which='major', color='k', linestyle='-',alpha=0.9)

ax.set_ylabel("g Force")
ax.set_xlabel("Time")
#%% Manage results
drop_data={  1 :    { 'id':1 , 'mass':230 ,'pass':1, 'maxg':12.5, 'start':'12:31:38.0' , 'end':'12:31:39.6', 'info':'squared'},
             2 :    { 'id':2 , 'mass':220 ,'pass':0, 'maxg':19.0, 'start':'12:35:47.0' , 'end':'12:35:48.0', 'info':'squared'},
             3 :    { 'id':3 , 'mass':220 ,'pass':0, 'maxg':9.80, 'start':'12:40:48.0' , 'end':'12:40:50.0', 'info':'squared'},
             4 :    { 'id':4 , 'mass':220 ,'pass':0, 'maxg':9.36, 'start':'12:45:35.0' , 'end':'12:45:39.0', 'info':'squared'},
             5 :    { 'id':5 , 'mass':135 ,'pass':1, 'maxg':13.1, 'start':'12:52:21.0' , 'end':'12:52:23.0', 'info':'rogallo'},
             6 :    { 'id':6 , 'mass':125 ,'pass':0, 'maxg':13.7, 'start':'12:57:08.0' , 'end':'12:57:11.0', 'info':'squared'},
             7 :    { 'id':7 , 'mass':120 ,'pass':1, 'maxg':16.7, 'start':'13:01:39.0' , 'end':'13:01:42.0', 'info':'squared'},
             8 :    { 'id':8 , 'mass':115 ,'pass':0, 'maxg':17.3, 'start':'13:05:29.0' , 'end':'13:05:31.0', 'info':'round'},
             9 :    { 'id':9 , 'mass':100 ,'pass':1, 'maxg':11.7, 'start':'13:09:01.0' , 'end':'13:09:03.0', 'info':'squared'},
             10 :   {'id':10 , 'mass':100 ,'pass':0, 'maxg':9.54, 'start':'13:12:36.0' , 'end':'13:12:38.0', 'info':'squared'},
             11 :   {'id':11 , 'mass':100 ,'pass':1, 'maxg':13.1, 'start':'13:15:58.0' , 'end':'13:16:00.0', 'info':'squared'},
             12 :   {'id':12 , 'mass':80  ,'pass':1, 'maxg':11.8, 'start':'13:19:35.0' , 'end':'13:19:37.0', 'info':'squared'},
}


df_drop_list = pd.DataFrame(drop_data).transpose()
dict_pass_fail ={1:"Pass",0:"Fail"}
df_drop_list['pass'] = df_drop_list['pass'].map(dict_pass_fail)


#Compute Force
df_drop_list['force'] = df_drop_list['mass'] * df_drop_list['maxg']* 9.81/10 # /10 for DaN}

#Rename columns for niver output
dict_col_name = {
 "id":"Drop Id",
 "mass":"Mass [Kg]",
 "pass":"Pass/Fail",
 "maxg":"Max g force [g]",
 "start":"Start [hh:mm:ss.s]",
 "end":"End [hh:mm:ss.s]",
 "force":"Force [daN]",
}

df_drop_list = df_drop_list.columns.map(dict_col_name)

print(df_drop_list)

#%% FINISH
print(" -------")

end_general = time.time()
print(f" Time total :{end_general - start_general} s")
print(" --- ENd ----")

#%%
