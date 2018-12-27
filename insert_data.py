# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:32:31 2018

@author: sofyan.fadli
"""

import sqlite3
import io
import random

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

names = []

for line in io.open('./names.txt', encoding="utf8"):
    names.append(line.strip().lower())
    
for i in range(1,100000):
    insert_data = "INSERT INTO data_sim VALUES (?,?,?,?,?)"
    cursor.execute(insert_data, (None,random.choice(names), random.choice(names), random.randint(100000, 999999), random.randint(100000, 999999)))


connection.commit()
connection.close()
