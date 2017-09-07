# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:45:37 2017

@author: alenia
"""


import os
import pandas as pd
import numpy as np
import surveyctoconverter_ERAB as ERAB
import surveyctoconverter_ADHD as SADHD
import qualtricsconverter_UG as UG
import qualtricsconverter_ADHD as QADHD
import surveyctoconverter_UG as SUG
import qualtricsconverter_UCD as UCD
import Syntax as sx
import merge_log
from collections import Counter


reader = sx.DataReader()


def read_data():
    
    surveycto_erab = ERAB.get_dataframe()
    qualtrics_ug = UG.get_dataframe()
    adhd = ahdh_pen_paper()
    surveycto_UG = SUG.get_dataframe()
    qualtrics_UCD = UCD.get_dataframe()
    frames = [surveycto_erab,qualtrics_ug,adhd,surveycto_UG,qualtrics_UCD]
    df = pd.concat(frames)
#    df.index=df.index.map(str.strip)
    df.reset_index(inplace=True)
    
    return df



#a = surveycto_erab.columns.tolist()
#b = qualtrics_ug.columns.tolist()
#c = set(a) & set(b)
#c = Counter(b)

def merge_data(): #CALL ME!
    df = read_data()
    log = merge_log.read_log()
    data = pd.merge(df,log,on='case_id',how='outer')
    data.set_index('case_id',inplace=True)
    data = remove_variables(data)
    reader.define_marital_status(data)
    reader.define_smoking_type(data)
    return data


def write_data():
    data = merge_data()
    data.to_csv('data.csv')
    return None


def notmerged():
    data = merge_data()
    notmerged = list(data.index[np.logical_or(data.Study.isnull(),data.Log.isnull())])
    notmerged.sort()
    thefile = open('not merged indexes.txt', 'w')
    thefile.writelines(["%s\n" % item  for item in notmerged])
    thefile.close()
    a = data.loc[notmerged]
    a[['Study','Log']].to_csv('not merged with type.csv')



def saveindex():
    qs = read_data()
    log = merge_log.read_log()
    notmerged()
    qsind = qs.case_id.tolist()
    qsind.sort()
    logind = log.case_id.tolist()
    logind.sort()
    thefile = open('index surveys.txt', 'w')
    thefile.writelines(["%s\n" % item  for item in qsind])
    thefile.close()
    thefile = open('index log files.txt', 'w')
    thefile.writelines(["%s\n" % item  for item in logind])
    thefile.close()
    return None


def check_merged(qs):
    log = merge_log.read_log()
    log.set_index('case_id',inplace=True)
    a = qs.index.tolist()
    b = log.index.tolist()
    return len(set(a)& set(b))
    

def save_variables_name(df,name):
    names = {'erab':'surveyctoerab variable list.txt',
             'qadhd':'qualtrics adhd variable list.txt',
             'sadhd':'surveyctoadhd variable list.txt',
             'qug':'qualtrics ug variable list.txt',
             'sug':'surveycto xsec variable list.txt',
             'qucd':'qualtrics ucd variable list.txt'}
    
    df.dropna(axis=1, how='all',inplace=True)
    aslist = df.columns.tolist()
    aslist.sort()
    fname = names[name] 
    thefile = open(fname, 'w')
    thefile.writelines(["%s\n" % item  for item in aslist])
    thefile.close()
    
    
def remove_variables(df):
    toremove = ['Comments','CON_1','CON_2','CON_3','CON_4','CON_5',\
                'CON_6','GROUP','First_labels','Exer._6_TEXT','BIS11_labels',
                'rel. freq._6_TEXT','HANDstr','Acad._6_TEXT','GROUP_comb',\
                'HANDstr','MARtxt','Marj_labels','Religious_6_TEXT','alc_hist','alc_typ',\
                'drugs_labels','likely_labels','last12_exp_labels','can_freq_labels',
                'pub_alc_typ','pur_alc_typ','smok_hist','rel. freq._6_TEXT','matchingcode']
    
    df.drop(toremove,inplace=True,axis=1)
    df['ETH'] = df['ETH'].str.lower()
    return df 


def ahdh_pen_paper():
    path = os.path.join('CSV', 'adhd_penpaper.csv')
    penpaper = pd.read_csv(path)
    penpaper.rename(columns={'Participant Code':'case_id'},inplace=True)
    penpaper=penpaper.drop(penpaper.columns[1:3],axis=1)
    penpaper=penpaper.drop(penpaper.columns[-3:],axis=1)
    qualtrics_adhd = QADHD.get_dataframe()
    surveycto_adhd = SADHD.get_dataframe()
    frames = [qualtrics_adhd,surveycto_adhd]
    df=pd.concat(frames)
    df.reset_index(inplace=True)
    data=pd.merge(df,penpaper,on='case_id',how='outer')
    data.set_index('case_id',inplace=True)
    return data