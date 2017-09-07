"""
Created on Wed Feb 22 16:01:19 2017

@author: alenia
"""

import pandas as pd
import os
import Syntax as sx


path=os.path.join('CSV','qualtrics_UG.csv')



def read_data():
    data=pd.read_csv(path,sep=',',index_col='ID')
    data.drop('UG\n\n\nParticipant ID (Filled in by experimenter)',inplace=True)
    data.drop('1234567890',inplace=True)
    data.drop('test',inplace=True)
    data.drop('1234',inplace=True)
    data.drop(['ID - Topics'],inplace=True,axis=1)
    data.drop('tst',inplace=True)        
    data.drop('{"ImportId":"QID455_TEXT"}',inplace=True)
    data = data[pd.notnull(data.index)]
    data.index=data.index.str.upper()
    data.drop(['RL061016S','RL031116S','CSS1_S_AS211116'],inplace=True)
    data=data.drop(data.columns[0:16],axis=1)
    data=data[~data.index.duplicated(keep='last')]
    data=rename_cols(data)

    return data



def process_df(df):
    reader = sx.DataReader()
    reader.SSS(df)
    reader.gender_qualtrics(df)  
    reader.age_qualtrics(df)
    reader.define_sss_subset(df)
    reader.define_bis_subset(df)
    reader.rename_bis(df)  
    reader.define_ftnd(df)
    reader.define_kirby_qualtrics(df)

    return df

    
    

def get_dataframe():    
    df=read_data()
    qualtrics_ug=process_df(df)
    qualtrics_ug.iloc[:,2:]=qualtrics_ug.iloc[:,2:].apply(pd.to_numeric)
    qualtrics_ug.index = qualtrics_ug.index.rename('case_id')
    qualtrics_ug.LifetimeSmoking.replace({7:4,4:5,5:6,6:7},inplace=True)
        

    qualtrics_ug = qualtrics_ug.reset_index()
    qualtrics_ug = qualtrics_ug[qualtrics_ug.case_id.str[:2]!='JS']
    qualtrics_ug.set_index('case_id',inplace=True)
    qualtrics_ug['Study'] = 'UG'
    return qualtrics_ug


def save_df():
    df = get_dataframe()
    df.to_csv('PROCESSED/qualtrics_UG_pandas.csv')
    return None



def rename_cols(df):
    
    l = ['12mts_exp_'+str(i) for i in range(1,11)]
    k = ['Alcohol_12mts_exp_'+str(i) for i in range(1,11)]
    col1 = dict(zip(l,k))
    
    l = ['30_days_'+str(i) for i in range(1,6)]
    l.append('30days_5+')
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
    df.rename(columns={'Past month':'Past_month_smoke'},inplace=True)

    return df







      
        