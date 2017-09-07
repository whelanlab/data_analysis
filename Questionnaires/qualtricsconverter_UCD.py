# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:42:24 2017

@author: alenia
"""

"""
Created on Wed Feb 22 16:01:19 2017

@author: alenia
"""

import pandas as pd
import Syntax as sx
import os

path=os.path.join('CSV','qualtrics_UCD.csv')

def read_data():
    data=pd.read_csv(path,sep=',',header=0,skiprows=[1,2],index_col='ID')
    data.index=data.index.str.upper()
    data.index = data.index.rename('case_id')
    data=data.drop(data.columns[0:7],axis=1)
    data=data.drop(data.columns[-1],axis=1)
    data=data[pd.notnull(data.index)]
    data=rename_cols(data)
    return data


def process_df(df):
    reader = sx.DataReader()   
    reader.age_qualtrics(df)
    reader.gender_qualtrics(df)
    reader.define_smoke30days(df)
    reader.define_audit_UCD(df)
    reader.define_dast_UCD(df)
    reader.define_DASS42(df)
    reader.define_ftnd(df)
    reader.rename_CPNI_UCD(df)
    reader.define_personality_dis(df)
    reader.define_dsm_iv(df)
    reader.define_eating_disorder(df)
    reader.define_dangerousness_scale(df)
    reader.denial(df)
    reader.define_zscores(df)
    reader.define_tscores(df)
    reader.define_pss_erab(df)
    reader.define_bis_subset(df)
    reader.rename_bis(df) 
    reader.MX_UCD(df)
    reader.bf(df) 
    reader.Tbf(df)
    reader.define_tci_UCD(df)
    reader.rename_neo_UCD(df)
    reader.define_neo_erab(df)  
    return df


def get_dataframe():
    df=read_data()
    df['Study'] = pd.Series(['UCD' for x in range(len(df.index))],index=df.index)    
    qualtrics_ucd=process_df(df)
    return qualtrics_ucd
    

def save_df():
    a=get_dataframe()
    a.to_csv('PROCESSED/qualtrics_UCD_pandas.csv')
    return None


def rename_cols(df):
    df.rename(columns={'Chain-sm':'Chain_smoke_freq'}, inplace=True)
    df.rename(columns={'Inc.':'Mntincome'},inplace=True)
    df.rename(columns={'Intend':'Intend_Smoke'},inplace=True)
    df.rename(columns={'Freq/ func':'Freq_Smoke_Func'},inplace=True)
    df.rename(columns={'Trips':'Trips_Smoke'},inplace=True)
    df.rename(columns={'30 days':'smoke_last30days'},inplace=True) #change name and then launch the same script as ERAB  
    df.rename(columns={'MAR':'MAR_UCD'},inplace=True)  
    df['ever-smoke'].replace({1:True,2:False}, inplace=True)
    df.rename(columns={'ever-smoke':'Tried_cig'},inplace=True)
    df.rename(columns={'Exer.':'Sports_Frequency'},inplace=True)
    df['Sports'].replace({1:True,2:False},inplace=True)    
    df.rename(columns={'Sports':'Team_sports'},inplace=True)
    df.rename(columns={'Religious':'Religious_Identity'},inplace=True)
    df.rename(columns={'rel. freq.':'Rel_Practice'},inplace=True)
    df['Smoker'].replace({1:'Smoker',2:'Non Smoker'},inplace=True)
    df.rename(columns={'Smoker':'Smoker_Non_smoker'},inplace=True)
    return df







      
        