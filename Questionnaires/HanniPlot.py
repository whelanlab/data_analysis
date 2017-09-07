# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:20:53 2017

@author: alenia
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('full_COGNz PROCWMz DATA_violinplot.csv')


df['fake']=1
hashtable = {1:'MS',2:'Control'}          
df['Group'].replace(hashtable,inplace=True)

plt.subplot(1,3,1)


ax = sns.violinplot(x='fake',y='COGNz_mo0',data=df,hue='Group',split=True,legend=None)
plt.ylabel('Cognitive efficiency composite score')
plt.xlabel('Month 0')
plt.xticks([])
plt.ylim([-3,2])
#plt.axis([-1,1, -3, 2])
ax.legend().set_visible(False)



plt.subplot(1,3,2)
ax=sns.violinplot(x='fake',y='COGNz_mo13',data=df,hue='Group',split=True)
plt.xlabel('Month 13')
plt.xticks([])
plt.ylabel('aa')
ax.legend().set_visible(False)
ax.yaxis.label.set_visible(False)
plt.ylim([-3,2])
#plt.axis([-3, 3, -3, 3])


plt.subplot(1,3,3)

ax=sns.violinplot(x='fake',y='COGNz_mo26',data=df,hue='Group',split=True)
plt.xlabel('Month 26')
plt.ylabel('aaaa')
plt.xticks([])
plt.ylim([-3,2])

#plt.axis([-3, 3, -3, 3])
ax.yaxis.label.set_visible(False)



plt.tight_layout()
plt.show()
plt.savefig('hannipic.tiff')
