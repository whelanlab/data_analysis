# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:12:38 2017

@author: alenia
"""

import pandas as pd
import os


sstpath = os.path.join('CSV/LOG','allversion_SST_stats.csv')
ddtpath = os.path.join('CSV/LOG','DD_K_results.csv')
csstpath = os.path.join('CSV/LOG','CSST_stats.csv')
emidpath = os.path.join('CSV/LOG','eMID_summary.csv')
pstwfbpath = os.path.join('CSV/LOG','PSTwFB.csv')
pstnofbpath = os.path.join('CSV/LOG','PSTnFB.csv')
smokstrooppath = os.path.join('CSV/LOG','SmokingStroop_summary_Values.xlsx')
strooppath = os.path.join('CSV/LOG','Stroop_summary_Values.csv')
igtpath = os.path.join('CSV/LOG','IGT_summary_Values.csv')
nbackpath = os.path.join('CSV/LOG','Nback_summary_Values.csv')


def read_log():
    ddt = pd.read_csv(ddtpath)
    sst = pd.read_csv(sstpath)
    csst = pd.read_csv(csstpath)
    emid = pd.read_csv(emidpath)
    pstwf = pd.read_csv(pstwfbpath)
    pstnf = pd.read_csv(pstnofbpath)
    smokesrt = pd.read_excel(smokstrooppath)
    stroop = pd.read_csv(strooppath)
    igt = pd.read_csv(igtpath)
    nback = pd.read_csv(nbackpath)
#   PD = pd.read_csv(pdpath)


    ddt = ddt.drop_duplicates(subset='case_id', keep='last')
    ddt.set_index('case_id',inplace=True)
    ddt.index=ddt.index.str.upper()

    sst = sst.drop_duplicates(subset='case_id', keep='last')
    sst.set_index('case_id',inplace=True)
    sst.index=sst.index.str.upper()
    
    csst = csst.drop_duplicates(subset='case_id', keep='last')
    csst.set_index('case_id',inplace=True)
    csst.index=csst.index.str.upper()
    
    
    emid = emid.drop_duplicates(subset='case_id', keep='last')
    emid.set_index('case_id',inplace=True)
    emid.index=emid.index.str.upper()
    
    
    pstwf = pstwf.drop_duplicates(subset='case_id', keep='last')
    pstwf.set_index('case_id',inplace=True)
    pstwf.index=pstwf.index.str.upper()
    
    
    
    pstnf = pstnf.drop_duplicates(subset='case_id', keep='last')
    pstnf.set_index('case_id',inplace=True)
    pstnf.index=pstnf.index.str.upper()    
    
    
    smokesrt = smokesrt.drop_duplicates(subset='case_id', keep='last')
    smokesrt.set_index('case_id',inplace=True)
    smokesrt.index=smokesrt.index.str.upper()


    stroop = stroop.drop_duplicates(subset='case_id', keep='last')
    stroop.set_index('case_id',inplace=True)
    stroop.index=stroop.index.str.upper()
    
    
    
    igt = igt.drop_duplicates(subset='case_id', keep='last')
    igt.set_index('case_id',inplace=True)
    igt.index=igt.index.str.upper()



    nback = nback.drop_duplicates(subset='case_id', keep='last')
    nback.set_index('case_id',inplace=True)
    nback.index=nback.index.str.upper()
    
    
    
#    PD = PD.drop_duplicates(subset='case_id', keep='last')
#    PD.set_index('case_id',inplace=True)
#    PD.index=PD.index.str.upper()    

    
    
    log = sst.join(ddt,how='outer')
    log = log.join(csst,how='outer')
    log = log.join(emid,how='outer')
    
    log = log.join(pstwf,how='outer')
    log = log.join(pstnf,how='outer')
    log = log.join(smokesrt,how='outer')
    log = log.join(stroop,how='outer')
    log = log.join(igt,how='outer')
    log = log.join(nback,how='outer')    
#    log = log.join(PD,how='outer')     
    
    
    log.reset_index(inplace=True)
    log = log[log.case_id != 'AAA']
    log = log[log.case_id != 'QQ']
    log = log[log.case_id != 'TTT']
    log = log[log.case_id != 'VFG']


    log['Log'] = 'True'
    return log