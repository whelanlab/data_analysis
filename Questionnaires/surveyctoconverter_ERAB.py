# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:01:19 2017

@author: alenia
"""

import pandas as pd
import Syntax as sx
import os


PREEEG=os.path.join('CSV','PRE_EEG_ERAB_SURVEYCTO_FINALVERSION_WIDE.csv')
POSTEEG=os.path.join('CSV','POST_EEG_ERAB_SURVEYCTO_WIDE.csv')
FIRSTBATCH=os.path.join('CSV','erab_first_batch.csv')





def read_data_firstbatch():
    data=pd.read_csv(FIRSTBATCH,sep=',',na_values=[' '])
    data=data[pd.notnull(data.index)]
#    data.rename(columns={'Subject_ID': 'case_id'},inplace=True)
    data = data.set_index('case_id')     
    data = data.drop('deviceid')
    data.index=data.index.str.upper()    
    data = rename_cols(data)
    return data




def process_dataset(data):
    reader = sx.DataReader()
    reader.gender_erab(data)
    reader.define_audit_ERAB(data)
    reader.define_smoke30days(data)
    reader.define_bis_subset(data)
    reader.rename_bis(data)
    reader.MX_erab(data)
    reader.define_ever_smoke_erab(data)
    reader.define_personality_dis(data)
    reader.define_dsm_iv(data)
    reader.define_dangerousness_scale(data)
    reader.define_eating_disorder(data)
    reader.denial(data)
    reader.define_zscores(data)
    reader.define_tscores(data)
    reader.define_DASS_ERAB(data)
    reader.define_dast_erab(data)
    reader.define_MAAS(data)
    reader.define_pss_erab(data)
    reader.define_tci(data)
    reader.define_neo_erab(data)
    reader.define_ftnd(data)
    reader.define_AEQ(data)
    reader.bf(data)
    reader.Tbf(data)
    return data


def get_dataframe():

    df = read_data_firstbatch()
    df['Study'] = 'ERAB'
    surveycto_erab=process_dataset(df)
    surveycto_erab = surveycto_erab.loc[surveycto_erab['LOGFILE NAME'].str[0:2]!='NO'] 
    return surveycto_erab


def save_df():
    df = get_dataframe()
    df.to_csv('PROCESSED/surveycto_ERAB_pandas.csv')
    return None


def rename_cols(df):
    df.rename(columns={'Chain_smoke':'Chain_smoke_freq'}, inplace=True)
    df.rename(columns={'NOTES_caseid': 'Comments'},inplace=True)
    df.rename(columns={'YearsOfEducation':'EDUyrs'}, inplace=True)
    df.rename(columns={'Monthly_income':'Mntincome'}, inplace=True)
    df.rename(columns={'Freq_Func_smoke':'Freq_Smoke_Func'},inplace=True)
    df.rename(columns={'Marital_status':'MAR_ERAB'},inplace=True)  
    df['Team_sports'].replace({1:True,0:False},inplace=True)    
    df['Sports_Frequency'].replace({6:5},inplace=True)
    df.rename(columns={'Religious_Practice':'Rel_Practice'},inplace=True)   
    return df



#d1=get_dataframe(reader)
#f1 = open('d1_index.txt', 'w')
#f2 = open('d2_index.txt', 'w')
#
#a=d1.index.tolist()
#b=d2.index.tolist()
#
#for item in a:
#    print>>f1,item
#    
#for item in b:
#   print>>f2,item




#OLD 



#
#def read_data():
#    d1=pd.read_csv(PREEEG,sep=',',index_col='Subject_ID')
#    d2=pd.read_csv(POSTEEG,sep=',',index_col='Subject_ID')
#    d1.index=d1.index.map(str.strip)
#    d2.index=d2.index.map(str.strip)
#    d2.index=d2.index.str.rstrip('...')
#    d1.drop('TESTERLOH',inplace=True)
#    d2=drop_duplicated_index(d2,19,'ERAB_S1_LOH_241116')
#    d2=drop_index(d2,6)    
#    d1,d2=rename_index(d1,d2)
#    d1 = d1.drop(d1.columns[-3:],axis=1)    
#    d2 = d2.drop(d2.columns[-3:],axis=1)                      
#    d1 = d1.drop(d1.columns[0:10],axis=1)    
#    d2 = d2.drop(d2.columns[0:10],axis=1)   
#    d1=d1[pd.notnull(d1.index)]
#    d1.index=d1.index.str.upper()
#    d2.index=d2.index.str.upper()
#
#        
#    d2=d2[pd.notnull(d2.index)]        
#    data= pd.merge(d1,d2,left_index=True,right_index=True)
#    return d1,d2,data
#
#def reindex(df,old,new):
#    as_list = df.index.tolist()
#    idx = as_list.index(old)
#    as_list[idx] = new
#    df.index = as_list
#    return df
#
#
#def rename_index(d1,d2):
#    d1=reindex(d1,'Caroline Dawson','ERAB_S1_LOH081216AFTERNOON')
#    d2=reindex(d2,'ERAB_S1_AS141116_AFTERNOON','ERAB_S1_AS141116AFTERNOON')
#    d2=reindex(d2,'Darragh Bree','ERAB_S1_LOH_0512MORNING')
#    d2=reindex(d2,'Caroline Dawson','ERAB_S1_LOH081216AFTERNOON')
#    d2=reindex(d2,'16325218','ERAB_S1_LOH_151116')
#    d2=reindex(d2,'16318463','ERAB_S2_LOH061216AFTERNOON')
#    d2=reindex(d2,'ERAB_S3_LOH_171116','ERAB_S3_LOH_181116')
#    return d1,d2
#
#
#def drop_duplicated_index(data,idx,new_value):
#    data.reset_index(inplace=True)
#    data.iloc[idx,0]=new_value
#    data=data.set_index('index')
#    return data
#
#def drop_index(data,idx):
#    data.reset_index(inplace=True)
#    data.drop(idx,inplace=True)
#    data=data.set_index('index')
#    return data
#    
#def process_dataset(data,reader):
#    data=reader.define_audit(data)
#    data=reader.define_bis_subset(data)
#    
#    return data





['ERAB_S1_JF_150217',
 'ERAB_S1_JF_150217A',
 'ERAB_S1_JF_200217',
 'ERAB_S1_JF_030317A']


