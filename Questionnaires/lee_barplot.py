# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:54:14 2017

@author: alenia
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns






f2fr = pd.read_csv(r'CSV/Real_synth_corrs_csv/f2fr.csv')
f2fs = pd.read_csv(r'CSV/Real_synth_corrs_csv/f2fs.csv')
f2or = pd.read_csv(r'CSV/Real_synth_corrs_csv/f2or.csv')
f2os = pd.read_csv(r'CSV/Real_synth_corrs_csv/f2os.csv')

f2fr = f2fr.dropna()
f2fs = f2fs.dropna()
f2or = f2or.dropna()
f2os = f2os.dropna()

w1 = (np.ones_like(f2fr[f2fr.columns[0]]) / len(f2fr[f2fr.columns[0]]))*100
w2 = (np.ones_like(f2fs[f2fs.columns[0]]) / len(f2fs[f2fs.columns[0]]))*100
w3 = (np.ones_like(f2or[f2or.columns[0]]) / len(f2or[f2or.columns[0]]))*100
w4 = (np.ones_like(f2os[f2os.columns[0]]) / len(f2os[f2os.columns[0]]))*100


y1 = np.array(f2fr['Inter-ROI Correlations (Real)'])
y1 = np.absolute(y1)
y2 = np.array(f2fs['Inter-ROI Correlations (synthetic)'])
y2 = np.absolute(y2)

y3 = np.array(f2or['ROI-Outcome Correlations (Real)'])
y4 = np.array(f2os['ROI-Outcome Correlations (Synthetic)'])
y3 = np.absolute(y3)
y4 = np.absolute(y4)


y12 = [y1,y2]
y34 = [y3,y4]
plt.subplot(1,2,1)
plt.hist(y34,bins=50,orientation='horizontal',weights=[w3,w4])
#plt.xscale('log')
plt.title('ROI-Outcome Correlations')
plt.legend(['Real','synthetic'],loc='upper left')
plt.xlabel('% overall')
plt.ylabel('values')
plt.gca().invert_xaxis()


plt.subplot(1,2,2)
plt.hist(y12,bins=50,orientation='horizontal',weights=[w1,w2])
#plt.xscale('log')
plt.title('Inter-ROI Correlations')
plt.legend(['Real','synthetic'],loc='upper right')

plt.tight_layout()