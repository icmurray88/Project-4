#!/usr/bin/env python
# coding: utf-8

# In[5]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Llamallama88!",
  database="Project4"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Project4 (firstname, lastname, coursename, courselocation) VALUES (%s, %s, %s, %s)"
val = ("Sam, Smith, BUS100, Hall")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

import csv
with open('project4.csv','w',newline='')as f:
    thewriter=csv.writer(f)
    
    thewriter.writerow(['firstname', 'lastname', 'coursename', 'courselocation'])


# In[ ]:




