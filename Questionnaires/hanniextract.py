import pandas as pd
import merge #import library that process the qs
import numpy as np

data = merge.merge_data() #function that obtain the general dataset

data = data[np.logical_or(data.Study=='ADHD_surveycto',data.Study=='ADHD_qualtrics')] 
#filter by study type

columns= [
'code',
'DIA',
'DIAyr',
'ADHD_subtype',
'OTHDIA',
'ADHD_subtype2',
'sibling_control',
'sibling_ADHDsibDOB',
'sibling_yrADHDsibdx',
'parent_control',
'parent_ADHDchildDOB',
'parent_yrADHDchilddx',
'Sex',
'Gender',
'DOB',
'Age',
'EDUyrs',
'HAN',
'STAI_State_Total',
'STAI_Trait_Total',
'CAARS_ADHDindex',
'CAARS_HyperImpDSM4',
'CAARS_HyperRest',
'CAARS_ImpEmot',
'CAARS_InattnDSM4',
'CAARS_InattnMem',
'CAARS_Selfconcept',
'CAARS_SymptomDSM4_total',
] #set columns to filter

df = data[columns] #subset the dataset

#filtered = df.dropna(axis=0, how='any')

df.to_csv('filtered_hanni.csv')
#save the file
