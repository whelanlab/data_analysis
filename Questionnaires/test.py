
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
        #macpath='CSV/mastersheet.csv'
        data=pd.read_csv(winpath,sep=',',header=1,index_col='ID')
        return data
        
        
    def add_null(self,data):
        data.replace(-999,np.NaN)
        return data
    

    
    def preprocess_data(self,data):
        
        self.read_data()
        self.add_null(data)
        
        return data
    
    
    
    
reader=DataReader()
data=reader.read_data()
df=reader.preprocess_data(data)


      
        