#%% [markdown]

#----------------------------------
# # Logger reader
#
# ## Session 2
#
# 27/12/2020 - Fred
#
#----------------------------------


#%% Import lib
import math
import os

import glob
# import string
# import sys
import time

from datetime import date,  datetime

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
data_folder_path = os.path.join(cwd, "Data","proceed" ,"session_2020-12-21")
print('Data Folder_path:' + data_folder_path)

report_folder_path = os.path.join(cwd, "report","2020-12-21",'image')
print('Report Folder_path:' + report_folder_path)

date_time_str = '2020-12-21 '

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
df.drop(columns=['time'],inplace=True)
#df['time'] = pd.to_datetime(df['time'])

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

#%% [markdown]
# We set and alert flat if one axis exeed 15.5 g , as the sensor specs is 16g. it is display on the grpah by a orange cruve goding to -1
#%% set flag alarm
df['flag_max']=0
df.loc[(df['ax']>15.5) | (df['ay']>15.5) | (df['az']>15.5), ['flag_max']] = -1


#%% hand results
drop_data={  1 :    { 'id':1 ,'mass':230 ,'pass':'?',  'maxg':8.83 , 'in':'14:11:07' ,'start':'14:11:08', 'end':	'14:11:14'	,'out':	'14:11:22' , 'info':'??'},
             2 :    { 'id':2 ,'mass':220 ,'pass':'?',  'maxg':9.50 , 'in':'14:16:04' ,'start':'14:16:05', 'end':	'14:16:07'  ,'out':	'14:16:10' , 'info':'??'},
             3 :    { 'id':3 ,'mass':220 ,'pass':'?',  'maxg':10.75, 'in':'14:21:13' ,'start':'14:21:14', 'end':	'14:21:18'	,'out':	'14:21:20' , 'info':'??'},
             4 :    { 'id':4 ,'mass':210 ,'pass':'?',  'maxg':5.36 , 'in':'14:25:20' ,'start':'14:25:21', 'end':	'14:25:24'	,'out':	'14:25:28' , 'info':'??'},
             5 :    { 'id':5 ,'mass':140 ,'pass':'yes','maxg':10.28, 'in':'14:30:02' ,'start':'14:30:03', 'end':	'14:30:06'	,'out':	'14:30:08' , 'info':'squared (ozone)'},
             6 :    { 'id':6 ,'mass':125 ,'pass':'?',  'maxg':17.61, 'in':'14:33:46' ,'start':'14:33:47', 'end':	'14:33:50'	,'out':	'14:33:54' , 'info':'??'},
             7 :    { 'id':7 ,'mass':125 ,'pass':'?',  'maxg':14.24, 'in':'14:37:20' ,'start':'14:37:21', 'end':	'14:37:24'	,'out':	'14:37:27' , 'info':'??'},
             8 :    { 'id':8 ,'mass':120 ,'pass':'?',  'maxg':14.49, 'in':'14:41:02' ,'start':'14:41:03', 'end':	'14:41:06'	,'out':	'14:41:08' , 'info':'??'},
             9 :    { 'id':9 ,'mass':115 ,'pass':'?',  'maxg':11.01, 'in':'14:44:31' ,'start':'14:44:32', 'end':	'14:44:34'	,'out':	'14:44:36' , 'info':'??'},
             10 :   {'id':10 ,'mass':115 ,'pass':'?',  'maxg':15.37, 'in':'14:47:36' ,'start':'14:47:37', 'end':	'14:47:39'	,'out':	'14:47:42' , 'info':'??'},
             11 :   {'id':11 ,'mass':100 ,'pass':'?',  'maxg':13.83, 'in':'14:51:06' ,'start':'14:51:07', 'end':	'14:51:10'	,'out':	'14:51:13' , 'info':'??'},
             12 :   {'id':12 ,'mass':90  ,'pass':'?',  'maxg':16.74, 'in':'14:55:10' ,'start':'14:55:11', 'end':	'14:55:13'	,'out':	'14:55:15' , 'info':'??'},
             13 :   {'id':13 ,'mass':80  ,'pass':'?',  'maxg':13.58, 'in':'14:58:16' ,'start':'14:58:17', 'end':	'14:58:19'	,'out':	'14:58:23' , 'info':'??'},
}

#%% Plot

ax = df['accel'].plot(figsize=(18,12))
ax = df['flag_max'].plot()

