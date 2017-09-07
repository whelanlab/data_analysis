# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 12:25:34 2017

@author: alenia
"""

import merge as merge
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


merge.write_data()
merge.notmerged()
merge.saveindex()

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


file_list = drive.ListFile({'q': "'%s' in parents" % '0B47oiKVG_cJ6c051a0Rkd0V3Tm8'}).GetList()
for f in file_list:
    if f['title']=='Data Bank' or f['title']=='Not Merged' or f['title']=='ID Log' or f['title']=='ID Surveys':
        f.Delete()



file1 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": '0B47oiKVG_cJ6c051a0Rkd0V3Tm8'}]})
file1.SetContentFile('data.csv')
file1['title']='Data Bank'

file1.Upload({'convert': True})




file2 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": '0B47oiKVG_cJ6c051a0Rkd0V3Tm8'}]})
file2.SetContentFile('not merged with type.csv')
file2['title']='Not Merged'

file2.Upload({'convert': True})



file3 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": '0B47oiKVG_cJ6c051a0Rkd0V3Tm8'}]})
file3.SetContentFile('index surveys.txt')
file3['title']='ID Surveys'

file3.Upload({'convert': True})


file4 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": '0B47oiKVG_cJ6c051a0Rkd0V3Tm8'}]})
file4.SetContentFile('index log files.txt')
file4['title']='ID Log'

file4.Upload({'convert': True})  

        
#permission = file1.InsertPermission({
#                        'type': 'user',
#                        'value': 'anyone',
#                        'role': 'reader'})        
#        
#    
