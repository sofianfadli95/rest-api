# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:09:56 2018

@author: sofyan.fadli
"""

import cx_Oracle
import base64

counter = 0

def blob_json(blob):
    blob = blob.read()
    blob = base64.encodebytes(blob)
    # return blob.decode('ascii')
    return blob
        
new_data = {"nama" : "AAAAA"}
connection = cx_Oracle.connect('DWH_STG_KORLANTAS/STGKORLANTAS2016@10.100.15.239:1521/DWHPROD')
cursor = connection.cursor()

names = []

query = "SELECT * FROM tbl_data_sim WHERE nama LIKE :nama AND ROWNUM <= 20"
result = cursor.execute(query, new_data)
for row in result:
    print("Holder ID : {}, Nama : {}, Nama lengkap : {}, NIK : {}, Photo : {}, No SIM : {}".format
          (row[0],row[1],row[2],row[3],blob_json(row[4]),row[5]))
    counter += 1
    image_64_decode = base64.decodebytes(blob_json(row[4]))
    image_result = open('photo_{}.gif'.format(counter), 'wb') # create a writable image and write the decoding result 
    image_result.write(image_64_decode)
connection.commit()
connection.close()