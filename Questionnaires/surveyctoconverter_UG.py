# -*- coding: utf-8 -*-
"""
Created on Mon May 22 12:59:34 2017

@author: alenia
"""

import pandas as pd
import Syntax as sx
import os

path= os.path.join('CSV','surveycto_UG_firstbatch.csv')


def read_data():
    data = pd.read_csv(path)
    data.rename(columns={'ID':'case_id'}, inplace=True)
    data = data.set_index('case_id')
    data.index=data.index.str.upper()
    data = data.drop(data.columns[0:11],axis=1)
    data = data.drop(data.columns[-3:],axis=1)
    data = rename_cols(data)
    return data


def process_df(df):
    reader = sx.DataReader()    
    reader.age_qualtrics(df)
    reader.gender_surveyctocross(df)
    reader.SSS_surveycto(df)
    reader.define_sss_subset(df)
    reader.define_bis_subset_survey(df)        
    reader.rename_bis(df)
    reader.define_ftcd(df)
    reader.define_ftnd(df)
    reader.define_kirby_crosssect(df)
    reader.define_type_cross(df)
    return df





def get_dataframe():
    df=read_data()
    surveycto_ug=process_df(df)
#    as_list = surveycto_ug.index.tolist()
#    for i,j in enumerate(as_list):
#        if j=='BM260916M':
#            if surveycto_ug.iloc[i][0] == 'M' :
#                as_list[i]='BM260916M2'
#    surveycto_ug.index = as_list
#    surveycto_ug.index.name = 'case_id'
    return surveycto_ug
    

def save_df():
    a=get_dataframe()
    a.to_csv('PROCESSED/surveycto_xsect_pandas.csv')
    return None


def rename_cols(df):
    
    l = ['A12mts_exp_'+str(i) for i in range(1,11)]
    k = ['Alcohol_12mts_exp_'+str(i) for i in range(1,11)]
    col1 = dict(zip(l,k))
    
    l = ['A30_days_'+str(i) for i in range(1,6)]
    l.append('A30days_5_')
    k = ['Alcohol30_days_'+str(i) for i in range(1,6)]
    k.append('Alcohol30_days_5+')
    col2 = dict(zip(l,k))
    
    l = ['Likely_ '+str(i) for i in range(1,11)]
    k = ['Likely_Alcohol_'+str(i) for i in range(1,11)]
    col3 = dict(zip(l,k))     
    
    df.rename(columns=col1, inplace=True)
    df.rename(columns=col2, inplace=True)
    df.rename(columns=col3, inplace=True)

    df.rename(columns={'Life':'LifetimeSmoking'}, inplace=True)
    df.rename(columns={'Past_month':'Past_month_smoke'},inplace=True)
    return df


        