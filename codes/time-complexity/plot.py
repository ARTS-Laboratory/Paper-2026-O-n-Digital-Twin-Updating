# -*- coding: utf-8 -*-
"""
Created on Mon May  1 09:34:06 2023

@author: OGUNNIYI
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy
import math
import json
from scipy.stats import linregress
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

# from pylab import *
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 8})
plt.rcParams.update({'axes.titlesize': 8})
plt.rcParams.update({'axes.labelsize': 8})
plt.rcParams.update({'lines.markersize': 8})
plt.rcParams.update({'legend.fontsize': 8})
plt.rc('xtick', labelsize=8) 
plt.rc('ytick', labelsize=8) 

plt.close('all') 

#%% Load data

data = np.loadtxt("data_all_nodes.txt", skiprows=1)

df = pd.read_csv("data_last_nodes.csv")

node_num = data[:,0]

time_GE = data[:,3]

time_LEMP = data[:,4]

#%% Calculate logarithms

df['log_nodenum'] = np.log(df['nodenum'])
df['log_timeGE'] = np.log(df['timeGE'])
df['log_timeLEMP'] = np.log(df['timeLEMP'])

# Fit linear regression on log-log data
GE_fit = linregress(df['log_nodenum'], df['log_timeGE'])
LEMP_fit = linregress(df['log_nodenum'], df['log_timeLEMP'])


#%% Plot GEP log-log fit

plt.figure(figsize=(3.2,2))
# plt.scatter(df['log_nodenum'], df['log_timeGE'], color='blue', label='GE Data')
plt.plot(df['log_nodenum'], df['log_timeGE'], '-.o', markersize= 4, label='GEP')
plt.plot(df['log_nodenum'],
         GE_fit.intercept + GE_fit.slope * df['log_nodenum'],
         color='#d62728', label='GE fit')
plt.locator_params(axis="y", nbins=8)
plt.xlim(4.0, 5.2 )
plt.xlabel('log(number of nodes)')
plt.ylabel('log(time (s))')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('figures/GE_log-log.pdf', dpi=500)

#%% Plot LEMP log-log fit
plt.figure(figsize=(3.2,2))
# plt.scatter(df['log_nodenum'], df['log_timeLEMP'], color='green', label='LEMP Data')
plt.plot(df['log_nodenum'], df['log_timeLEMP'], '-.s', color='#ff7f0e', markersize= 4, label=r'LEMP')
plt.plot(df['log_nodenum'],
         LEMP_fit.intercept + LEMP_fit.slope * df['log_nodenum'],
         color='#d62728', label='LEMP fit')
plt.locator_params(axis="y", nbins=6)
plt.xlim(4.0, 5.2 )
plt.xlabel('log(number of nodes)')
plt.ylabel('log(time (s))')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('figures/LEMP_log-log.pdf', dpi=500)
plt.show()