ax.axhline(y=1,color='m', ls='--', alpha=0.5)
""" ax.grid(b=True, which='minor', color='p', linestyle='--', alpha=0.3) """
ax.grid(b=True, which='major', color='k', linestyle='-',alpha=0.9)

ax.set_ylabel("g Force")
ax.set_xlabel("Time")
ax.set_title(f"All drops graph")
ax.set_xlim([datetime(2020, 12, 21,14,10), datetime(2020, 12, 21,15,1)])

#add drop number 
for key, value in drop_data.items():
    drop_time =  datetime.strptime(date_time_str + value['start'], '%Y-%m-%d %H:%M:%S')
    ax.text(drop_time , -1.5, key, horizontalalignment='left',
                      verticalalignment='top' , fontsize=14, color='dimgray') 


fig = ax.get_figure()
fig.tight_layout()
fig.savefig( os.path.join(report_folder_path, f"Figure_all.png"))


#%% extract all graph 

for key, value in drop_data.items():
    print("zoom drop: ", key)
    date_time_start = datetime.strptime(date_time_str + value['start'], '%Y-%m-%d %H:%M:%S')
    date_time_end = datetime.strptime(date_time_str + value['end'], '%Y-%m-%d %H:%M:%S')
    date_time_in = datetime.strptime(date_time_str + value['in'], '%Y-%m-%d %H:%M:%S')
    date_time_out = datetime.strptime(date_time_str + value['out'], '%Y-%m-%d %H:%M:%S')


    df_shock = df[date_time_start:date_time_end]
    df_ind = df[date_time_in:date_time_out]
    max_g = df_shock['accel'].max()
    time_max_g = df_shock['accel'].idxmax()
    value['maxg']= max_g

    ax_ind = df_ind['accel'].plot(figsize=(13,8))
    ax_ind = df_ind['flag_max'].plot()

    ax_ind.axhline(y=1,color='m', ls='--', alpha=0.5)
    
    ax_ind.axvline(x=date_time_start,color='grey', ls='--', alpha=0.8)
    ax_ind.axvline(x=date_time_end  ,color='grey', ls='--', alpha=0.8)
    ax_ind.annotate(s='', xy=(date_time_start,max_g+5), xytext=(date_time_end,max_g+5), arrowprops=dict(arrowstyle='<->'))
    ax_ind.text(date_time_start , max_g+6, '  Opening', horizontalalignment='left',
                      verticalalignment='top' , fontsize=14, color='gray') 
    
    ax_ind.text(time_max_g , max_g+3, f" {round(max_g,2)} g  mass: {value['mass']} kg\n pass: {value['pass']}  info: {value['info']} ", horizontalalignment='left',
                      verticalalignment='top', fontsize=13 , color='b')


    """ ax.grid(b=True, which='minor', color='p', linestyle='--', alpha=0.3) """
    ax_ind.grid(b=True, which='major', color='k', linestyle='-',alpha=0.9)


    ax_ind.set_ylabel("g Force")
    ax_ind.set_xlabel("Time")
    ax_ind.set_title(f"Zoom drop #{key}")
    ax_ind.plot()
    fig_ind = ax_ind.get_figure()
    fig_ind.tight_layout()
    fig_ind.savefig( os.path.join(report_folder_path, f"zoom_{key}.png"))
    fig_ind.clf()

print('end export')

#%% 
df_drop_list = pd.DataFrame(drop_data).transpose()
dict_pass_fail ={1:"Pass",0:"Fail",'?':"?",'yes':"Pass",'no':"Fail"}
df_drop_list['pass'] = df_drop_list['pass'].map(dict_pass_fail)


#Compute Force
df_drop_list['force'] = df_drop_list['mass'] * df_drop_list['maxg']* 9.81/10 # /10 for DaN}

#%%Rename columns for nicer output
dict_col_name = {
 "id":"Drop Id",
 "mass":"Mass [Kg]",
 "pass":"Pass/Fail",
 "maxg":"Max g force [g]",
 "in":"Start_drop [hh:mm:ss.s]",
 "out":"End_drop [hh:mm:ss.s]",
 "start":"Start_opening [hh:mm:ss.s]",
 "end":"End_opening [hh:mm:ss.s]",
 "force":"Force [daN]",
}

df_drop_list.columns = df_drop_list.columns.map(dict_col_name)

print(df_drop_list)

#%% FINISH
print(" -------")

end_general = time.time()
print(f" Time total :{end_general - start_general} s")
print(" --- ENd ----")

#%%

# %%
