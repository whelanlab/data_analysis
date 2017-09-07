# -*- coding: utf-8 -*-
"""
Created on Wed May 03 12:02:51 2017

@author: alenia
"""

"""
Created on Wed Feb 22 16:01:19 2017

@author: alenia
"""

import pandas as pd
import Syntax as sx
import numpy as np
import os 


oldpath=os.path.join('CSV','ADHD_surveyCTO_1stbatch_DATA.xlsx')
newpath=os.path.join('CSV','surveycto_ADHD.csv')


def read_data():
    d1=pd.read_excel(oldpath)
    d2=pd.read_csv(newpath)
    d2=d2.drop(d2.columns[-3:],axis=1)
    d2.rename(columns={'EDUyrs':'EDU'}, inplace=True)
#    d2.drop(['EDUtxt'], 1,inplace=True)

    d1['code'] = d1.CODE_1_TEXT + d1.CODE_TEXT_2 + d1.CODE_TEXT_3 + d1.CODE_TEXT_4.astype(str)+d1.CODE_TEXT_5
    d2['code'] = d2.CODE_1_TEXT + d2.CODE_TEXT_2 + d2.CODE_TEXT_3 + d2.CODE_TEXT_4.astype(str)+d2.CODE_TEXT_5
    d2 = define_HEI_WEI(d2)
    d2 = change_names(d2)
    a = d2.columns.tolist()
    frames = [d1,d2]
    data = pd.concat(frames)
    data = data[a] #concat takes the dictionary keys, i have to rearrrenge those
    data.drop(['CODE_1_TEXT','CODE_TEXT_2','CODE_TEXT_3','CODE_TEXT_4','CODE_TEXT_5'], 1,inplace=True)
    data.rename(columns={'caseid':'case_id'}, inplace=True)
    data.rename(columns={'EDUyrs':'EDU'}, inplace=True)
    data=data.set_index('case_id')
    data['MED'].replace('n/a',np.nan,inplace=True)
    data.code = data.code.str.upper()
    data.index=data.index.str.upper()
    data=data.drop(data.columns[0:9],axis=1)
    data=rename_cols(data)
    return data


def process_df(df):
    reader = sx.DataReader()    
    reader.gender_surveycto_adhd(df)
    reader.define_marital_adhd(df)
    reader.define_control_adhd(df)
    reader.define_DIA_adhd(df)
    reader.define_type_adhd(df)
    reader.define_WURS(df)
    reader.define_tci(df)
    reader.define_STAI(df)
    reader.define_neo_erab(df)
    reader.define_bis_subset_adhd(df)
    reader.define_CAARS(df)
    reader.define_MASC(df)
    return df



def define_HEI_WEI(data):
    data['HEI']=np.where(data['HEI_respoptions'] == 1,(data['HEIft']*12 + data['HEIinch'])*2.54,data['HEIcm'])
    data['WEI']=np.where(data['WEI_storkg'] == 1,(data['WEIst']*14 + data['WEIlb'])*0.4535,data['WEIkg'])
    data.drop(['WEIkg','WEIlb','WEIst','HEIft','HEIinch','HEIcm','WEI_storkg','HEI_respoptions'], 1,inplace=True)
    data.HEI = data.HEI.round()
    data.WEI = data.WEI.round()    
    return data



def change_names(data):
       
    hashtable = {'48_180517':'ADHD1_AS_170517C','49_010617c':'ADHD1_LR_020617C',\
                 '53_060617c':'ADHDONLYFMRI_53_060617c','50_020617c':'ADHD2_LR_010617C',\
                 '49_310517c':'ADHD1_AS_160617C','55_070617c':'ADHD1_LR_060617C',\
                 'ADHD1_AS_090617C':'ADHD1_AS_090617S','ADHD1_LR_150117P':'ADHD1_LR_150617P',\
                 'ADHD_LR_050417P':'ADHD2_LR_050417P','ADHD_AS_050417A':'ADHD1_AS_050417A',
                 'ADHD2_LR_040817P' : 'ADHD2_LR_040817S','191216A':'ADHD1_AS_191216A'}
    data['caseid'].replace(hashtable,inplace=True)        
    data.loc[(data['code']=='INSEP2000M'),'caseid'] = 'ADHD1_AS_300517C'
    data.loc[(data['code']=='onapr1997b'),'caseid'] = 'ADHD1_LR_290617A'    
    data.loc[(data['code']=='hdfeb1966m'),'caseid'] = 'ADHD1_AS_140817C'    
    return data


def get_dataframe():
    df=read_data()
    df['Study'] = pd.Series(['ADHD_surveycto' for x in range(len(df.index))],index=df.index)    
    surveycto_adhd=process_df(df)
    return surveycto_adhd
    

def save_df():
    a=get_dataframe()
    a.to_csv('PROCESSED/surveycto_ADHD_pandas.csv')
    return None


def rename_cols(df):
    df.rename(columns={'AGE':'Age'},inplace=True)
    df.rename(columns={'EDU':'EDUyrs'},inplace=True)
    df.rename(columns={'INC':'Mntincome'},inplace=True)
    df.rename(columns={'MED':'CurrentMedication'},inplace=True)
    df.rename(columns={'OCC':'Occupation'},inplace=True)
    df.rename(columns={'MAR':'MAR_ADHD'},inplace=True)  
    return df