# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:32:31 2018

@author: sofyan.fadli
"""

import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS data_sim (holder_id INTEGER PRIMARY KEY, nama text, nama_lengkap text, nik text, no_sim)"
cursor.execute(create_table)

connection.commit()

connection.close()