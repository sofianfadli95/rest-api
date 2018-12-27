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

class Ktp(Resource):
    keywords = ["nik" , "pendidikanakhir", "namalengkapayah", "golongandarah", "kabupatenname", "propinsiname",
                "namalengkap", "kecamatanname", "agama", "jenispekerjaan", "statuskawin", "penyandangcacat", 
                "kodepos", "dusun", "tanggallahir", "statushubungankeluarga", "ektpstatus", "tempatlahir", "nokel",
                "namalengkapibu", "ektpcreated", "kelname", "nokk", "nort", "nokab", "alamat", "jeniskelamin", "norw",
                "nokec", "noprop", "lastupdate"]
    parser = reqparse.RequestParser()
    
    for element in keywords:
        parser.add_argument(element, 
                            type=str,
                            required=False,
                            help="This field cannot be left blank!"
                )
    
    def post(self):
        data = Ktp.parser.parse_args()
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

        db = cx_Oracle.connect('STAGING_SPOT/STAGING_SPOT@10.100.15.239:1521/DWHPROD')
        cur = db.cursor()
        cur.arraysize=50
        
        query = "SELECT * FROM PPST_TEMP_ADMINDUK WHERE "
        
        keyword = []
        users = []
            
        # Iterasi key dan value-nya
        for key, value in new_data.items():
            keyword.append("UPPER(" + key + ")" + " LIKE :"+ key)
        query = query + " AND ".join(keyword) + " AND ROWNUM <= 10"
        # print(query)
        result = cur.execute(query, new_data)
        def blob_json(blob):
            if bool(blob) is True and type(blob) is not str:
                blob = blob.read()
                blob = base64.encodebytes(blob)
                return blob.decode('ascii')
            return None
            
        if result:
            for row in result:
                users.append({ 'nik' : row[0], 'pendidikanakhir' : row[1], 'namalengkapayah' : row[2], 'golongandarah' : row[3],
                              'kabupatenname' : row[4], 'propinsiname' : row[5], 'namalengkap' : row[6], 'kecamatanname' : row[7], 'agama' : row[8],
                              'jenispekerjaan' : row[9], 'statuskawin' : row[10], 'penyandangcacat' : row[11], 'kodepos' : row[12],
                              'dusun' : row[13], 'tanggallahir' : row[14], 'statushubungankeluarga' : row[15], 'ektpstatus' : row[16],
                              'tempatlahir' : row[17], 'nokel' : row[18], 'namalengkapibu' : row[19], 'ektpcreated' : row[20],
                              'kelname' : row[21], 'nokk' : row[22], 'nort' : row[23], 'nokab' : row[24],
                              'alamat' : row[25], 'jeniskelamin' : row[26], 'norw' : row[27], 'nokec' : row[28],
                              'noprop' : row[29], 'lastupdate' : str(row[30]), 'foto' : row[31]})
            db.close()
            # f = open("result.json","w")
            # f.write(json.dumps({'users' : users})
            # f.close()
            if len(users) != 0:
                return {'users' : users}
            return {'message' : 'Data tidak ditemukan'}
        db.close()
        return {'message' : 'Data tidak ditemukan'}
        
        
        
        
