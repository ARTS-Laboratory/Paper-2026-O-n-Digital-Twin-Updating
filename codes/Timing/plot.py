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

#%% GEP, LEMP plot

# plt.figure(figsize=(3.2,2))
# plt.plot(node_num, time_GE,'--o', markersize=3)
# plt.plot(node_num, time_LEMP,'-.s', markersize=3)
# plt.legend(['GEP','LEMP'], framealpha=1)
# plt.locator_params(axis="x", nbins=8)
# # plt.locator_params(axis="y", nbins=6)
# plt.grid()
# plt.ylabel('time (s)')
# plt.xlabel('number of nodes')
# plt.tight_layout()
# # plt.savefig('figures/time1.pdf', dpi=500)


# fig, ax1 = plt.subplots(figsize=(4,2))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('number of nodes')
# ax1.set_ylabel('time (s)')
# ax1.plot(node_num, time_GE,'--o', markersize= 4, linewidth=1.5, label='GEP')
# # ax1.plot(node_num, freq_LEMP,'-.o', markersize= 3, linewidth=1.5, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# plt.grid()
# # plt.yscale('log', base=100)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:orange'
# ax2.set_ylabel('time (ms)', color=color)  # we already handled the x-label with ax1
# ax2.plot(node_num, time_LEMP*1000,'--s', markersize=4, linewidth=1, color=color, label='LEMP')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(0.3, 1.6)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# # plt.savefig('figures/O(n) plot.pdf', dpi=500)
# plt.show()


#%% GEP, LEMP log scale plot

# plt.figure(figsize=(3.2,2))
# plt.yscale('log', base=10)
# plt.plot(node_num, time_GE,'--o', markersize=3)
# plt.plot(node_num, time_LEMP,'-.s', markersize=3)
# plt.legend(['GEP','LEMP'], framealpha=1)
# plt.locator_params(axis="x", nbins=8)
# # plt.locator_params(axis="y", nbins=6)
# plt.ylim(10^(-4), 10^1 )
# plt.xlim(0, 175 )
# plt.grid()
# plt.ylabel('time (s)')
# plt.xlabel('number of nodes')
# plt.tight_layout()
# plt.savefig('figures/time.pdf', dpi=500)

#%% computional gain

# plt.figure(figsize=(2.9,2.1))
# plt.plot(node_num, time_GE/time_LEMP,'--s', markersize=3)
# # plt.plot(node_num, time_LEMP,'-.s', markersize=3)
# plt.legend(['computational gain'], framealpha=1)
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-150, 3000 )
# plt.xlim(0, 175 )
# plt.grid()
# plt.ylabel('computational gain (#x)')
# plt.xlabel('number of nodes')
# plt.tight_layout()
# plt.savefig('figures/speed_up2.pdf', dpi=500)

#%% Plot GEP log-log fit

plt.figure(figsize=(12,5))
# plt.scatter(df['log_nodenum'], df['log_timeGE'], color='blue', label='GE Data')
plt.plot(df['log_nodenum'], df['log_timeLEMP'], '--o', color='blue', label='GEP Data')
plt.plot(df['log_nodenum'],
         GE_fit.intercept + GE_fit.slope * df['log_nodenum'],
         color='red', label='GE Fit')
plt.xlabel('log(Node Number)')
plt.ylabel('log(GE Runtime)')
plt.grid()
plt.title('Log-Log Regression: GE')
plt.legend()
plt.tight_layout()
plt.show()
# plt.savefig('figures/speed_up2.pdf', dpi=500)

# #%% Plot LEMP log-log fit
# plt.figure(figsize=(12,5))
# # plt.scatter(df['log_nodenum'], df['log_timeLEMP'], color='green', label='LEMP Data')
# plt.plot(df['log_nodenum'], df['log_timeLEMP'], '--s', color='orange', label='LEMP Data')
# plt.plot(df['log_nodenum'],
#          LEMP_fit.intercept + LEMP_fit.slope * df['log_nodenum'],
#          color='red', label='LEMP Fit')
# plt.xlabel('log(Node Number)')
# plt.ylabel('log(LEMP Runtime)')
# plt.grid()
# plt.title('Log-Log Regression: LEMP')
# plt.legend()
# plt.tight_layout()
# # plt.savefig('figures/speed_up2.pdf', dpi=500)
# plt.show()


