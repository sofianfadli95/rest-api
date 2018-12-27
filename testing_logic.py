# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:51:24 2018

@author: sofyan.fadli
"""

import cx_Oracle
import base64

db = cx_Oracle.connect('sofian/sofian@192.168.9.105:1521/orcl')
cur = db.cursor()
cur.arraysize=50

# my_dict = {"nik" : 760447, "no_sim" : 134417} , "no_sim" : 134417
data = {"nama" : "anna solana hamami kadarachman", "no_sim" : None, "nik" : 676799}
new_data = data
for key in list(data):
    if data[key] == None:
        new_data.pop(key, None)

query = "SELECT * FROM data_sim WHERE "
keyword = []
values = []
row = []

# Iterasi key dan value-nya
for key, value in new_data.items():
    keyword.append(key + " = :"+ key)
    
query = query + " AND ".join(keyword)
print(query)
result = cur.execute(query, new_data)
row = result.fetchone()
img = row[4].read()
print(type(img))
print(img)




