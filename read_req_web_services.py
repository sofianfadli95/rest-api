# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:12:01 2018

@author: sofyan.fadli
"""

import cx_Oracle

db = cx_Oracle.connect('sofian/sofian@192.168.3.52:1521/oracle')
cur = db.cursor()
cur.arraysize=50
cur.execute("""SELECT HOLDER_ID, NAMA, NAMA_LENGKAP, NIK , NO_SIM FROM DATA_SIM""")
print ("""HOLDER_ID \t NAMA \t NAMA_LENGKAP \t NIK \t NO_SIM \n""")
for column_1, column_2, column_3, column_4, column_5 in cur.fetchall():
    print(column_1, "\t", column_2, "\t", column_3, "\t", column_4, "\t", column_5, "\n")
document = cur.execute("""SELECT JARIKIRI_LF, JARIKIRI_RF	, JARIKIRI_MF	, JARIKIRI_IF	 , JARIKIRI_TF FROM DATA_SIM""")
row = document.fetchone()
imageBlob = row[0]
imageBlob1 = row[1]
imageBlob2 = row[2]

blob = imageBlob.read()
blob1 = imageBlob1.read()
blob2 = imageBlob2.read()
cur.close()
db.close()

