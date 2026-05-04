# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 12:12:16 2025

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

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 9})
plt.rcParams.update({'axes.titlesize': 9})
plt.rcParams.update({'axes.labelsize': 9})
plt.rcParams.update({'lines.markersize': 9})
plt.rcParams.update({'legend.fontsize': 9})
plt.rc('xtick', labelsize=9) 
plt.rc('ytick', labelsize=9)

#%% load data


df = pd.read_csv("data/free_error_data.csv")

modes = df['Mode']
err_9 = df['error_9']
err_16 = df['error_16']
err_25 = df['error_25']
err_36 = df['error_36']
err_49 = df['error_49']
err_64 = df['error_64']





#%% plot free plate

plt.figure(figsize=(5.5,2.2))
# plt.plot(time,voltage,'-', markersize=3, label='battery')
plt.plot(modes,err_9,'--', markersize=4, marker ="v", label='9 nodes')
plt.plot(modes,err_16,'-', markersize=4, marker ="s", label='16 nodes')
plt.plot(modes,err_25,'--', markersize=4, marker ="x", label='25 nodes')
plt.plot(modes,err_36,'-', markersize=4, marker ="+", label='36 nodes')
plt.plot(modes,err_49,'--', markersize=4, marker ="o", label='49 nodes')
plt.plot(modes,err_64,'-', markersize=4, marker ="^", label='64 nodes')

plt.locator_params(axis="x", nbins=8)
plt.locator_params(axis="y", nbins=8)
# plt.plot(time,power,'.')
plt.ylabel('error (%)')
plt.xlabel('modes')
plt.legend(framealpha=1, fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.savefig('figure/free_plate_error.pdf', dpi=500)












