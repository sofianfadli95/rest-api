# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 09:19:09 2018

@author: sofyan.fadli
"""

from flask_restful import Resource, reqparse
import cx_Oracle
import base64

import os
os.environ['LD_LIBRARY_PATH'] = '/usr/lib/oracle/12.2/client64/lib/'

class Sim(Resource):
    keywords = ["holder_id", "nama", "nama_lengkap", "nik", "no_sim"]
    parser = reqparse.RequestParser()
    
    for element in keywords:
        parser.add_argument(element, 
                            type=str,
                            required=False,
                            help="This field cannot be left blank!"
                )
    
    def post(self):
        data = Sim.parser.parse_args()
        new_data = data
        for key in list(data):
            if data[key] == None:
                new_data.pop(key, None)
        # print(new_data)
        # print(type(new_data))
        if not bool(new_data):
            return {'message' : 'Anda belum memasukkan keyword pencarian.'}
        # Mengganti setiap value menjadi value utk parameter 'LIKE'
        for key,value in new_data.items():
            new_data[key] = "%" + value.upper() + "%"

        db = cx_Oracle.connect('DWH_STG_KORLANTAS/STGKORLANTAS2016@10.100.15.239:1521/DWHPROD')
        cur = db.cursor()
        cur.arraysize=50
        
        query = "SELECT * FROM tbl_data_sim WHERE "
        
        keyword = []
        users = []
            
        # Iterasi key dan value-nya
        for key, value in new_data.items():
            keyword.append("UPPER(" + key + ")" + " LIKE :"+ key)
        query = query + " AND ".join(keyword) + " AND ROWNUM <= 10"
        # print(query)
        result = cur.execute(query, new_data)
        def blob_json(blob):
            if blob and type(blob) is not str:
                blob = blob.read()
                blob = base64.encodebytes(blob)
                return blob.decode('ascii')
            return None
            
        if result:
            for row in result:
                users.append({'holder_id' : row[0], 'nama' : row[1], 'nama_lengkap' : row[2], 'nik' : row[3],
                              'photo' : blob_json(row[4]), 'no_sim' : row[5]})
            db.close()
            # f = open("result.json","w")
            # f.write(json.dumps({'users' : users}))
            # f.close()
            if len(users) != 0:
                return {'users' : users}
            return {'message' : 'Data tidak ditemukan'}
        db.close()
        return {'message' : 'Data tidak ditemukan'}
        
        
        
        