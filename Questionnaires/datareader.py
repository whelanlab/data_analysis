
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib as plt

winpath='CSV\mastersheet.csv'
macpath='CSV/mastersheet.csv'
path='CSV\mastersheet.xlsx'


#df=pd.read_excel(path,sep=',',header=1,index_col='ID')


class DataReader:
    
    def read_data(self):
        winpath='CSV\mastersheet.csv'
        #macpath='/Volumes/ShareDisk_1/Andrea/src/CSV/mastersheet.csv'
        data=pd.read_csv(winpath,sep=',',header=1,index_col='ID')
        data.index=data.index.str.upper()
        return data
        
        
    def add_null(self,data):
        data.replace(-999,np.NaN)
        return data
    
 
    def replace_column(self,col,hashtable):        
        data[col].replace(hashtable,inplace=True)
        return data
    
    
    def set_gender_rescored(self,data):
        col='Gender_Rescored'
        HashTable = {-1 : 'F', 0 : 'GQ', 1 : 'M'}
        data=self.replace_column(col,HashTable)
        return data
        
    
   
    def set_gender(self,data):          
        col='Gender'
        HashTable = {"Female" : 'F', "1" : 'F', "female" : 'F', "FEMALE" : 'F', "FEMALE16" : 'F',
                     "2" : 'M', "male" : 'M', "Male" : 'M', "3" : 'GQ'}
        
        data=self.replace_column(col,HashTable)
        return data
        
    
    def set_ever_smoke(self,data):
        col='ever_smoke'
        HashTable = {1 : 'Yes', 2 : 'No'}
        data=self.replace_column(col,HashTable)
        return data
    
#   
   
    def set_ADHDgroupcomb(self,data):          
        col='ADHD_GROUP_comb'
        
        HashTable = {1 : 'ADHD&anxiety + ADHD' , 2 : 'siblingADHD' , 4 : 'Anxiety' , 5 : 'Control'}

        data=self.replace_column(col,HashTable)
        return data
        
        
        
    def set_Surveyed_post_hoc(self,data):
        col='Surveyed_post_hoc'
        HashTable = {0 : 'No', 1 : 'Yes'}
        data=self.replace_column(col,HashTable)
        return data    
    
    def set_Relapse_Early_Late(self,data):
        col='Relapse_Early_Late'
        HashTable = {1 : 'Early', 2 : 'Late'}
        data=self.replace_column(col,HashTable)
        return data 
    
    
    def set_han(self,data):
        col='HAN'
        HashTable = {1 : 'R', 2 : 'L'}
        data=self.replace_column(col,HashTable)
         
        return data    
    
    
    
    def preprocess_data(self,data):
        self.add_null(data)
        self.set_gender(data)
        self.set_gender_rescored(data)
        self.set_ever_smoke(data)
        self.set_Surveyed_post_hoc(data)
        self.set_han(data)
        self.set_ADHDgroupcomb(data)
        self.set_Relapse_Early_Late(data)
        return data
    
    
    
    
reader=DataReader()
data=reader.read_data()
df=reader.preprocess_data(data)



      
        