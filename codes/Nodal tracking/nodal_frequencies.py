# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:58:31 2023

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
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 9})
plt.rcParams.update({'axes.titlesize': 9})
plt.rcParams.update({'axes.labelsize': 9})
plt.rcParams.update({'lines.markersize': 9})
plt.rcParams.update({'legend.fontsize': 9})
plt.rc('xtick', labelsize=9) 
plt.rc('ytick', labelsize=9)

#%% FREE PLATE
# data = np.loadtxt('data/Frequency_data.txt',skiprows=2)

plt.close('all') 

# modes = data[:,0]

#%% Node 6

# ge_6 = data[:,1]
# LEMP_6 = data[:,2]
# error_6 = data[:,3]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_6,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_6,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_6,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node6.pdf', dpi=500)
# plt.show()


#%% Node 7

# ge_7 = data[:,4]
# LEMP_7 = data[:,5]
# error_7 = data[:,6]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_7,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_7,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_7,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node7.pdf', dpi=500)
# plt.show()

#%% Node 8

# ge_8 = data[:,7]
# LEMP_8 = data[:,8]
# error_8 = data[:,9]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_8,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_8,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_8,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node8.pdf', dpi=500)
# plt.show()

#%% Node 13

# ge_13 = data[:,22]
# LEMP_13 = data[:,23]
# error_13 = data[:,24]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_13,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_13,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_13,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node13.pdf', dpi=500)
# plt.show()

#%% Node 14

# ge_14 = data[:,25]
# LEMP_14 = data[:,26]
# error_14 = data[:,27]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_14,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_14,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_14,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node14.pdf', dpi=500)
# plt.show()

#%% Node 15

# ge_15 = data[:,28]
# LEMP_15 = data[:,29]
# error_15 = data[:,30]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_15,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_15,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_15,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node15.pdf', dpi=500)
# plt.show()

#%% Node 16

# ge_16 = data[:,31]
# LEMP_16 = data[:,32]
# error_16 = data[:,33]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_16,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_16,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_16,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node16.pdf', dpi=500)
# plt.show()

#%% Node 17

# ge_17 = data[:,34]
# LEMP_17 = data[:,35]
# error_17 = data[:,36]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_17,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_17,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_17,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node17.pdf', dpi=500)
# plt.show()

#%% Node 18

# ge_18 = data[:,37]
# LEMP_18 = data[:,38]
# error_18 = data[:,39]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_18,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_18,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_18,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node18.pdf', dpi=500)
# plt.show()


#%% Node 23

# ge_23 = data[:,52]
# LEMP_23 = data[:,53]
# error_23 = data[:,54]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_23,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_23,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_23,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node23.pdf', dpi=500)
# plt.show()

#%% Node 24

# ge_24 = data[:,55]
# LEMP_24 = data[:,56]
# error_24 = data[:,57]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_24,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_24,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_24,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('figures/node24.pdf', dpi=500)
# plt.show()

#%% Node 25

# ge_25 = data[:,58]
# LEMP_25 = data[:,59]
# error_25 = data[:,60]


# fig, ax1 = plt.subplots(figsize=(3.3,2.7))
# # plt.grid(True)
# # color = 'tab:'
# ax1.set_xlabel('mode')
# ax1.set_ylabel('frequency (Hz)')
# ax1.plot(modes, ge_25,'--s', markersize= 4, linewidth=2, label='GE')
# ax1.plot(modes, LEMP_25,'-.o', markersize= 2, linewidth=1, label='LEMP')
# # ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
# ax1.tick_params(axis='y')
# plt.locator_params(axis="x", nbins=8)
# plt.locator_params(axis="y", nbins=6)
# # plt.yscale('log', base=100)
# # plt.ylim(100,600)
# plt.legend(framealpha=1, fontsize=10)
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:red'
# ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
# ax2.plot(modes, error_25,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
# ax2.tick_params(axis='y', labelcolor=color)
# plt.legend(framealpha=1, fontsize=10)
# plt.locator_params(axis="y", nbins=8)
# plt.ylim(-.5,100)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# # plt.savefig('figures/node25.pdf', dpi=500)
# plt.show()


#%% Mode 7

node_data = np.loadtxt('data/node7_data.txt',skiprows=1)

node_number = node_data[:,0]
ge_7 = node_data[:,1]
lemp_7 = node_data[:,2]
error_7 = node_data[:,3]


fig, ax1 = plt.subplots(figsize=(4,2))
plt.grid(True)
# color = 'tab:'
ax1.set_xlabel('node number')
ax1.set_ylabel('frequency (Hz)')
ax1.plot(node_number, ge_7,'--s', markersize= 3 , linewidth=1.5, label='GE')
ax1.plot(node_number, lemp_7,'-.o', markersize= 2, linewidth=1, label='LEMP')
# ax1.plot(thick, Mae,'--',linewidth=4, label='solveset')
ax1.tick_params(axis='y')
plt.locator_params(axis="x", nbins=12)
plt.locator_params(axis="y", nbins=8)
# plt.yscale('log', base=100)
plt.ylim(1350,1705)
plt.legend(framealpha=1, fontsize=9)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('error (%)', color=color)  # we already handled the x-label with ax1
ax2.plot(node_number, error_7,'o--', markersize=1.5, linewidth=.5, color=color, label='error')
ax2.tick_params(axis='y', labelcolor=color)
plt.legend(framealpha=1, fontsize=9)
plt.locator_params(axis="y", nbins=8)
plt.ylim(-.5,100)
# plt.grid(True)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('figures/node7_data.pdf', dpi=500)
plt.show()