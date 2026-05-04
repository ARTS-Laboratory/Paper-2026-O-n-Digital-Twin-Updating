# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:12:16 2025

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the CSV data
df = pd.read_csv("data_last_nodes.csv")

# Calculate logarithms
df['log_nodenum'] = np.log(df['nodenum'])
df['log_timeGE'] = np.log(df['timeGE'])
df['log_timeLEMP'] = np.log(df['timeLEMP'])

# Fit linear regression on log-log data
GE_fit = linregress(df['log_nodenum'], df['log_timeGE'])
LEMP_fit = linregress(df['log_nodenum'], df['log_timeLEMP'])

# Plot GE
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.scatter(df['log_nodenum'], df['log_timeGE'], color='blue', label='GE Data')
plt.plot(df['log_nodenum'],
         GE_fit.intercept + GE_fit.slope * df['log_nodenum'],
         color='red', label='GE Fit')
plt.xlabel('log(Node Number)')
plt.ylabel('log(GE Runtime)')
plt.title('Log-Log Regression: GE')
plt.legend()

# Plot LEMP
plt.subplot(1,2,2)
plt.scatter(df['log_nodenum'], df['log_timeLEMP'], color='green', label='LEMP Data')
plt.plot(df['log_nodenum'],
         LEMP_fit.intercept + LEMP_fit.slope * df['log_nodenum'],
         color='red', label='LEMP Fit')
plt.xlabel('log(Node Number)')
plt.ylabel('log(LEMP Runtime)')
plt.title('Log-Log Regression: LEMP')
plt.legend()

plt.tight_layout()
plt.show()
