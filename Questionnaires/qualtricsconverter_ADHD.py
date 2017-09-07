"""
Created on Wed Feb 22 16:01:19 2017

@author: alenia
"""
import os
import pandas as pd
import Syntax as sx
import numpy as np


path = os.path.join('CSV', 'qualtrics_ADHD_IUSandLEQ.csv')
pathKG = os.path.join('CSV', 'qualtrics_KG_ADHD.xlsx')



def read_data():
    data = pd.read_csv(path,sep=',',header=0,skiprows=[1,2])
    data = data.drop(data.columns[0:5],axis=1)
    data = data.drop(data.columns[1:11],axis=1)
    data = data.drop(data.columns[-1],axis=1)
    data['matchingcode'] = data.CODE_1 + data.CODE_2 + data.CODE_3 + data.CODE_4.astype(str) + data.CODE_5
    data.drop(['CODE_1','CODE_2','CODE_3','CODE_4','CODE_5'], 1, inplace=True)
    data['MED'].replace('n/a',np.nan,inplace=True)
    data = data.set_index('case_id')
    data.index = data.index.str.upper()
    data['Study'] = 'ADHD_qualtrics'
    return data



def process_df(df):
    reader = sx.DataReader()   
    reader.han_qualtrics_adhd(df)
    reader.define_DIA_adhd(df)
    reader.maritalstatus_qualtrics_adhd(df)
    reader.gender_qualtrics_adhd(df)
    reader.define_tci(df)
    reader.define_STAI_qualtrics(df)
    reader.define_neo_erab(df)
    reader.define_CAARS_qualtrics(df)
    return df


    
def get_KG_df():
    data = pd.read_excel(pathKG,header=0)
    data['matchingcode'] = data.CODE1+data.CODE2+data.CODE3+data.CODE4.astype(str)+data.CODE5
    data.drop(['CODE1', 'CODE2', 'CODE3', 'CODE4', 'CODE5'], 1, inplace=True)
    data['MED'].replace('n/a',np.nan,inplace=True)
    data.replace(-999,np.nan,inplace=True)
    data = data.set_index('case_id')
    data['Study'] = 'ADHD_qualtrics'
    data.index = data.index.str.upper()
    reader = sx.DataReader()  
    reader.define_DIA_adhd(data)
    reader.maritalstatus_qualtrics_adhd(data)
    reader.gender_qualtrics_adhd(data)
    reader.define_STAI(data)
    reader.define_CAARS(data)
    return data


def get_dataframe():
    df=read_data()
    qualtrics_adhd = process_df(df)
    kg_qualtrics = get_KG_df()
    frames = [qualtrics_adhd, kg_qualtrics]
    qualtrics = pd.concat(frames)
    qualtrics = rename_cols(qualtrics)
    return qualtrics



def save_df():
    a=get_dataframe()
    a.to_csv('PROCESSED/qualtrics_ADHD_pandas.csv')
    return None


def rename_cols(df):
    df.rename(columns = {'EDU':'EDUyrs'}, inplace=True)
    df.rename(columns = {'AGE':'Age'}, inplace=True)
    df.rename(columns = {'INC':'Mntincome'}, inplace=True)
    df.rename(columns = {'MED':'CurrentMedication'}, inplace=True)
    df.rename(columns = {'OCC':'Occupation'}, inplace=True)
    df.rename(columns = {'MAR':'MAR_ADHD'}, inplace=True)  
    return df  