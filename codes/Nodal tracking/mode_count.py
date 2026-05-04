# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 18:13:38 2025

@author: OGUNNIYI
"""

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 9})
plt.rcParams.update({'axes.titlesize': 9})
plt.rcParams.update({'axes.labelsize': 9})
plt.rcParams.update({'lines.markersize': 9})
plt.rcParams.update({'legend.fontsize': 9})
plt.rc('xtick', labelsize=9) 
plt.rc('ytick', labelsize=9)

# Manually reconstructing data based on image structure
modes = list(range(1, 16))
counts = [0, 2, 15, 8, 2, 2, 17, 11, 0, 0, 0, 0, 2, 0, 0]

# Create a histogram plot
plt.figure(figsize=(2.5, 2))
plt.bar(modes, counts, edgecolor='black')
plt.xlabel("mode")
plt.ylabel("count")
# plt.locator_params(axis="x", nbins=4)
# plt.locator_params(axis="y", nbins=8)
# plt.title("Histogram of Mode vs Count")
plt.ylim(0, 20)
plt.xticks(modes)  # Ensure all modes are labeled
plt.tight_layout()
plt.savefig('figures/mode_count.pdf', dpi=500)

# Show the plot
plt.show()
