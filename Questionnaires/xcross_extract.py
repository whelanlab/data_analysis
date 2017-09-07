import pandas as pd
import merge
import numpy as np




data = merge.merge_data()
df1 = data[np.logical_or(data.Study == 'UG',data.Study == 'BCANN')]
df2 = data[data.Study == 'CANN_MB']
#df3 = data[data.Study == 'ERAB']

df3 = data[data.index.str.contains('JF')]                                      
frames = [df1,df2,df3]
xcross = pd.concat(frames)
xcross.dropna(axis=1, how='all',inplace=True)
xcross.to_csv('xsectional.csv')

