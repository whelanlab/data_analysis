# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 11:49:12 2017

@author: alenia
"""
from __future__ import division
import re
import pandas as pd
import numpy as np
import itertools as it
class DataReader:

    def SSS(self,data):
        data.rename(columns={'Q44': 'sss1', 'Q46': 'sss3', 'Q50': 'sss5', 'Q48': 'sss6',
                             'Q51': 'sss8', 'Q52': 'sss9', 'Q58': 'sss14', 'Q60': 'sss16',
                             'Q61': 'sss17', 'Q62': 'sss18', 'Q66': 'sss22', 'Q67': 'sss23',
                             'Q68': 'sss24', 'Q72': 'sss28', 'Q73': 'sss29', 'Q76': 'sss32',
                             'Q78': 'sss34', 'Q80': 'sss36', 'Q83': 'sss39',


                             'Q45': 'sss2', 'Q47': 'sss4', 'Q49': 'sss7', 'Q53': 'sss10',
                             'Q55': 'sss11','Q56': 'sss12', 'Q57': 'sss13', 'Q59': 'sss15',
                             'Q63': 'sss19','Q64': 'sss20', 'Q65': 'sss21', 'Q69': 'sss25',
                             'Q70': 'sss26','Q71': 'sss27', 'Q74': 'sss30', 'Q75': 'sss31',
                             'Q77': 'sss33','Q79': 'sss35', 'Q81': 'sss37', 'Q82': 'sss38',
                             'Q84': 'sss40',

                             }, inplace=True)

        y={}
        for i in range(1,41):
            y[i]='sss'+str(i)
        col_names=y


        columns1={'Q44': 'sss1', 'Q46': 'sss3', 'Q50': 'sss5', 'Q48': 'sss6',
                  'Q51': 'sss8', 'Q52': 'sss9', 'Q58': 'sss14', 'Q60': 'sss16',
                  'Q61': 'sss17', 'Q62': 'sss18', 'Q66': 'sss22', 'Q67': 'sss23',
                  'Q68': 'sss24', 'Q72': 'sss28', 'Q73': 'sss29', 'Q76': 'sss32',
                  'Q78': 'sss34', 'Q80': 'sss36', 'Q83': 'sss39'}


        columns2={'Q45': 'sss2', 'Q47': 'sss4', 'Q49': 'sss7', 'Q53': 'sss10',
                  'Q55': 'sss11','Q56': 'sss12', 'Q57': 'sss13', 'Q59': 'sss15',
                  'Q63': 'sss19','Q64': 'sss20', 'Q65': 'sss21', 'Q69': 'sss25',
                  'Q70': 'sss26','Q71': 'sss27', 'Q74': 'sss30', 'Q75': 'sss31',
                  'Q77': 'sss33','Q79': 'sss35', 'Q81': 'sss37', 'Q82': 'sss38',
                  'Q84': 'sss40'}


        columns1=list(columns1.viewvalues())
        columns2=list(columns2.viewvalues())


        for i in range(len(columns1)):
            
            data[columns1[i]].replace('2','0',inplace=True)
            data[columns1[i]]=data[columns1[i]].apply(pd.to_numeric)

        for i in range(len(columns2)):
            HashTable = {'1' : '0', '2' : '1'}
            data[columns2[i]].replace(HashTable,inplace=True)
            data[columns2[i]]=data[columns2[i]].apply(pd.to_numeric)


        col_names = list(col_names.values())
        data['SSS_TOTAL']=data[col_names].sum(axis=1)

        return data
    
    
    
    def SSS_surveycto(self,data):
        data.rename(columns={'Q44': 'sss1', 'Q46': 'sss3', 'Q50': 'sss5', 'Q48': 'sss6',
                             'Q51': 'sss8', 'Q52': 'sss9', 'Q58': 'sss14', 'Q60': 'sss16',
                             'Q61': 'sss17', 'Q62': 'sss18', 'Q66': 'sss22', 'Q67': 'sss23',
                             'Q68': 'sss24', 'Q72': 'sss28', 'Q73': 'sss29', 'Q76': 'sss32',
                             'Q78': 'sss34', 'Q80': 'sss36', 'Q83': 'sss39',


                             'Q45': 'sss2', 'Q47': 'sss4', 'Q49': 'sss7', 'Q53': 'sss10',
                             'Q55': 'sss11','Q56': 'sss12', 'Q57': 'sss13', 'Q59': 'sss15',
                             'Q63': 'sss19','Q64': 'sss20', 'Q65': 'sss21', 'Q69': 'sss25',
                             'Q70': 'sss26','Q71': 'sss27', 'Q74': 'sss30', 'Q75': 'sss31',
                             'Q77': 'sss33','Q79': 'sss35', 'Q81': 'sss37', 'Q82': 'sss38',
                             'Q84': 'sss40',

                             }, inplace=True)

        y={}
        for i in range(1,41):
            y[i]='sss'+str(i)
        col_names=y


        columns1={'Q44': 'sss1', 'Q46': 'sss3', 'Q50': 'sss5', 'Q48': 'sss6',
                  'Q51': 'sss8', 'Q52': 'sss9', 'Q58': 'sss14', 'Q60': 'sss16',
                  'Q61': 'sss17', 'Q62': 'sss18', 'Q66': 'sss22', 'Q67': 'sss23',
                  'Q68': 'sss24', 'Q72': 'sss28', 'Q73': 'sss29', 'Q76': 'sss32',
                  'Q78': 'sss34', 'Q80': 'sss36', 'Q83': 'sss39'}


        columns2={'Q45': 'sss2', 'Q47': 'sss4', 'Q49': 'sss7', 'Q53': 'sss10',
                  'Q55': 'sss11','Q56': 'sss12', 'Q57': 'sss13', 'Q59': 'sss15',
                  'Q63': 'sss19','Q64': 'sss20', 'Q65': 'sss21', 'Q69': 'sss25',
                  'Q70': 'sss26','Q71': 'sss27', 'Q74': 'sss30', 'Q75': 'sss31',
                  'Q77': 'sss33','Q79': 'sss35', 'Q81': 'sss37', 'Q82': 'sss38',
                  'Q84': 'sss40'}


        columns1=list(columns1.viewvalues())
        columns2=list(columns2.viewvalues())


        for i in range(len(columns1)):
            
            data[columns1[i]].replace(2,0,inplace=True)

        for i in range(len(columns2)):
            HashTable = {1:0,2:1}
            data[columns2[i]].replace(HashTable,inplace=True)


        col_names = list(col_names.values())
        data['SSS_TOTAL']=data[col_names].sum(axis=1)



        return data    
    


    def define_sss_subset(self,data):

        data['SSS_boredom_susceptibility']= data['sss2']+ data['sss5'] + data['sss7']+data['sss8'] + \
                                            data['sss15']+data['sss24'] + data['sss27']+data['sss31'] + \
                                            data['sss34'] + data['sss39']

        data['SSS_disinhibition']= data['sss1']+ data['sss12'] + data['sss13']+data['sss25'] + \
                                   data['sss29']+data['sss30'] + data['sss32']+data['sss33'] + \
                                   data['sss35'] + data['sss36']

        data['SSS_experience_seeking']= data['sss4']+ data['sss6'] + data['sss9']+data['sss10'] + \
                                        data['sss14']+data['sss18'] + data['sss19']+data['sss22'] + \
                                        data['sss26'] + data['sss37']

        data['SSS_adventure_seeking']= data['sss3']+ data['sss11'] + data['sss16']+data['sss17'] + \
                                       data['sss20']+data['sss21'] + data['sss23']+data['sss28'] + \
                                       data['sss38'] + data['sss40']
        return data










    def han_qualtrics_adhd(self,data):
        col='HAN'
        data[col]=data[col].str.upper()
        hashtable = {'RIGHT':1,'LEFT':2,'RIGHT-HANDED':1,'LEFT-HANDED':2,'RIGHT HANDED':1,
                     'OTHER':3}        
        data[col].replace(hashtable,inplace=True)
        return data


    def maritalstatus_qualtrics_adhd(self,data):
        col = 'MAR'
        data[col]=data[col].str.lower()
        hashtable = {'single':1,'in a relationship':2,'married':3}          
        data[col].replace(hashtable,inplace=True)
        
        status={1:'single',2:'in a relationship',3:'married',4:'separated',5:'divorced',6:'widowed'}
        data['MARtxt'] = data['MAR'].map(status)
        return data




    def rename_bis(self,data):
        old = ['BIS11_'+str(i) for i in range(1,30)]
        new = ['BIS_'+str(i) for i in range(1,30)]
        col1=dict(zip(old,new))
        
        bis_columns={'BIS11_9': 'BIS11_9R', 'BIS11_20': 'BIS11_20R', 'BIS11_30': 'BIS11_30R',
                      'BIS11_1': 'BIS11_1R','BIS11_7': 'BIS11_7R', 'BIS11_8': 'BIS11_8R',
                      'BIS11_12': 'BIS11_12R', 'BIS11_13': 'BIS11_13R','BIS11_10': 'BIS11_10R',
                      'BIS11_15': 'BIS11_15R','BIS11_29': 'BIS11_29R'}


        old = list(bis_columns.viewvalues())       
        new = [s.replace('11','') for s in old]
        col2 = dict(zip(old,new))

        
        data.rename(columns=col1,inplace=True)
        data.rename(columns=col2,inplace=True)        
        
        return data




    def define_bis_subset_adhd(self,data):

        data.rename(columns={'BIS_9': 'BIS_9R', 'BIS_20': 'BIS_20R', 'BIS_30': 'BIS_30R',
                             'BIS_1': 'BIS_1R','BIS_7': 'BIS_7R', 'BIS_8': 'BIS_8R',
                             'BIS_12': 'BIS_12R', 'BIS_13': 'BIS_13R','BIS_10': 'BIS_10R',
                             'BIS_15': 'BIS_15R','BIS_29': 'BIS_29R'}, inplace=True)



        bis_columns={'BIS_9': 'BIS_9R', 'BIS_20': 'BIS_20R', 'BIS_30': 'BIS_30R',
                      'BIS_1': 'BIS_1R','BIS_7': 'BIS_7R', 'BIS_8': 'BIS_8R',
                      'BIS_12': 'BIS_12R', 'BIS_13': 'BIS_13R','BIS_10': 'BIS_10R',
                      'BIS_15': 'BIS_15R','BIS_29': 'BIS_29R'}


        bis_columns=list(bis_columns.viewvalues())



        for i in range(len(bis_columns)):
            HashTable = {4:1,3:2,2:3,1:4}
            data[bis_columns[i]]=pd.to_numeric(data[bis_columns[i]],errors='coerce')
            data[bis_columns[i]].replace(HashTable,inplace=True)



        a=['BIS_5','BIS_11','BIS_28', 'BIS_6','BIS_24','BIS_26','BIS_2','BIS_3','BIS_4',\
           'BIS_17','BIS_19','BIS_22','BIS_25','BIS_16','BIS_21','BIS_23','BIS_14','BIS_18',\
           'BIS_27']
        bis_columns.extend(a)


        for i in range(len(bis_columns)):
            data[bis_columns[i]]=pd.to_numeric(data[bis_columns[i]],errors='coerce')



        data['BIS_1storder_attention']=data['BIS_5']+data['BIS_9R']+data['BIS_11'] + data['BIS_20R'] +\
                                             data['BIS_28']


        data['BIS_1storder_cog_instab']=data['BIS_6']+data['BIS_24']+data['BIS_26']




        data['BIS_1storder_motor']=data['BIS_2']+data['BIS_3']+data['BIS_4'] + \
                                          data['BIS_17']+data['BIS_19'] + data['BIS_22'] + \
                                          data['BIS_25']



        data['BIS_1storder_perseverance']=data['BIS_16']+data['BIS_21']+data['BIS_23'] + \
                                                data['BIS_30R']


        data['BIS_1storder_self_control']=data['BIS_1R']+data['BIS_7R']+data['BIS_8R'] + \
                                                 data['BIS_12R']+data['BIS_13R'] + data['BIS_14']




        data['BIS_1storder_cog_complex']=data['BIS_10R']+data['BIS_15R']+data['BIS_18'] + \
                                                data['BIS_27']+data['BIS_29R']


        data['BIS_2ndorder_attentional'] = data['BIS_1storder_attention']+data['BIS_1storder_cog_instab']

        data['BIS_2ndorder_motor'] = data['BIS_1storder_motor']+data['BIS_1storder_perseverance']


        data['BIS_2ndorder_nonplanning'] = data['BIS_1storder_self_control']+ \
                                                data['BIS_1storder_cog_complex']

        data['BIS_TOTAL'] = data['BIS_2ndorder_attentional'] + data['BIS_2ndorder_motor'] + \
                                   data['BIS_2ndorder_nonplanning']

        return data
    
    
    
    
    
    
    
    def define_bis_subset(self,data):

        data.rename(columns={'BIS11_9': 'BIS11_9R', 'BIS11_20': 'BIS11_20R', 'BIS11_30': 'BIS11_30R',
                             'BIS11_1': 'BIS11_1R','BIS11_7': 'BIS11_7R', 'BIS11_8': 'BIS11_8R',
                             'BIS11_12': 'BIS11_12R', 'BIS11_13': 'BIS11_13R','BIS11_10': 'BIS11_10R',
                             'BIS11_15': 'BIS11_15R','BIS11_29': 'BIS11_29R'}, inplace=True)



        bis_columns={'BIS11_9': 'BIS11_9R', 'BIS11_20': 'BIS11_20R', 'BIS11_30': 'BIS11_30R',
                      'BIS11_1': 'BIS11_1R','BIS11_7': 'BIS11_7R', 'BIS11_8': 'BIS11_8R',
                      'BIS11_12': 'BIS11_12R', 'BIS11_13': 'BIS11_13R','BIS11_10': 'BIS11_10R',
                      'BIS11_15': 'BIS11_15R','BIS11_29': 'BIS11_29R'}


        bis_columns=list(bis_columns.viewvalues())



        for i in range(len(bis_columns)):
            HashTable = {4:1,3:2,2:3,1:4}
            data[bis_columns[i]]=pd.to_numeric(data[bis_columns[i]],errors='coerce')
            data[bis_columns[i]].replace(HashTable,inplace=True)



        a=['BIS11_5','BIS11_11','BIS11_28', 'BIS11_6','BIS11_24','BIS11_26','BIS11_2','BIS11_3','BIS11_4',\
           'BIS11_17','BIS11_19','BIS11_22','BIS11_25','BIS11_16','BIS11_21','BIS11_23','BIS11_14','BIS11_18',\
           'BIS11_27']
        bis_columns.extend(a)


        for i in range(len(bis_columns)):
            data[bis_columns[i]]=pd.to_numeric(data[bis_columns[i]],errors='coerce')



        data['BIS_1storder_attention']=data['BIS11_5']+data['BIS11_9R']+data['BIS11_11'] + data['BIS11_20R'] +\
                                             data['BIS11_28']


        data['BIS_1storder_cog_instab']=data['BIS11_6']+data['BIS11_24']+data['BIS11_26']




        data['BIS_1storder_motor']=data['BIS11_2']+data['BIS11_3']+data['BIS11_4'] + \
                                          data['BIS11_17']+data['BIS11_19'] + data['BIS11_22'] + \
                                          data['BIS11_25']



        data['BIS_1storder_perseverance']=data['BIS11_16']+data['BIS11_21']+data['BIS11_23'] + \
                                                data['BIS11_30R']


        data['BIS_1storder_self_control']=data['BIS11_1R']+data['BIS11_7R']+data['BIS11_8R'] + \
                                                 data['BIS11_12R']+data['BIS11_13R'] + data['BIS11_14']




        data['BIS_1storder_cog_complex']=data['BIS11_10R']+data['BIS11_15R']+data['BIS11_18'] + \
                                                data['BIS11_27']+data['BIS11_29R']


        data['BIS_2ndorder_attentional'] = data['BIS_1storder_attention']+data['BIS_1storder_cog_instab']

        data['BIS_2ndorder_motor'] = data['BIS_1storder_motor']+data['BIS_1storder_perseverance']


        data['BIS_2ndorder_nonplanning'] = data['BIS_1storder_self_control']+ \
                                                data['BIS_1storder_cog_complex']

        data['BIS_TOTAL'] = data['BIS_2ndorder_attentional'] + data['BIS_2ndorder_motor'] + \
                                   data['BIS_2ndorder_nonplanning']

        return data    
     


    def define_bis_subset_survey(self,data):

        data.rename(columns={'BIS11_9': 'BIS11_9R', 'BIS11_20': 'BIS11_20R', 'BIS11_30': 'BIS11_30R',
                             'BIS11_1': 'BIS11_1R','BIS11_7': 'BIS11_7R', 'BIS11_8': 'BIS11_8R',
                             'BIS11_12': 'BIS11_12R', 'BIS11_13': 'BIS11_13R','BIS11_10': 'BIS11_10R',
                             'BIS11_15': 'BIS11_15R','BIS11_29': 'BIS11_29R'}, inplace=True)



        bis_columns={'BIS11_9': 'BIS11_9R', 'BIS11_20': 'BIS11_20R', 'BIS11_30': 'BIS11_30R',
                      'BIS11_1': 'BIS11_1R','BIS11_7': 'BIS11_7R', 'BIS11_8': 'BIS11_8R',
                      'BIS11_12': 'BIS11_12R', 'BIS11_13': 'BIS11_13R','BIS11_10': 'BIS11_10R',
                      'BIS11_15': 'BIS11_15R','BIS11_29': 'BIS11_29R'}


        bis_columns=list(bis_columns.viewvalues())



        for i in range(len(bis_columns)):
            HashTable = {4:1,3:2,2:3,1:4}
#            data[bis_columns[i]]=pd.to_numeric(data[bis_columns[i]],errors='coerce')
            data[bis_columns[i]].replace(HashTable,inplace=True)



        a=['BIS11_5','BIS11_11','BIS11_28', 'BIS11_6','BIS11_24','BIS11_26','BIS11_2','BIS11_3','BIS11_4',\
           'BIS11_17','BIS11_19','BIS11_22','BIS11_25','BIS11_16','BIS11_21','BIS11_23','BIS11_14','BIS11_18',\
           'BIS11_27']
        bis_columns.extend(a)


#        for i in range(len(bis_columns)):
#            data[bis_columns[i]]=pd.to_numeric(data[bis_columns[i]],errors='coerce')



        data['BIS_1storder_attention']=data['BIS11_5']+data['BIS11_9R']+data['BIS11_11'] + data['BIS11_20R'] +\
                                             data['BIS11_28']


        data['BIS_1storder_cog_instab']=data['BIS11_6']+data['BIS11_24']+data['BIS11_26']




        data['BIS_1storder_motor']=data['BIS11_2']+data['BIS11_3']+data['BIS11_4'] + \
                                          data['BIS11_17']+data['BIS11_19'] + data['BIS11_22'] + \
                                          data['BIS11_25']



        data['BIS_1storder_perseverance']=data['BIS11_16']+data['BIS11_21']+data['BIS11_23'] + \
                                                data['BIS11_30R']


        data['BIS_1storder_self_control']=data['BIS11_1R']+data['BIS11_7R']+data['BIS11_8R'] + \
                                                 data['BIS11_12R']+data['BIS11_13R'] + data['BIS11_14']




        data['BIS_1storder_cog_complex']=data['BIS11_10R']+data['BIS11_15R']+data['BIS11_18'] + \
                                                data['BIS11_27']+data['BIS11_29R']


        data['BIS_2ndorder_attentional'] = data['BIS_1storder_attention']+data['BIS_1storder_cog_instab']

        data['BIS_2ndorder_motor'] = data['BIS_1storder_motor']+data['BIS_1storder_perseverance']


        data['BIS_2ndorder_nonplanning'] = data['BIS_1storder_self_control']+ \
                                                data['BIS_1storder_cog_complex']

        data['BIS_TOTAL'] = data['BIS_2ndorder_attentional'] + data['BIS_2ndorder_motor'] + \
                                   data['BIS_2ndorder_nonplanning']

        return data    











    def define_kirby_qualtrics(self,data):

        kirby={}
        for i in range(1,15):
            kirby['Q'+str(i+70)+'.1']='kirby'+str(i)

        for i in range(1,11):
            kirby['Q'+str(i+84)]='kirby'+str(14+i)


        kirby['Q102']= 'kirby25'
        kirby['Q95']= 'kirby26'
        kirby['Q96']= 'kirby27'

        data.rename(columns=kirby, inplace=True)

        kk=list(kirby.viewvalues())

        for i in range(0,len(kk)):
            HashTable = {'1':0,'2':1}
            data[kk[i]].replace(HashTable,inplace=True)

        return data
    
    
    

    def define_kirby_crosssect(self,data):

        kirby={}
        for i in range(1,15):
            kirby['Q'+str(i+70)+'.0']='kirby'+str(i)

        for i in range(1,11):
            kirby['Q'+str(i+84)]='kirby'+str(14+i)


        kirby['Q102']= 'kirby25'
        kirby['Q95']= 'kirby26'
        kirby['Q96']= 'kirby27'

        data.rename(columns=kirby, inplace=True)

        kk=list(kirby.viewvalues())

        for i in range(0,len(kk)):
            HashTable = {1:0,2:1}
            data[kk[i]].replace(HashTable,inplace=True)

        return data

    def age_qualtrics(self,data):
        data['age'] = data['age'].apply(pd.to_numeric)
        data['age'].replace({1:np.NaN},inplace=True)
        data.rename(columns={'age':'Age'},inplace=True)
        return data
    



    def gender_qualtrics(self,data):
        data.rename(columns={'gen.':'Gender'},inplace=True)
        col='Gender'
        data[col]=data[col].str.upper()
        data[col]=data[col].str.strip()

        hashtable = {'1' : 'F', 'FEMALE' : 'F','FEMALE ' : 'F', 'FEMALE16' : 'F',
                     '2' : 'M', 'MALE' : 'M', '3' : 'GQ'}

        data[col].replace(hashtable,inplace=True)
        return data



    def gender_qualtrics_adhd(self,data):
        col='Sex'
        data[col]=data[col].str.upper()

        hashtable = {'1' : 'F', 'FEMALE' : 'F','FEMALE ' : 'F', 'FEMALE16' : 'F',
                     '2' : 'M', 'MALE' : 'M'}

        data[col].replace(hashtable,inplace=True)
        
        
        data.rename(columns={'GEN':'Gender'},inplace=True)
        col='Gender'
        data[col]=data[col].str.upper()

        hashtable = {'1' : 'F', 'FEMALE' : 'F','FEMALE ' : 'F', 'FEMALE16' : 'F',
                     '2' : 'M', 'MALE' : 'M', 'AGENDER' : 'GQ'}

        data[col].replace(hashtable,inplace=True)        
        
        
        return data
        
    
    
    def gender_erab(self,data):
        data.rename(columns={'Gender_Identity':'Gender'},inplace=True)
        col='Gender'
        data[col]=data[col].str.upper()

        hashtable = {'1' : 'F', 'FEMALE' : 'F','FEMALE ' : 'F', 'FEMALE16' : 'F',
                     '2' : 'M', 'MALE' : 'M', '3' : 'GQ'}

        data[col].replace(hashtable,inplace=True)
        return data


#    def gender_surveyctocross(self,data):
#        data.rename(columns={'gen.':'Gender'},inplace=True)
#
#        hashtable = {1 : 'F',2 :'M', 3:'GQ'}
#
#        data['Gender'].replace(hashtable,inplace=True)
#        return data     
#    
    


    def gender_surveyctocross(self,data):
        data.rename(columns={'gen.':'Gender'},inplace=True)
        col='Gender'
        data[col]=data[col].str.upper()
        hashtable = {'1' : 'F', 'FEMALE' : 'F','FEMALE ' : 'F', 'FEMALE16' : 'F',
                     '2' : 'M', 'MALE' : 'M', '3' : 'GQ'}
        data['Gender'].replace(hashtable,inplace=True)
        return data     
    




    def define_audit_UCD(self,data):

        data.rename(columns={'AUDIT_1': 'audit1_r', 'AUDIT_2': 'audit2_r', 'AUDIT_3': 'audit3_r',
                             'AUDIT_4': 'audit4_r','AUDIT_5': 'audit5_r', 'AUDIT_6': 'audit6_r',
                             'AUDIT_7': 'audit7_r','AUDIT_8': 'audit8_r', 'AUDIT_9': 'audit9_r',
                             'AUDIT_10': 'audit10_r'}, inplace=True)


        audit_columns={'AUDIT_1': 'audit1_r', 'AUDIT_2': 'audit2_r', 'AUDIT_3': 'audit3_r',
                             'AUDIT_4': 'audit4_r','AUDIT_5': 'audit5_r', 'AUDIT_6': 'audit6_r',
                             'AUDIT_7': 'audit7_r','AUDIT_8': 'audit8_r'}

        audit_columns=list(audit_columns.viewvalues())
        HashTable = {1 : 0, 2 : 1, 3 : 2, 4 : 3, 5 : 4}

        for i in range(len(audit_columns)):
            data[audit_columns[i]].replace(HashTable,inplace=True)

        HashTable = {1 : 0, 2 : 2, 3 : 4}
        data['audit9_r'].replace(HashTable,inplace=True)
        data['audit10_r'].replace(HashTable,inplace=True)
        data['AUDIT_TOTAL'] = data['audit1_r'] + data['audit2_r'] + data['audit3_r'] + data['audit4_r'] + \
                              data['audit5_r'] + data['audit6_r'] + data['audit7_r'] + data['audit8_r'] + \
                              data['audit9_r'] + data['audit10_r']
                              
                              
                              
        data['AUDIT_Dependency']=data['audit4_r']+data['audit5_r']+data['audit6_r']


        data['AUDIT_Hazardous_consumption']=data['audit1_r'] + data['audit2_r'] + data['audit3_r']



        data['AUDIT_ALCO_PROBLEMS'] = data['audit4_r'] + data['audit5_r'] + data['audit6_r'] + data['audit7_r'] +\
                                      data['audit8_r'] + data['audit9_r'] + data['audit10_r']

        data['AUDIT_Alco_Related_Harm'] = data['audit7_r'] + data['audit8_r'] + data['audit9_r'] + data['audit10_r']                     
        return data


    def define_audit_ERAB(self,data):


        data['AUDIT_TOTAL'] = data['AUDIT_1'] + data['AUDIT_2'] + data['AUDIT_3'] + data['AUDIT_4'] + \
                              data['AUDIT_5'] + data['AUDIT_6'] + data['AUDIT_7'] + data['AUDIT_8'] + \
                              data['AUDIT_9'] + data['AUDIT_10']
                              
                              
                              
        data['AUDIT_Dependency']=data['AUDIT_4']+data['AUDIT_5']+data['AUDIT_6']


        data['AUDIT_Hazardous_consumption']=data['AUDIT_1'] + data['AUDIT_2'] + data['AUDIT_3']



        data['AUDIT_ALCO_PROBLEMS'] = data['AUDIT_4'] + data['AUDIT_5'] + data['AUDIT_6'] + data['AUDIT_7'] +\
                                      data['AUDIT_8'] + data['AUDIT_9'] + data['AUDIT_10']

        data['AUDIT_Alco_Related_Harm'] = data['AUDIT_7'] + data['AUDIT_8'] + data['AUDIT_9'] + data['AUDIT_10']                     
        return data


    def rename_CPNI_UCD(self,data):
        
        y=[]
        z=[]
        for i in range(1,201):
            y.append('CPNI_CPNI_'+str(i))
            z.append('CPNI_'+str(i))

        c=dict(zip(y,z))

        data.rename(columns=c,inplace=True)        
        
        
        return data


    def define_personality_dis(self,data):
        data.rename(columns={'CPNI_4':'CPNI_4_R','CPNI_125':'CPNI_125_R','CPNI_180':'CPNI_180_R','CPNI_22':'CPNI_22_R',
                             'CPNI_27':'CPNI_27_R','CPNI_44':'CPNI_44_R','CPNI_83':'CPNI_83_R','CPNI_146':'CPNI_146_R'},inplace=True)

        columns={'CPNI_4':'CPNI_4_R','CPNI_125':'CPNI_125_R','CPNI_180':'CPNI_180_R','CPNI_22':'CPNI_22_R',
                             'CPNI_27':'CPNI_27_R','CPNI_44':'CPNI_44_R','CPNI_83':'CPNI_83_R','CPNI_146':'CPNI_146_R'}

        values=list(columns.viewvalues())
        HashTable = {1:4,2:3,3:2,4:1}

        for i in range(len(values)):
            data[values[i]].replace(HashTable,inplace=True)



        data['PA'] = data.CPNI_1 +data.CPNI_22_R +data.CPNI_43 + data.CPNI_64 + \
                     data.CPNI_82 +data.CPNI_101 + data.CPNI_118

        data['BO'] = data.CPNI_2 +data.CPNI_23 +data.CPNI_44_R + data.CPNI_65 + data.CPNI_83_R + \
                     data.CPNI_102 +data.CPNI_119 + data.CPNI_128 + data.CPNI_129

        data['OC'] = data.CPNI_3 +data.CPNI_24 +data.CPNI_45 + data.CPNI_66 + data.CPNI_84 + \
                     data.CPNI_103 +data.CPNI_145 + data.CPNI_184

        data['DE'] = data.CPNI_25 + data.CPNI_46 + data.CPNI_67 +data.CPNI_85 + data.CPNI_104 + \
                     data.CPNI_130 +data.CPNI_158 + data.CPNI_4_R

        data['ST'] = data.CPNI_5 +data.CPNI_8 +data.CPNI_26 + data.CPNI_47 + \
                     data.CPNI_68 +data.CPNI_86 + data.CPNI_87 + data.CPNI_105 +\
                     data.CPNI_154 + data.CPNI_198

        data['NA'] = data.CPNI_7 +data.CPNI_28 +data.CPNI_49 + data.CPNI_70 + \
                     data.CPNI_89 +data.CPNI_107 + data.CPNI_132 + data.CPNI_133 + \
                     data.CPNI_146_R

        data['CD'] = data.CPNI_6 +data.CPNI_27_R +data.CPNI_48 + data.CPNI_69 + \
                     data.CPNI_88 + data.CPNI_106 + data.CPNI_131 + data.CPNI_141 + \
                     data.CPNI_151 + data.CPNI_155 + data.CPNI_157 + data.CPNI_160 + \
                     data.CPNI_164 + data.CPNI_170 + data.CPNI_172

        data['CDA'] = data.CPNI_27_R + data.CPNI_48 +data.CPNI_69 + data.CPNI_88 + \
                     data.CPNI_155 + data.CPNI_157 + data.CPNI_172

        data['CDD'] = data.CPNI_6 +data.CPNI_106 + data.CPNI_131 + data.CPNI_141 + data.CPNI_151 + \
                     data.CPNI_160 +data.CPNI_164 + data.CPNI_170

        data['SZ'] = data.CPNI_8 +data.CPNI_29 + data.CPNI_50 + \
                     data.CPNI_125_R +data.CPNI_165 + data.CPNI_174 + data.CPNI_180_R

        data['AV'] = data.CPNI_9 +data.CPNI_30 +data.CPNI_51 + data.CPNI_71 + \
                     data.CPNI_90 +data.CPNI_108 + data.CPNI_120

        data['HI'] = data.CPNI_10 +data.CPNI_31 +data.CPNI_52 + data.CPNI_72 + \
                     data.CPNI_91 +data.CPNI_109 + data.CPNI_121 + data.CPNI_142

        data['PAG'] = data.CPNI_19 + data.CPNI_34 +data.CPNI_39 + data.CPNI_60 + \
                     data.CPNI_79 + data.CPNI_98 + data.CPNI_116

        data['DPD'] = data.CPNI_20 +data.CPNI_33 +data.CPNI_40 + data.CPNI_41 + \
                     data.CPNI_61 +data.CPNI_80 + data.CPNI_99
        return data


    def define_dsm_iv(self,data):

        data['SAD'] = data.CPNI_15 + data.CPNI_37 + data.CPNI_58 + data.CPNI_78 +\
		               data.CPNI_97 + data.CPNI_115 + data.CPNI_126 + data.CPNI_138

        data['ODD'] = data.CPNI_14 + data.CPNI_36 + data.CPNI_57 + data.CPNI_77 +\
		               data.CPNI_96 + data.CPNI_114 + data.CPNI_124 + data.CPNI_137


        data['ADHD'] = data.CPNI_13 + data.CPNI_35 + data.CPNI_56 + data.CPNI_76 + \
		                data.CPNI_95 + data.CPNI_113 + data.CPNI_136 + data.CPNI_139 + \
					      data.CPNI_143 + data.CPNI_147 + data.CPNI_153 + data.CPNI_159 + \
					      data.CPNI_162 + data.CPNI_163 + data.CPNI_166 + data.CPNI_171 + \
					      data.CPNI_173 + data.CPNI_185

        data['ADHDINAT'] = data.CPNI_35 + data.CPNI_113 + data.CPNI_139 + data.CPNI_147 + \
		                   data.CPNI_159 + data.CPNI_162 + data.CPNI_166 +data. CPNI_173 + \
							  data.CPNI_185

        data['ADHDHI'] = data.CPNI_13 + data.CPNI_56 + data.CPNI_76 + data.CPNI_95 + data.CPNI_136 + \
		                  data.CPNI_143 + data.CPNI_153 + data.CPNI_163 + data.CPNI_171

        data['DEP'] = data.CPNI_21 + data.CPNI_33 + data.CPNI_41 + data.CPNI_54 + \
		               data.CPNI_74 + data.CPNI_93 + data.CPNI_111 + data.CPNI_134 + \
					    data.CPNI_149 + data.CPNI_168 + data.CPNI_177 + data.CPNI_182 + \
					    data.CPNI_189 + data.CPNI_190 + data.CPNI_191

        data['GAD'] = data.CPNI_15 + data.CPNI_30 + data.CPNI_37 + data.CPNI_46 + \
		               data.CPNI_58 + data.CPNI_59 + data.CPNI_61 + data.CPNI_71 + \
					     data.CPNI_78 + data.CPNI_105 + data.CPNI_120 + data.CPNI_184

        data['MND'] = data.CPNI_12 + data.CPNI_32 + data.CPNI_53 + data.CPNI_55 + \
		               data.CPNI_122 + data.CPNI_159 + data.CPNI_144 + data.CPNI_148 + \
					    data.CPNI_159 + data.CPNI_167 + data.CPNI_175 + data.CPNI_181 + \
					    data.CPNI_183 + data.CPNI_185 + data.CPNI_187 + data.CPNI_189

        data['PCD'] = data.CPNI_14 + data.CPNI_21 + data.CPNI_23 + data.CPNI_31 + \
		               data.CPNI_54 + data.CPNI_61 + data.CPNI_74 + data.CPNI_111 + \
					    data.CPNI_114 + data.CPNI_118 + data.CPNI_124 + data.CPNI_134 + \
					    data.CPNI_182 + data.CPNI_191 + data.CPNI_194 + data.CPNI_196 + data.CPNI_197

        data['PTH'] = data.CPNI_5 + data.CPNI_26 + data.CPNI_43 + data.CPNI_47 + \
		               data.CPNI_68 + data.CPNI_86 + data.CPNI_129 + data.CPNI_154 + data.CPNI_198

        data['SOM'] = data.CPNI_93 + data.CPNI_138 + data.CPNI_177 + data.CPNI_182 + \
		               data.CPNI_194 + data.CPNI_196

        data['LEARN'] = data.CPNI_55 + data.CPNI_181 + data.CPNI_183 + data.CPNI_192

        data['MEM'] = data.CPNI_166 + data.CPNI_187

        data['LANG'] = data.CPNI_38 + data.CPNI_144 + data.CPNI_148 + data.CPNI_167 + data.CPNI_175

        data['PERCEPMO'] = data.CPNI_12 + data.CPNI_123 + data.CPNI_176 + data.CPNI_188

        data['SUBCORT'] = data.CPNI_38 + data.CPNI_94 + data.CPNI_135

        data['ADHDHYP'] = data.CPNI_13 + data.CPNI_56 + data.CPNI_136 + data.CPNI_143 + \
		                   data.CPNI_153 + data.CPNI_163

        data['ADHDIMP'] = data.CPNI_76 + data.CPNI_95 + data.CPNI_171

        data['MATDEL'] = data.CPNI_75 + data.CPNI_112 + data.CPNI_156 + data.CPNI_193 + data.CPNI_195

        data ['EMODYS'] = data.CPNI_14 + data.CPNI_21 + data.CPNI_23 + data.CPNI_31 + \
		                   data.CPNI_54 + data.CPNI_61 + data.CPNI_74 + data.CPNI_114 + \
						     data.CPNI_168 + data.CPNI_197

        data['COLD'] = data.CPNI_29 + data.CPNI_87 + data.CPNI_89 + data.CPNI_174

        data['SLEEP'] = data.CPNI_59 + data.CPNI_75 + data.CPNI_111 + data.CPNI_115 + \
		                 data.CPNI_126 + data.CPNI_134 + data.CPNI_191

        data['NEURODYS'] = data.CPNI_12 + data.CPNI_32 + data.CPNI_35 + data.CPNI_38 + \
		                    data.CPNI_53 + data.CPNI_55 + data.CPNI_73 + data.CPNI_75 + \
					          data.CPNI_94 + data.CPNI_112 + data.CPNI_113 + data.CPNI_122 + \
						       data.CPNI_123 + data.CPNI_135 + data.CPNI_136 + data.CPNI_144 + \
                           data.CPNI_147 + data.CPNI_148 + data.CPNI_156 + data.CPNI_159 + \
						      data.CPNI_162 + data.CPNI_166 + data.CPNI_167 + data.CPNI_173 + \
						      data.CPNI_175 + data.CPNI_176 + data.CPNI_177 + data.CPNI_181 + \
						      data.CPNI_183 + data.CPNI_185 + data.CPNI_187 + data.CPNI_188 + \
                          data.CPNI_189 + data.CPNI_192 + data.CPNI_193 + data.CPNI_194 + \
						     data.CPNI_195 + data.CPNI_196

        data['EXF44'] = data.CPNI_4_R + data.CPNI_8 + data.CPNI_11 + data.CPNI_12 + data.CPNI_25 + \
		                data.CPNI_31 + data.CPNI_32 + data.CPNI_35 + data.CPNI_47 + data.CPNI_53 + \
					    data.CPNI_55 + data.CPNI_73 + data.CPNI_89 + data.CPNI_92 + data.CPNI_109 + \
					    data.CPNI_110 + data.CPNI_113 + data.CPNI_119 + data.CPNI_122
#CHECK!!!



        data['DECM'] = data.CPNI_4_R + data.CPNI_11 + data.CPNI_25 + data.CPNI_32 + data.CPNI_53 + \
		               data.CPNI_73 + data.CPNI_92 + data.CPNI_110 + data.CPNI_122 + \
					   data.CPNI_184 + data.CPNI_185

        data['METACOG'] = data.CPNI_12 + data.CPNI_35 + data.CPNI_47 + data.CPNI_55 + data.CPNI_113 + \
		                  data.CPNI_123 + data.CPNI_139 + data.CPNI_144 + data.CPNI_147  + data.CPNI_148 + \
				   	      data.CPNI_159 + data.CPNI_162 + data.CPNI_166 + data.CPNI_167 + data.CPNI_173 + \
				          data.CPNI_167 + data.CPNI_173 + data.CPNI_175 + data.CPNI_176 + data.CPNI_177 + \
				          data.CPNI_181 + data.CPNI_183 + data.CPNI_187 + data.CPNI_189 + data.CPNI_192

        data['SOCIN'] = data.CPNI_8 + data.CPNI_31 + data.CPNI_89 + data.CPNI_109 + \
		                data.CPNI_119 + data.CPNI_128 + data.CPNI_129 + data.CPNI_130 + \
					    data.CPNI_145 + data.CPNI_198

        data['SOCANX'] = data.CPNI_1 + data.CPNI_9 + data.CPNI_30 + data.CPNI_51 + data.CPNI_71 + \
		                 data.CPNI_82 + data.CPNI_90 + data.CPNI_101 + data.CPNI_105 + \
					     data.CPNI_108 + data.CPNI_120

        data['SELFEST'] = data.CPNI_33 + data.CPNI_90 + data.CPNI_108 + data.CPNI_130 + data.CPNI_146_R

        data['SOCWITH'] = data.CPNI_1 + data.CPNI_8 + data.CPNI_9 + data.CPNI_29 + data.CPNI_30 + \
		                  data.CPNI_50 + data.CPNI_51 + data.CPNI_71 + data.CPNI_82 + \
					      data.CPNI_90 + data.CPNI_120

        data['LAB'] = data.CPNI_23 + data.CPNI_31 + data.CPNI_116


        data['DIS'] = data.CPNI_76 + data.CPNI_95 + data.CPNI_119 + data.CPNI_171

        data['AGG'] = data.CPNI_14 + data.CPNI_27_R + data.CPNI_44_R + data.CPNI_137

        data['APA'] = data.CPNI_29 + data.CPNI_74 + data.CPNI_87 + data.CPNI_89 + data.CPNI_174

        data['PAR'] = data.CPNI_1 + data.CPNI_43 + data.CPNI_82


        return data




    def define_eating_disorder(self,data):
        data['ANOREX'] = data.CPNI_17  + data.CPNI_42 + data.CPNI_62 + data.CPNI_152
        data['BUL'] = data.CPNI_81 + data.CPNI_100 + data.CPNI_161 + data.CPNI_178 +data.CPNI_179 +\
                      data.CPNI_186    
        
        return data

    def define_dangerousness_scale(self,data):
        data['DANGER'] = data.CPNI_14 +data.CPNI_21 +data.CPNI_27_R + data.CPNI_23 + \
                         data.CPNI_36 + data.CPNI_44_R + data.CPNI_48 + data.CPNI_64 + \
                         data.CPNI_65 + data.CPNI_69 + data.CPNI_88 + data.CPNI_106 + \
                         data.CPNI_124 + data.CPNI_131

        data['ANTTV'] = data.CPNI_75 + data.CPNI_131 +data.CPNI_155


        return data

    def denial(self, data):

        l=[]

#        for i in it.chain(range(1,4),range(5,22),range(23,27),range(28,44),range(45,83),range(84,125),\
#                          range(126,180),range(181,199)):
#            l.append("CPNI_"+str(i))
#IREMOVED THE VALUES NOT IN THE FILE

        for i in it.chain(range(1,4),range(5,18),range(19,22),range(23,27),range(28,44),range(45,63),range(64,83),\
                          range(84,117),range(118,125),range(128,140),range(141,150),range(151,180),range(181,199)):
            l.append("CPNI_"+str(i))
            
        
        l.append("CPNI_126")
        subs={'CPNI_4':'CPNI_4_R','CPNI_125':'CPNI_125_R','CPNI_180':'CPNI_180_R','CPNI_22':'CPNI_22_R',
                             'CPNI_27':'CPNI_27_R','CPNI_44':'CPNI_44_R','CPNI_83':'CPNI_83_R','CPNI_146':'CPNI_146_R'}
        
        
        for i in range(len(l)):
            for key in subs.keys():
                if l[i]==key:
                    l[i]=subs[key]
                

        data['DENIAL']=data[l].sum(axis=1)


        return data



    def define_zscores(self,data):

        data['ZPA'] = (data.PA-12.2)/3.1
        
        data['ZBO'] = (data.BO-16.2)/3.7
                    
        data['ZOC'] = (data.OC-15.3)/3.3

        data['ZDE'] = (data.DE-14.0)/3.5

        data['ZST'] = (data.ST-13.6)/3.5

        data['ZNA'] = (data.NA-15.2)/4.3

        data['ZCD'] = (data.CD-19.3)/4.8

        data['ZCDA'] = (data.CDA-9.3)/2.3

        data['ZCDD'] = (data.CDD-10.0)/3.0

        data['ZSZ'] = (data.SZ-11.8)/2.6

        data['ZAV'] = (data.AV-12.0)/3.5

        data['ZHI'] = (data.HI-14.0)/3.6

        data['ZPAG'] = (data.PAG-12.8)/3.5

        data['ZDPD'] = (data.DPD-13.2)/3.

        data['ZSAD'] = (data.SAD-11.7)/3.9

        data['ZODD'] = (data.ODD-15.3)/4.5

        data['ZADHD'] = (data.ADHD-34.5)/9.8

        data['ZADHDINA'] = (data.ADHDINAT-18.6)/5.9

        data['ZADHDHI'] = (data.ADHDHI-15.9)/5.1

        data['ZADHDHYP'] = (data.ADHDHYP-10.6)/3.8

        data['ZADHDIMP'] = (data.ADHDIMP-5.4)/1.9

        data['ZDEP'] = (data.DEP-23.4)/5.6

        data['ZGAD'] = (data.GAD-19.9)/5.0

        data['ZPTH'] = (data.PTH-12.4)/3.4

        data['ZANOREX'] = (data.ANOREX-5.9)/1.9

        data['ZBUL'] = (data.BUL-7.4)/2.0

        data['ZMND'] = (data.MND-26.6)/7.7

        data['ZPCD'] = (data.PCD-29.4)/6.9

        data['ZCOLD'] = (data.COLD-6.1)/1.8

        data['ZEMODYS'] = (data.EMODYS-17.7)/4.7

        data['ZSOM'] = (data.SOM-8.5)/2.2

        data['ZLANG'] = (data.LANG-6.8)/2.2

        data['ZMEM'] = (data.MEM-4.0)/1.5

        data['ZLEARN'] = (data.LEARN-6.3)/2.4

        data['ZPERCEPM'] = (data.PERCEPMO-5.4)/1.8

        data['ZSUBCORT'] = (data.SUBCORT-3.8)/1.2

        data['ZMATDEL'] = (data.MATDEL-6.6)/2.2

        data['ZSLEEP'] = (data.SLEEP-9.8)/2.7

        data['ZNEURODY'] = (data.NEURODYS-61.4)/15.4

        data['ZDANGER'] = (data.DANGER-27.2)/6.3

        data['ZANTTV'] = (data.ANTTV-3.5)/1.0
 
        data['ZDENIAL'] = (data.DENIAL-306.7)/56.0

        data['ZEXF44'] = (data.EXF44 - 77.4)/19.0

        data['ZDECM'] = (data.DECM - 21.4)/5.9

        data['ZMETACOG'] = (data.METACOG - 38.9)/10.9

        data['ZSOCIN'] = (data.SOCIN - 17.2)/4.4

        data['ZSOCANX'] = (data.SOCANX - 17.8)/4.8

        data['ZSOCWITH'] = (data.SOCWITH - 17.6)/4.5

        data['ZSELFEST'] = (data.SELFEST - 6.5)/2.2

        data['ZLAB'] = (data.LAB-5.1)/1.78

        data['ZDIS'] = (data.DIS-6.7)/2.30

        data['ZAGG'] = (data.AGG-8.1)/2.33

        data['ZAPA'] = (data.APA-7.0)/1.92

        data['ZPAR'] = (data.PAR-4.1)/1.43

        return data


##################################AOIFE CODE#########################################################

    def define_tscores(self,data):

        data['TPA'] = 50 + (10 * data.ZPA)
		
        data['TBO'] = 50 + (10 * data.ZBO)
		
        data['TOC'] =  50 + (10 * data.ZOC)
		
        data['TDE'] = 50 + (10 * data.ZDE)
		
        data['TST'] = 50 + (10 * data.ZST)
		
        data['TNA'] = 50 + (10 * data.ZNA)
		
        data['TCD'] = 50 + (10 * data.ZCD)
		
        data['TCDA'] = 50 + (10 * data.ZCDA)
		
        data['TCDD'] = 50 + (10 * data.ZCDD)
		
        data['TSZ'] = 50 + (10 * data.ZSZ)
		
        data['TAV'] = 50 + (10 * data.ZAV)
		
        data['THI'] = 50 + (10 * data.ZHI)
		
        data['TPAG'] = 50 + (10 * data.ZPAG)
		
        data['TDPD'] = 50 + (10 * data.ZDPD)
		
        data['TSAD'] = 50 + (10 * data.ZSAD)
		
        data['TODD'] = 50 + (10 * data.ZODD)
		
        data['TADHD'] = 50 + (10 * data.ZADHD)
		
        data['TADHDINA'] = 50 + (10 * data.ZADHDINA)
		
        data['TADHDHI'] = 50 + (10 * data.ZADHDHI)
		
        data['TADHDHYP'] = 50 + (10 * data.ZADHDHYP)
		
        data['TADHDIMP'] = 50 + (10 * data.ZADHDIMP)
		
        data['TDEP'] = 50 + (10 * data.ZDEP)
		
        data['TGAD'] = 50 + (10 * data.ZGAD)
		
        data['TPTH'] = 50 + (10 * data.ZPTH)
		
        data['TANOREX'] = 50 + (10 * data.ZANOREX)
		
        data['TBUL'] = 50 + (10 * data.ZBUL)
		
        data['TMND'] = 50 + (10 * data.ZMND)
		
        data['TPCD'] = 50 + (10 * data.ZPCD)
		
        data['TEXF44'] = 50 + (10 * data.ZEXF44)
		
        data['TDECM'] = 50 + (10 * data.ZDECM)
		
        data['TMETACOG'] = 50 + (10 * data.ZMETACOG)
		
        data['TSOCIN'] = 50 + (10 * data.ZSOCIN)
		
        data['TCOLD'] = 50 + (10 * data.ZCOLD)
		
        data['TEMODYS'] = 50 + (10 * data.ZEMODYS)
		
        data['TSOM'] = 50 + (10 * data.ZSOM)
		
        data['TLANG'] = 50 + (10 * data.ZLANG)
		
        data['TMEM'] = 50 + (10 * data.ZMEM)
		
        data['TLEARN'] = 50 + (10 * data.ZLEARN)
		
        data['TPERCEPM'] = 50 + (10 * data.ZPERCEPM)
		
        data['TSUBCORT'] = 50 + (10 * data.ZSUBCORT)
		
        data['TMATDEL'] = 50 + (10 * data.ZMATDEL)
		
        data['TSLEEP'] = 50 + (10 * data.ZSLEEP)
		
        data['TNEURODY'] = 50 + (10 * data.ZNEURODY)
		
        data['TDANGER'] = 50 + (10 * data.ZDANGER)
		
        data['TANTTV'] = 50 + (10 * data.ZANTTV)
		
        data['TDENIAL'] = 50 + (10 * data.ZDENIAL)
		
        data['TSOCANX'] = 50 + (10 * data.ZSOCANX)

        data['TSELFEST'] = 50 + (10 * data.ZSELFEST)
		
        data['TSOCWITH'] = 50 + (10 * data.ZSOCWITH)
		
        data['TLAB'] = 50 + (10 * data.ZLAB)
		
        data['TDIS'] = 50 + (10 * data.ZDIS)
		
        data['TAGG'] = 50 + (10 * data.ZAGG)
		
        data['TAPA'] = 50 + (10 * data.ZAPA)
		
        data['TPAR'] = 50 + (10 * data.ZPAR)


        return data





######################################################################################################



    def define_DASS_ERAB(self,data):
        
        data['DASS21_stress'] = 2* (data.DASS21_1 + data.DASS21_6 + data.DASS21_8 + data.DASS21_11 + \
                                  data.DASS21_12 + data.DASS21_14 + data.DASS21_18)

        data['DASS21_anxiety'] = 2* (data.DASS21_2 + data.DASS21_4 + data.DASS21_7 + data.DASS21_9 + \
                                  data.DASS21_15 + data.DASS21_19 + data.DASS21_20)

        data['DASS21_depression'] = 2* (data.DASS21_3 + data.DASS21_5 + data.DASS21_10 + data.DASS21_13 + \
                                  data.DASS21_16 + data.DASS21_17 + data.DASS21_21)
        
        
        return data
    
    
    
######################################################################################################


    def define_DASS42(self,data):
        
        data['DASS42_stress'] =     data.DASS_1 + data.DASS_6 + data.DASS_8 + data.DASS_11 + \
                                  data.DASS_12 + data.DASS_14 + data.DASS_18 + data.DASS_22 +\
                                  data.DASS_27 + data.DASS_29 + data.DASS_32 + data.DASS_33 +\
                                  data.DASS_34 + data.DASS_35 + data.DASS_37 + data.DASS_39
                                  
                                  
        data['DASS42_anxiety'] =    data.DASS_2 + data.DASS_4 + data.DASS_7 + data.DASS_9 + \
                                  data.DASS_15 + data.DASS_19 + data.DASS_20 + data.DASS_23 +\
                                  data.DASS_25 + data.DASS_28 + data.DASS_30 + data.DASS_36 +\
                                  data.DASS_40 + data.DASS_41
        
        
        
        data['DASS42_depression'] = data.DASS_3 + data.DASS_5 + data.DASS_10 + data.DASS_13 + \
                                  data.DASS_16 + data.DASS_17 + data.DASS_21 + data.DASS_24 +\
                                  data.DASS_26 + data.DASS_31 + data.DASS_34 + data.DASS_37 +\
                                  data.DASS_38 + data.DASS_42
                                  
        dass = ['DASS_'+str(i) for i in range(1,43)]
        dass42 = ['DASS42_'+str(i) for i in range(1,43)]
        
        cols = dict(zip(dass,dass42))
        data.rename(columns=cols,inplace=True)

        
        
        return data








    def define_MAAS(self,data):
        data['MAAS6_TOTAL'] = (data.MAAS6_1 + data.MAAS6_2 + data.MAAS6_3 + data.MAAS6_4 + \
                              data.MAAS6_5 + data.MAAS6_6)/6


        return data

######################################################################################################






    def define_dast_UCD(self,data):
        
        a = ['DAST_20_'+str(i) for i in range(1,21)]
        b = ['DAST'+str(i) for i in range(1,21)]
        col = dict(zip(a,b))
        
        col['DAST_20_4']= 'DAST4r'
        col['DAST_20_5']= 'DAST5r'
        
        data.rename(columns=col,inplace=True)
        
        hashtable={1:0,2:1}
        for elem in col.values():
            data[elem].replace(hashtable,inplace=True)
            
            
        data.DAST4r.replace({1:0,0:1},inplace=True)
        data.DAST5r.replace({1:0,0:1},inplace=True)


        data['DAST_total']=data[col.values()].sum(axis=1)


        return data
    
    
    
    def define_dast_erab(self,data):

        a = ['DAST_'+str(i) for i in range(1,21)]
        b = ['DAST'+str(i) for i in range(1,21)]
        col = dict(zip(a,b))
        
        col['DAST_4']= 'DAST4r'
        col['DAST_5']= 'DAST5r'
        
        data.rename(columns=col,inplace=True)
                    
        data.DAST4r.replace({1:0,0:1},inplace=True)
        data.DAST5r.replace({1:0,0:1},inplace=True)


        data['DAST_total']=data[col.values()].sum(axis=1)


        return data


    


    def define_pss_erab(self,data):


        col1={'PSS_1':'pss1','PSS_2':'pss2','PSS_3':'pss3','PSS_6':'pss6', \
              'PSS_9':'pss9','PSS_10':'pss10'}

        data.rename(columns=col1,inplace=True)



        col2={'PSS_4':'pss4','PSS_5':'pss5','PSS_7':'pss7','PSS_8':'pss8'}

        HashTable = {0:4,1:3,2:2,3:1,4:0}
        #controllare 0a4 o 1a5
        data.rename(columns=col2,inplace=True)


        pss2col=list(col2.viewvalues())



        for i in range(len(pss2col)):
            
            data[pss2col[i]].replace(HashTable,inplace=True)

        l=[]
        for i in range(1,11):
            l.append('pss'+str(i))

        data['PSS_TOTAL']=data[l].sum(axis=1)
        data['MSPSS_Sig_Other_subscale'] = (data.MSPSS_1 + data.MSPSS_2 + data.MSPSS_5 + data.MSPSS_10) / 4
        data['MSPSS_Friend_subscale'] = (data.MSPSS_6 + data.MSPSS_7 + data.MSPSS_9 + data.MSPSS_12) / 4
        data['MSPSS_Family_subscale'] = (data.MSPSS_3 + data.MSPSS_4 + data.MSPSS_8 + data.MSPSS_11) / 4


        l=[]

        for i in range(1,13):
            l.append("MSPSS_"+str(i))

        data['MSPSS_total']=data[l].sum(axis=1)/12

        return data


    def define_tci(self,data):
        tci=[]

        for i in range (1,35):
            tci.append("TCI_"+str(i))


        ctci=['Ctci001', 'Ctci010', 'Ctci014', 'Ctci024', 'Ctci044', 'Ctci047', 'Ctci051', \
              'Ctci059', 'Ctci063', 'Ctci071' ,'Ctci077', 'Ctci053', 'Ctci102', 'Ctci104',\
              'Ctci105','Ctci109', 'Ctci122', 'Ctci123', 'Ctci135', 'Ctci139', 'Ctci145', \
              'Ctci155', 'Ctci156', 'Ctci159', 'Ctci165', 'Ctci170', 'Ctci172', 'Ctci176',\
              'Ctci179', 'Ctci193', 'Ctci205', 'Ctci210', 'Ctci215', 'Ctci222']

        c=dict(zip(tci,ctci))
        data.rename(columns=c,inplace=True)

        ctci2=['Ctci014', 'Ctci047', 'Ctci063', 'Ctci077' ,'Ctci053','Ctci105',\
               'Ctci123', 'Ctci139', 'Ctci145', 'Ctci155', 'Ctci156', 'Ctci159',\
               'Ctci165', 'Ctci170', 'Ctci172', 'Ctci179', 'Ctci193', 'Ctci205',\
               'Ctci210', 'Ctci176']

        hashtable={1:5 ,2: 4, 3:3}

        for i in range(0,20):
            data[ctci2[i]].replace(hashtable,inplace=True)



        data['Ctci_excit'] = data.Ctci001 + data.Ctci063 + data.Ctci053 + data.Ctci104 + data.Ctci122 +\
                              data.Ctci145 + data.Ctci156 + data.Ctci165+ data.Ctci176 + data.Ctci205


        data['Ctci_imp'] = data.Ctci010 + data.Ctci047 + data.Ctci071 + data.Ctci102 + data.Ctci123 +\
                           data.Ctci179 + data.Ctci193 + data.Ctci210

        data['Ctci_extra'] = data.Ctci014 + data.Ctci024 + data.Ctci059 + data.Ctci105 + data.Ctci139 +\
                             data.Ctci155 + data.Ctci172 + data.Ctci215 + data.Ctci222

        data['Ctci_diso'] = data.Ctci044 + data.Ctci051 + data.Ctci077 + data.Ctci109 + data.Ctci135 +\
                            data.Ctci159+ data.Ctci170


        data['Ctci_novseek'] = data.Ctci_excit + data.Ctci_imp + data.Ctci_extra + data.Ctci_diso


        return data







    def define_tci_UCD(self,data):
        tci=[]

        for i in range (1,35):
            tci.append("TCI_TCI_"+str(i))


        ctci=['Ctci001', 'Ctci010', 'Ctci014', 'Ctci024', 'Ctci044', 'Ctci047', 'Ctci051', \
              'Ctci059', 'Ctci063', 'Ctci071' ,'Ctci077', 'Ctci053', 'Ctci102', 'Ctci104',\
              'Ctci105','Ctci109', 'Ctci122', 'Ctci123', 'Ctci135', 'Ctci139', 'Ctci145', \
              'Ctci155', 'Ctci156', 'Ctci159', 'Ctci165', 'Ctci170', 'Ctci172', 'Ctci176',\
              'Ctci179', 'Ctci193', 'Ctci205', 'Ctci210', 'Ctci215', 'Ctci222']

        c=dict(zip(tci,ctci))
        data.rename(columns=c,inplace=True)

        ctci2=['Ctci014', 'Ctci047', 'Ctci063', 'Ctci077' ,'Ctci053','Ctci105',\
               'Ctci123', 'Ctci139', 'Ctci145', 'Ctci155', 'Ctci156', 'Ctci159',\
               'Ctci165', 'Ctci170', 'Ctci172', 'Ctci179', 'Ctci193', 'Ctci205',\
               'Ctci210', 'Ctci176']

        hashtable={1:5 ,2: 4, 3:3}

        for i in range(0,20):
            data[ctci2[i]].replace(hashtable,inplace=True)



        data['Ctci_excit'] = data.Ctci001 + data.Ctci063 + data.Ctci053 + data.Ctci104 + data.Ctci122 +\
                              data.Ctci145 + data.Ctci156 + data.Ctci165+ data.Ctci176 + data.Ctci205


        data['Ctci_imp'] = data.Ctci010 + data.Ctci047 + data.Ctci071 + data.Ctci102 + data.Ctci123 +\
                           data.Ctci179 + data.Ctci193 + data.Ctci210

        data['Ctci_extra'] = data.Ctci014 + data.Ctci024 + data.Ctci059 + data.Ctci105 + data.Ctci139 +\
                             data.Ctci155 + data.Ctci172 + data.Ctci215 + data.Ctci222

        data['Ctci_diso'] = data.Ctci044 + data.Ctci051 + data.Ctci077 + data.Ctci109 + data.Ctci135 +\
                            data.Ctci159+ data.Ctci170


        data['Ctci_novseek'] = data.Ctci_excit + data.Ctci_imp + data.Ctci_extra + data.Ctci_diso


        return data



    def rename_neo_UCD(self,data):
        
        y=[]
        z=[]
        for i in range(1,61):
            y.append('NEOFFI_NEOFFI_'+str(i))
            z.append('NEO_'+str(i))

        c=dict(zip(y,z))

        data.rename(columns=c,inplace=True)       
        
        return data



    def define_neo_erab(self,data):

        a=['NEO_11', 'NEO_6', 'NEO_21', 'NEO_26', 'NEO_36', 'NEO_41', 'NEO_51',\
           'NEO_56', 'NEO_7', 'NEO_37', 'NEO_2' , 'NEO_17', 'NEO_22', 'NEO_32',\
           'NEO_47', 'NEO_52', 'NEO_13', 'NEO_43', 'NEO_53','NEO_58', 'NEO_19',\
           'NEO_4', 'NEO_34', 'NEO_49', 'NEO_5', 'NEO_10', 'NEO_25', 'NEO_35',\
           'NEO_60', 'NEO_20', 'NEO_40', 'NEO_50', 'NEO_28']

        b=[]

        for i in range(len(a)) :
            b.append(re.sub('_','',a[i].lower()))

        c=dict(zip(a,b))

        hashtable={1:0, 2:1, 3:2, 4:3, 5:4}
        data.rename(columns=c,inplace=True)


        for i in range(len(b)):
            data[b[i]].replace(hashtable,inplace=True)



        d=['NEO_1', 'NEO_16', 'NEO_31', 'NEO_46', 'NEO_12', 'NEO_42', 'NEO_27', 'NEO_57',\
           'NEO_23','NEO_48', 'NEO_3',  'NEO_8', 'NEO_18', 'NEO_38','NEO_9', 'NEO_14',\
           'NEO_24', 'NEO_29', 'NEO_44', 'NEO_54','NEO_59', 'NEO_39', 'NEO_15', 'NEO_30',\
           'NEO_55','NEO_45','NEO_33']

        e=[]

        for i in range(len(d)) :
            e.append(re.sub('_','',d[i].lower()))


        f=dict(zip(d,e))
        data.rename(columns=f,inplace=True)

        hashtable={1:4, 2:3, 3:2, 4:1, 5:0}
        for i in range(len(e)):
            data[e[i]].replace(hashtable,inplace=True)

        data['NEOFFI_extraversion'] = data.neo2 + data.neo7 + data.neo12 + data.neo17 +\
                                      data.neo22 + data.neo27 + data.neo32 + data.neo37 +\
                                      data.neo42 + data.neo47 + data.neo52 + data.neo57

        data['NEOFFI_openness'] = data.neo3 + data.neo8 + data.neo13 + data.neo18 + data.neo23 +\
                                  data.neo28 + data.neo33 + data.neo38 + data.neo43 + data.neo48 +\
                                  data.neo53 + data.neo58


        data['NEOFFI_agreeableness'] = data.neo4 + data.neo9 + data.neo14 + data.neo19 + data.neo24 +\
                                       data.neo29 + data.neo34 + data.neo39 + data.neo44 + data.neo49 +\
                                       data.neo54 + data.neo59

        data['NEOFFI_conscientiousness'] = data.neo5 + data.neo10 + data.neo15 + data.neo20 + data.neo25 +\
                                           data.neo30 + data.neo35 + data.neo40 + data.neo45 + data.neo50 +\
                                           data.neo55 + data.neo60

        data['NEOFFI_neuroticism'] = data.neo1 + data.neo6 + data.neo11 + data.neo16 + data.neo21 +\
                                     data.neo26 + data.neo31 + data.neo36 + data.neo41 + data.neo46 +\
                                     data.neo51 + data.neo56
        return data




    def define_ever_smoke_erab(self,data):
        HashTable= {1:True,2:False}
        data['Ever_Smoke'].replace(HashTable, inplace=True)
        data.rename(columns={'Ever_Smoke':'Tried_cig'},inplace=True)
        HashTable= {1:'Smoker',0:'Non Smoker'}
        data['Smoker_Non_smoker'].replace(HashTable, inplace=True)
        return data

    def MX_erab(self, data):
        y={}
        z={}
        for i in range(1,156):
            y[i]='mpqb_'+str(i)
            z[i]='M'+str(i)


        a = list(y.values())
        b = list(z.values())
        c=dict(zip(a,b))

        data.rename(columns=c,inplace=True)

        return data




    def MX_UCD(self, data):
        y={}
        z={}
        for i in range(1,156):
            y[i]='MPQ_'+str(i)
            z[i]='M'+str(i)


        a = list(y.values())
        b = list(z.values())
        c=dict(zip(a,b))

        data.rename(columns=c,inplace=True)

        return data



    
    def define_ftnd(self,data):

        data.rename(columns={'FTND_1': 'ftnd1_r', 'FTND_2': 'ftnd2_r', 'FTND_3': 'ftnd3_r',
                             'FTND_4': 'ftnd4_r','FTND_5': 'ftnd5_r', 'FTND_6': 'ftnd6_r'}, inplace=True)

        HashTable = {1:0,2:1,3:2,4:3}
        data['ftnd1_r'].replace(HashTable, inplace=True)


        HashTable = {1:0,2:1}
        data['ftnd2_r'].replace(HashTable, inplace=True)


        HashTable = {1:1,2:0}
        data['ftnd3_r'].replace(HashTable, inplace=True)



        HashTable = {1:0,2:1,3:2,4:3}
        data['ftnd4_r'].replace(HashTable, inplace=True)


        HashTable = {1:0,2:1}
        data['ftnd5_r'].replace(HashTable, inplace=True)

        HashTable = {1:0,2:1,3:1,4:1,5:1,6:1}
        data['ftnd6_r'].replace(HashTable, inplace=True)

        data['FTND_TOTAL'] = data['ftnd1_r'] + data['ftnd2_r'] + data['ftnd3_r'] + \
                             data['ftnd4_r'] + data['ftnd5_r'] + data['ftnd6_r']
        return data    


    def define_ftcd(self,data):

        data.rename(columns={'FTCD_1': 'ftcd1_r','FTCD_2':'ftcd2_r', 'FTCD_3': 'ftcd3_r',
                             'FTCD_4': 'ftcd4_r','FTCD_5': 'ftcd5_r', 'FTCD_6': 'ftcd6_r'}, inplace=True)

        HashTable = {1:0,2:1,3:2,4:3}
        data['ftcd1_r'].replace(HashTable, inplace=True)


        HashTable = {1:0,2:1}
        data['ftcd2_r'].replace(HashTable, inplace=True)


        HashTable = {1:1,2:0}
        data['ftcd3_r'].replace(HashTable, inplace=True)



        HashTable = {1:0,2:1,3:2,4:3}
        data['ftcd4_r'].replace(HashTable, inplace=True)


        HashTable = {1:0,2:1}
        data['ftcd5_r'].replace(HashTable, inplace=True)

        HashTable = {1:0,2:1,3:1,4:1,5:1,6:1}
        data['ftcd6_r'].replace(HashTable, inplace=True)

        data['FTCD_TOTAL'] = data['ftcd1_r'] + data['ftcd2_r'] + data['ftcd3_r'] + \
                             data['ftcd4_r'] + data['ftcd5_r'] + data['ftcd6_r']
        return data 




    def define_AEQ(self,data):
        
        
        
        data['AEQ_Positive_Global_Changes'] = data.AEQ_16 + data.AEQ_20 + data.AEQ_30 + data.AEQ_31 +\
                                              data.AEQ_38 + data.AEQ_40 + data.AEQ_42 + data.AEQ_43 +\
                                              data.AEQ_45 + data.AEQ_49 + data.AEQ_50 + data.AEQ_51 +\
                                              data.AEQ_52 + data.AEQ_54 + data.AEQ_62 + data.AEQ_65 +\
                                              data.AEQ_68 + data.AEQ_69 + data.AEQ_70 + data.AEQ_71 +\
                                              data.AEQ_72 + data.AEQ_76 + data.AEQ_83 + data.AEQ_87 

        data['AEQ_Sexual_Enhancement'] = data.AEQ_47 + data.AEQ_59 + data.AEQ_66 +data.AEQ_79 + \
                                         data.AEQ_80 + data.AEQ_81 + data.AEQ_88

        data['AEQ_Social_Physical_Pleasure'] = data.AEQ_35 + data.AEQ_8 + data.AEQ_15 +data.AEQ_17 + \
                                               data.AEQ_22 + data.AEQ_28 + data.AEQ_29 + data.AEQ_84


        data['AEQ_Assertiveness'] = data.AEQ_7 + data.AEQ_14 + data.AEQ_19 + data.AEQ_21 + data.AEQ_26 + \
                                     data.AEQ_36 + data.AEQ_41 + data.AEQ_63 + data.AEQ_73 + data.AEQ_90

        data['AEQ_Relaxation_Tension_Reduction'] = data.AEQ_57 + data.AEQ_61 + data.AEQ_64 + data.AEQ_74 + \
                                                   data.AEQ_75 + data.AEQ_78 + data.AEQ_85 + data.AEQ_86 + \
                                                   data.AEQ_89

        data['AEQ_Arousal_Interpersonal_Power'] = data.AEQ_10 + data.AEQ_11 + data.AEQ_18 + data.AEQ_23 + \
                                                  data.AEQ_33 + data.AEQ_39 + data.AEQ_58 + data.AEQ_67 + \
                                                  data.AEQ_77
        return data
    
    
    
    def bf(self,data):
       
        data['WBbf'] = data.M1 + data.M26 + data.M38  + data.M50 + data.M62+\
                       data.M74 + data.M85 + data.M97 + data.M109 + data.M121+\
                       data.M133 + data.M144
                       
        SPbf1 = 'M2 M15 M39 M51 M75 M87 M110'.split()
        SPbf0 =  'M63 M98 M122 M134 M145'.split()
        data['SPbf'] = data[SPbf1].eq(1).sum(axis=1) + data[SPbf0].eq(0).sum(axis=1)


        ACbf1 = 'M3 M16 M27 M52 M76 M88 M111 M123 M135 M146'.split() 
        ACbf0 =  'M64 M99'.split()
        data['ACbf'] = data[ACbf1].eq(1).sum(axis=1) + data[ACbf0].eq(0).sum(axis=1)


        SCbf1 = 'M5 M17 M40 M77 M112'.split() 
        SCbf0 = 'M28 M65 M89 M100 M124 M136 M148'.split()
        data['SCbf'] = data[SCbf1].eq(1).sum(axis=1) + data[SCbf0].eq(0).sum(axis=1)
        

        data['SRbf'] = data.M6 + data.M18 + data.M29 + data.M41 + data.M53 + data.M78 +\
                       data.M90 + data.M101 + data.M113 + data.M125 +data.M137 + data.M149

        AGbf1 = 'M8 M20 M31 M43 M55 M67 M103 M115 M127 M139 M151'.split()
        AGbf0 = 'M79'.split()
        data['AGbf'] = data[AGbf1].eq(1).sum(axis=1) + data[AGbf0].eq(0).sum(axis=1)
        

        data['ALbf'] = data.M7 + data.M19 + data.M30 + data.M42 + data.M54 + data.M66 +\
                       data.M91 + data.M102 + data.M114 + data.M126 + data.M138 + data.M150


        CNbf1 = 'M9 M44 M56 M68 M92 M116 M128 M140'.split()
        CNbf0 = 'M21 M33 M80 M152'.split()
        data['CNbf'] = data[CNbf1].eq(1).sum(axis=1) + data[CNbf0].eq(0).sum(axis=1)



        HAbf1 = 'M34 M69 M81 M93 M105 M129'.split() 
        HAbf0 = 'M11 M22 M46 M57 M141 M153'.split()
        data['HAbf'] = data[HAbf1].eq(1).sum(axis=1) + data[HAbf0].eq(0).sum(axis=1)

        TRbf1 = 'M12 M23 M35 M58 M70 M82 M94 M106 M142 M154'.split() 
        TRbf0 = 'M47 M118'.split()
        data['TRbf'] = data[TRbf1].eq(1).sum(axis=1) + data[TRbf0].eq(0).sum(axis=1)

        ABbf1 = 'M13 M24 M36 M48 M59 M71 M83 M95 M107 M119'.split() 
        ABbf0 = 'M130 M155'.split()
        data['ABbf'] = data[ABbf1].eq(1).sum(axis=1) + data[ABbf0].eq(0).sum(axis=1)
        
        UVbf1 = 'M25 M49 M72 M96 M120 M143 M147'.split()
        UVbf0 = 'M4 M14 M37 M61 M84 M108 M131'.split()
        data['UVbf'] = data[UVbf1].eq(1).sum(axis=1) + data[UVbf0].eq(0).sum(axis=1)
        
             
             
             

        data['PEMbf'] = (1.933 * data.WBbf) + (1.669 * data.SPbf) + (1.671 * data.ACbf) +\
                        (1.95 * data.SCbf) + (0.085 * data.SRbf) + (0.292 * data.ALbf) +\
                        (0.13 * data.AGbf) + (0.048 * data.CNbf) + (0.015 * data.HAbf) +\
                        (0.07 * data.TRbf) + 13.712


        data['NEMbf'] = (0.127 * data.WBbf) + (0.15 * data.SPbf) + (0.038 * data.ACbf) +\
                        (0.279 * data.SCbf) + (1.904 * data.SRbf) + (3.061 * data.ALbf) +\
                        (2.551 * data.AGbf) + (0.045 * data.CNbf) + (0.126 * data.HAbf) +\
                        (0.147 * data.TRbf) + 6.27
        

        data['CONbf'] = -0.085 * data.WBbf + (-0.052 * data.SPbf) + (0.241 * data.ACbf) +\
                        (-0.068 * data.SCbf) + (0.046 * data.SRbf) + (-0.302 * data.ALbf) +\
                        (0.296 * data.AGbf) + (2.717 * data.CNbf) + (2.579 * data.HAbf) +\
                        (2.199 * data.TRbf) + 20.742
        

        data['PEMAGbf'] = 1.529 * data.WBbf + 1.294 * data.SPbf + 3.211 * data.ACbf +\
                         (-0.317 * data.SCbf) + (-0.112 * data.SRbf) + (-0.085 * data.ALbf) +\
                         (0.063 * data.AGbf) + (0.154 * data.CNbf) + (-0.186 * data.HAbf) +\
                          (0.02 * data.TRbf) + 18.448
        

        data['PEMCObf'] = (1.582 * data.WBbf) + (1.387 * data.SPbf) + (-0.51 * data.ACbf) +\
                      (3.411 * data.SCbf) + (0.048 * data.SRbf) + (0.017 * data.ALbf) +\
                      (0.059 * data.AGbf) + (-0.068 * data.CNbf) + (0.205 * data.HAbf) +\
                      (0.097 * data.TRbf) + 16.804

        data['NEMAGbf'] = 0.042 * data.WBbf + (0.111 * data.SPbf) + (-0.036 * data.ACbf) +\
                      (-0.07 * data.SCbf) + (1.721 * data.SRbf) + (-0.885 * data.ALbf) +\
                      (5.26 * data.AGbf) + (0.106 * data.CNbf) + (0.13 * data.HAbf) +\
                      (0.057 * data.TRbf) + 22.739

        data['NEMALbf'] = (-0.043 * data.WBbf) + (-0.072 * data.SPbf) + (0.059 * data.ACbf) +\
                          (0.206 * data.SCbf) + (1.389 * data.SRbf) + (5.398 * data.ALbf) +\
                         (-0.695 * data.AGbf) + (-0.114 * data.CNbf) + (-0.025 * data.HAbf) +\
                          (0.089 * data.TRbf) + 20.341

        return data 
    
    
    def Tbf(self,data):
        data['TWBbf']  = ((data.WBbf - 8.6785) / 2.84443) * 10 + 50 
        data['TSPbf']  = ((data.SPbf - 4.7933) / 3.57565) * 10 + 50
        data['TACbf']  = ((data.ACbf - 6.9422) / 3.11712) * 10 + 50 
        data['TSCbf']  = ((data.SCbf - 7.7415) / 3.14921) * 10 + 50 
        data['TSRbf'] = ((data.SRbf - 5.6244) / 3.45281) * 10 + 50 
        data['TAGbf'] = ((data.AGbf - 2.5304) / 2.43678) * 10 + 50 
        data['TALbf'] = ((data.ALbf - 1.5104) / 2.30630) * 10 + 50 
        data['TCNbf'] = ((data.CNbf - 8.5378) / 2.57915) * 10 + 50 
        data['THAbf'] = ((data.HAbf - 8.7326) / 2.79156) * 10 + 50 
        data['TTRbf'] = ((data.TRbf - 8.2496) / 2.87842) * 10 + 50 
        data['TABbf'] = ((data.ABbf - 5.5052) / 3.06363) * 10 + 50 
        data['TUVbf'] = ((data.UVbf - 3.3467) / 2.39033) * 10 + 50 
        data['TPEMbf'] = ((data.PEMbf - 67.5556) / 14.62548) * 10 + 50  
        data['TNEMbf'] = ((data.NEMbf - 34.9926) / 14.74955) * 10 + 50 
        data['TCONbf'] = ((data.CONbf - 85.3111) / 14.41936) * 10 + 50 
        data['TPEMAGbf'] = ((data.PEMAGbf - 57.0207) / 14.24022) * 10 + 50 
        data['TPEMCObf'] = ((data.PEMCObf - 62.4948) / 14.66491) * 10 + 50 
        data['TNEMAGbf'] = ((data.NEMAGbf - 47.0059) / 14.82040) * 10 + 50 
        data['TNEMALbf'] = ((data.NEMALbf - 35.3726) / 14.48441) * 10 + 50
         
        return data


    def define_STAI_qualtrics(self,data):
        
        col1={'STAI1_1':'STAI1_1R','STAI1_2':'STAI1_2R','STAI1_5':'STAI1_5R',
              'STAI1_8':'STAI1_8R','STAI1_10':'STAI1_10R','STAI1_11':'STAI1_11R',
              'STAI1_15':'STAI1_15R','STAI1_16':'STAI1_16R'}
        
        data.rename(columns=col1, inplace=True)
        
        HashTable = {1:4,2:3,3:2,4:1}
        
        values=list(col1.viewvalues())

        for i in range(len(values)):
            data[values[i]].replace(HashTable,inplace=True)
        
        
        col2={'STAI1_19':'STAI1_19R','STAI1_20':'STAI1_20R','STAI2_1':'STAI2_1R','STAI2_3':'STAI2_3R',
              'STAI2_6':'STAI2_6R','STAI2_7':'STAI2_7R','STAI2_10':'STAI2_10R','STAI2_13':'STAI2_13R',
              'STAI2_14':'STAI2_14R','STAI2_16':'STAI2_16R','STAI2_19':'STAI2_19R'}
        
        data.rename(columns=col2, inplace=True)
                
        values=list(col2.viewvalues())

        for i in range(len(values)):
            data[values[i]].replace(HashTable,inplace=True)
            

            
            
        data['STAI_State_Total'] = data.STAI1_1R + data.STAI1_2R + data.STAI1_3 + data.STAI1_4 + data.STAI1_5R + data.STAI1_6+\
                                   data.STAI1_7 + data.STAI1_8R + data.STAI1_9 + data.STAI1_10R + data.STAI1_11R + data.STAI1_12+\
                                   data.STAI1_13 + data.STAI1_14 + data.STAI1_15R + data.STAI1_16R + data.STAI1_17 + data.STAI1_18+\
                                   data.STAI1_19R + data.STAI1_20R
                                   
                                   
        data['STAI_Trait_Total'] = data.STAI2_1R + data.STAI2_2 + data.STAI2_3R + data.STAI2_4 + data.STAI2_5 + data.STAI2_6R+\
                                   data.STAI2_7R + data.STAI2_8 + data.STAI2_9 + data.STAI2_10R + data.STAI2_11 + data.STAI2_12+\
                                   data.STAI2_13R + data.STAI2_14R + data.STAI2_15 + data.STAI2_16R + data.STAI2_17 + data.STAI2_18+\
                                   data.STAI2_19R + data.STAI2_20     
            
        
        return data


    
    
    

    def define_CAARS_qualtrics(self,data):

        data['CAARS_InattnMem'] = data.CAARS1_3 + data.CAARS1_7 + data.CAARS1_11 + data.CAARS1_16 +\
                                  data.CAARS1_18 + data.CAARS2_10 + data.CAARS2_14 + data.CAARS2_18 +\
                                  data.CAARS2_22 + data.CAARS3_5 + data.CAARS3_7 + data.CAARS3_22


        data['CAARS_HyperRest'] = data.CAARS1_1 + data.CAARS1_5 + data.CAARS1_13 + data.CAARS1_17 + data.CAARS1_20 +\
                                  data.CAARS2_3 + data.CAARS2_5 + data.CAARS2_9 + data.CAARS3_2 + data.CAARS3_10 +\
                                  data.CAARS3_13 + data.CAARS3_15 

        data['CAARS_ImpEmot'] = data.CAARS1_4 + data.CAARS1_8 + data.CAARS1_12 + data.CAARS1_19 + data.CAARS2_1 +\
                                data.CAARS2_8 + data.CAARS2_13 + data.CAARS2_17 + data.CAARS3_1 + data.CAARS3_3 +\
                                data.CAARS3_8 + data.CAARS3_17 
 
        data['CAARS_Selfconcept'] = data.CAARS1_6 + data.CAARS1_15 + data.CAARS2_4 + data.CAARS2_15 +\
                                    data.CAARS3_12 + data.CAARS3_19 



        data['CAARS_InattnDSM4'] = data.CAARS1_2 + data.CAARS2_2 + data.CAARS2_7 + data.CAARS2_11 +\
                                   data.CAARS2_20 + data.CAARS3_4 + data.CAARS3_16 + data.CAARS2_20 +\
                                   data.CAARS3_21


        data['CAARS_HyperImpDSM4'] = data.CAARS1_9 + data.CAARS1_14 + data.CAARS1_21 + data.CAARS1_22 +\
                                     data.CAARS2_16 + data.CAARS2_19 + data.CAARS3_6 + data.CAARS3_14 + data.CAARS3_18

        data['CAARS_SymptomDSM4_total'] = data.CAARS1_2 + data.CAARS1_9 + data.CAARS1_14 + data.CAARS1_21 + data.CAARS1_22 +\
                                          data.CAARS2_2 + data.CAARS2_7 + data.CAARS2_11 + data.CAARS2_16 + data.CAARS2_19 +\
                                          data.CAARS2_20 + data.CAARS3_4 +data.CAARS3_6 + data.CAARS3_14 + data.CAARS3_16+\
                                          data.CAARS3_18 + data.CAARS3_20 + data.CAARS3_21


        data['CAARS_ADHDindex'] = data.CAARS1_10 + data.CAARS1_19 + data.CAARS2_1 + data.CAARS2_4 + data.CAARS2_5 +\
                                  data.CAARS2_6 + data.CAARS2_12 + data.CAARS2_18 + data.CAARS3_1 + data.CAARS3_9 +\
                                  data.CAARS3_11 + data.CAARS3_19

        return data
    
    
    
    
    def define_WURS(self,data):
        
        data['WURS_subscore'] = data.WURS_3 + data.WURS_4 + data.WURS_5 + data.WURS_6 + data.WURS_7 +\
                                data.WURS_9 + data.WURS_10 + data.WURS_11 + data.WURS_12 + data.WURS_15+\
                                data.WURS_16 + data.WURS_17 + data.WURS_20 + data.WURS_21 + data.WURS_24 +\
                                data.WURS_25 + data.WURS_26 + data.WURS_27 + data.WURS_28 + data.WURS_29 +\
                                data.WURS_40 + data.WURS_41 + data.WURS_51 + data.WURS_56 + data.WURS_59
        return data
    
    
    
    def define_MASC(self,data):
        
        data['MASC_SP'] = data.MASC_26 + data.MASC_30 + data.MASC_33 + data.MASC_4 + data.MASC_7 + data.MASC_9+\
                          data.MASC_17 + data.MASC_19 + data.MASC_23 

        data['MASC_GAD'] = data.MASC_27 + data.MASC_29 + data.MASC_31 + data.MASC_1 + data.MASC_6 + data.MASC_39+\
                           data.MASC_40 + data.MASC_13 + data.MASC_17 + data.MASC_22 

        data['MASC_HR'] = data.MASC_29 + data.MASC_3 + data.MASC_10 + data.MASC_16 + data.MASC_22 


        data['MASC_PF'] = data.MASC_32 + data.MASC_36 + data.MASC_38 + data.MASC_14 

        data['MASC_OC'] = data.MASC_41 + data.MASC_42 + data.MASC_43 + data.MASC_44 + data.MASC_45 + data.MASC_46 +\
                          data.MASC_47 + data.MASC_48 + data.MASC_49 + data.MASC_50 
                          
        data['MASC_P'] = data.MASC_31 + data.MASC_37 + data.MASC_6 + data.MASC_12 + data.MASC_18 + data.MASC_20 + data.MASC_24 
        
        data['MASC_TR'] = data.MASC_27 + data.MASC_34 + data.MASC_1 + data.MASC_8 + data.MASC_15

        data['MASC_HA'] = data.MASC_28 + data.MASC_35 + data.MASC_2 + data.MASC_5 + data.MASC_11 +\
                          data.MASC_13 + data.MASC_21 + data.MASC_25 



        data['MASC_PST'] = data.MASC_31 + data.MASC_37 + data.MASC_6 + data.MASC_12 + data.MASC_18 +\
                           data.MASC_20 + data.MASC_24 + data.MASC_27 + data.MASC_34 + data.MASC_1 +\
                           data.MASC_8 + data.MASC_15


        data['MASC_SAT'] =  data.MASC_29 + data.MASC_3 + data.MASC_10 + data.MASC_16 + data.MASC_22 +\
                            data.MASC_32 + data.MASC_36 + data.MASC_38 + data.MASC_14

        data['MASC_Total'] = data.MASC_26 + data.MASC_30 + data.MASC_33 + data.MASC_4 + data.MASC_7 + data.MASC_9 +\
                             data.MASC_17 + data.MASC_19 + data.MASC_23 + data.MASC_29 + data.MASC_3 + data.MASC_10 +\
                             data.MASC_16 + data.MASC_22 + data.MASC_32 + data.MASC_36 + data.MASC_38 + data.MASC_14 +\
                             data.MASC_41 + data.MASC_42 + data.MASC_43 + data.MASC_44 + data.MASC_45 + data.MASC_46 +\
                             data.MASC_47 + data.MASC_48 + data.MASC_49 + data.MASC_50 + data.MASC_31 + data.MASC_37 +\
                             data.MASC_6 + data.MASC_12 + data.MASC_18 + data.MASC_20 + data.MASC_24 + data.MASC_27 +\
                             data.MASC_34 + data.MASC_1 + data.MASC_8 + data.MASC_15 + data.MASC_28 + data.MASC_35 +\
                             data.MASC_2 + data.MASC_5 + data.MASC_11 + data.MASC_13 + data.MASC_21 + data.MASC_25 +\
                             data.MASC_39 + data.MASC_40 

        
        data['MASC_inconsistency_score'] = abs(data.MASC_3 - data.MASC_10) + abs(data.MASC_4 - data.MASC_9) +\
                                           abs(data.MASC_8 - data.MASC_15) + abs(data.MASC_13 - data.MASC_35) +\
                                           abs(data.MASC_20 - data.MASC_27) + abs(data.MASC_22 - data.MASC_29) +\
                                           abs(data.MASC_43 - data.MASC_44) + abs(data.MASC_47 - data.MASC_50) 




        data['t_1'] =np.where(data['MASC_SP']<9,0,1)
        data['t_2'] =np.where(data['MASC_GAD']<15,0,1)
        data['t_3'] =np.where(data['MASC_SAT']<16,0,1)            


        data['t_total'] = data.t_1 + data.t_2 + data.t_3


        data['Anxiety_Probability_Score'] = ['Low Probability' if x == 0 else 'Borderline Probability'\
            if x == 1 else 'High Probability' if x==2 else 'Very High Probability' for x in data['t_total']]
        
        
            

        return data

    
    def define_CAARS(self,data):
        
        data['CAARS_InattnMem'] = data.CAARS_3 + data.CAARS_7 + data.CAARS_11 + data.CAARS_16 + data.CAARS_18 + data.CAARS_32 +\
                                  data.CAARS_36 + data.CAARS_40 + data.CAARS_44 + data.CAARS_49 + data.CAARS_51 + data.CAARS_66 
 
        data['CAARS_HyperRest'] = data.CAARS_1 + data.CAARS_5 + data.CAARS_13 + data.CAARS_17 + data.CAARS_20 + data.CAARS_25 +\
                                  data.CAARS_27 + data.CAARS_31 + data.CAARS_46 + data.CAARS_54 + data.CAARS_57 + data.CAARS_59 

        data['CAARS_ImpEmot'] = data.CAARS_4 + data.CAARS_8 + data.CAARS_12 + data.CAARS_19 + data.CAARS_23 + data.CAARS_30 +\
                                data.CAARS_35 + data.CAARS_39 + data.CAARS_43 + data.CAARS_47 + data.CAARS_52 + data.CAARS_61 

        data['CAARS_Selfconcept'] = data.CAARS_6 + data.CAARS_15 + data.CAARS_26 + data.CAARS_37 + data.CAARS_56 + data.CAARS_63

        data['CAARS_InattnDSM4'] = data.CAARS_2 + data.CAARS_24 + data.CAARS_29 + data.CAARS_33 + data.CAARS_42 + data.CAARS_48+\
                                   data.CAARS_60 + data.CAARS_64 + data.CAARS_65 
 
        data['CAARS_HyperImpDSM4'] = data.CAARS_9 + data.CAARS_14 + data.CAARS_21 + data.CAARS_22 + data.CAARS_38 + data.CAARS_41+\
                                     data.CAARS_50 + data.CAARS_58 + data.CAARS_62 

        data['CAARS_SymptomDSM4_total'] = data.CAARS_2 + data.CAARS_9 + data.CAARS_14 + data.CAARS_21 + data.CAARS_22 + data.CAARS_24 +\
                                          data.CAARS_29 + data.CAARS_33 + data.CAARS_38 + data.CAARS_41 + data.CAARS_42 + data.CAARS_48 +\
                                          data.CAARS_50 + data.CAARS_58 + data.CAARS_60 + data.CAARS_62 + data.CAARS_64 + data.CAARS_65 

        data['CAARS_ADHDindex'] = data.CAARS_10 + data.CAARS_19 + data.CAARS_23 + data.CAARS_26 + data.CAARS_27 + data.CAARS_28 +\
                                  data.CAARS_34 + data.CAARS_40 + data.CAARS_45 + data.CAARS_53 + data.CAARS_55 + data.CAARS_63 


        
        return data
    
    
    
    def define_STAI(self,data):
        
        col1={'STAIS_1':'STAIS_1R','STAIS_2':'STAIS_2R','STAIS_5':'STAIS_5R',
              'STAIS_8':'STAIS_8R','STAIS_10':'STAIS_10R','STAIS_11':'STAIS_11R',
              'STAIS_15':'STAIS_15R','STAIS_16':'STAIS_16R'}
        
        data.rename(columns=col1, inplace=True)
        
        HashTable = {1:4,2:3,3:2,4:1}
        
        values=list(col1.viewvalues())

        for i in range(len(values)):
            data[values[i]].replace(HashTable,inplace=True)
        
        
        col2={'STAIS_19':'STAIS_19R','STAIS_20':'STAIS_20R','STAIT_1':'STAIT_1R','STAIT_3':'STAIT_3R',
              'STAIT_6':'STAIT_6R','STAIT_7':'STAIT_7R','STAIT_10':'STAIT_10R','STAIT_13':'STAIT_13R',
              'STAIT_14':'STAIT_14R','STAIT_16':'STAIT_16R','STAIT_19':'STAIT_19R'}
        
        data.rename(columns=col2, inplace=True)
                
        values=list(col2.viewvalues())

        for i in range(len(values)):
            data[values[i]].replace(HashTable,inplace=True)
            

            
            
        data['STAI_State_Total'] = data.STAIS_1R + data.STAIS_2R + data.STAIS_3 + data.STAIS_4 + data.STAIS_5R + data.STAIS_6+\
                                   data.STAIS_7 + data.STAIS_8R + data.STAIS_9 + data.STAIS_10R + data.STAIS_11R + data.STAIS_12+\
                                   data.STAIS_13 + data.STAIS_14 + data.STAIS_15R + data.STAIS_16R + data.STAIS_17 + data.STAIS_18+\
                                   data.STAIS_19R + data.STAIS_20R
                                   
                                   
        data['STAI_Trait_Total'] = data.STAIT_1R + data.STAIT_2 + data.STAIT_3R + data.STAIT_4 + data.STAIT_5 + data.STAIT_6R+\
                                   data.STAIT_7R + data.STAIT_8 + data.STAIT_9 + data.STAIT_10R + data.STAIT_11 + data.STAIT_12+\
                                   data.STAIT_13R + data.STAIT_14R + data.STAIT_15 + data.STAIT_16R + data.STAIT_17 + data.STAIT_18+\
                                   data.STAIT_19R + data.STAIT_20     
            
        
        return data    
    
    
    
    def define_control_adhd(self,data):
        HashTable = {1:True,2:False}
        data['parent_control'].replace(HashTable, inplace=True)
        data['sibling_control'].replace(HashTable, inplace=True)
        
        data['Control'] =np.where(((data['DIA'] == 5) & ((data['parent_control']==False) | (data['sibling_control']==False))),True,False)

        return data
    
    
    
    def gender_surveycto_adhd(self,data):
        
        data.rename(columns={'GEN':'Gender'},inplace=True)
        hashtable = {-1:'F',1:'M',0:'GQ'}
        col='Gender'
        data[col].replace(hashtable,inplace=True)        
        col='Sex'
        data[col].replace(hashtable,inplace=True)        

        return data
    

    def define_marital_adhd(self,data):        
        status={1:'single',2:'in a relationship',3:'married',4:'separated',5:'divorced',6:'widowed'}
        data['MAR_ADHDtxt'] = data['MAR_ADHD'].map(status)
        return data
    
    

    def define_marital_status(self,data):
        
        status_erab_ucd={1:'Single',2:'In a relationship',3:'In a relationship',4:'Separated or divorced',5:'Widowed'}
        status_adhd={1:'Single',2:'In a relationship',3:'In a relationship',4:'Separated or divorced',5:'Separated or divorced',\
                     6:'Widowed'}

        data['MAR']=np.where(data.Study=='ERAB', data['MAR_ERAB'].map(status_erab_ucd),\
                        np.where(data.Study=='UCD', data['MAR_UCD'].map(status_erab_ucd),\
                        np.where(data.Study=='ADHD_surveycto',data['MAR_ADHD'].map(status_adhd),np.where(data.Study=='ADHD_qualtrics',\
                        data['MAR_ADHD'].map(status_adhd),np.NaN))))


        return data    
    
    def define_DIA_adhd(self,data):
        dia={1:'ADHD only',2:'Anxiety',3:'ADHD and anxiety',4:'Other diagnosis',5:'None of the above'}
        data['DIAtxt'] = data['DIA'].map(dia)
        return data
    
    
    def define_type_adhd(self,data):
        row_index = data.Control == True
        data.loc[row_index, 'ADHD_Type'] = 'control'
        
        row_index = data.parent_control == True
        data.loc[row_index, 'ADHD_Type'] = 'parent'
        
        row_index = data.sibling_control == True
        data.loc[row_index, 'ADHD_Type'] = 'sibling'
        
        row_index = data.DIA == 1
        data.loc[row_index, 'ADHD_Type'] = 'adhd'
        
        row_index = data.DIA == 2
        data.loc[row_index, 'ADHD_Type'] = 'anxiety only'

        row_index = data.DIA == 3
        data.loc[row_index, 'ADHD_Type'] = 'adhd and anxiety'
        
        
        
        
        row_index = data.Control == True
        data.loc[row_index, 'ADHD_Type2'] = 'control'
        
        row_index = data.parent_control == True
        data.loc[row_index, 'ADHD_Type2'] = 'parent'
        
        row_index = data.sibling_control == True
        data.loc[row_index, 'ADHD_Type2'] = 'sibling'
                
        row_index = data.DIA == 2
        data.loc[row_index, 'ADHD_Type2'] = 'anxiety only'        
        
        
        row_index = ((data.DIA == 3) | (data.DIA == 1))
        data.loc[row_index, 'ADHD_Type2'] = 'adhd'


        return data
    
    
    
    
    
    def define_type_cross(self,data):
        data['Study'] = ['BCANN' if i[0:2]=='BM' else 'CANN_MB' if i[0:2]=='CA' else 'UG' for i in data.index.tolist()]
        return data



    def define_smoke30days(self,data):
        
        data.rename(columns={'smoke_last30days':'Past_month_smoke'},inplace=True)
        col='Past_month_smoke'
        
        
        data[col] = [1 if x == 0 else 2 if x >1 and x<5 else 3 if x>=5 and x<30\
                     else 4 if x>=30 and x<151 else 5 if x>=151 and x<301 else 6 if x>=301 and x<600 else 7 if x>=600 else np.NaN for x in data[col]]
        

        return data
    
#    
    
    def define_smoking_type(self,data):
        

        
        data['Smoker_type'] = np.where(np.logical_and(data.LifetimeSmoking==7, data.Past_month_smoke>2),
                              'Smoker', np.where(np.logical_and(data.LifetimeSmoking==7,data.Past_month_smoke == 1), \
                              'Ex-smoker', np.where(np.logical_and(data.LifetimeSmoking<7, data.Past_month_smoke == 1),\
                              'Non-smoker', None)))   
        
        data.loc['EJ130515SEX','Smoker_type'] = 'Ex-smoker'

     
        return data