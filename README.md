# ML-for-deployment
This repository is all about of deployment of Machine Learning model

This assignments has been done under the guidance of <b>iNeuron</b>. [click here to visit](https://ineuron.ai/)
![alt text](https://github.com/MachineLearnWithRosh/ML-for-deployment/blob/master/Images/ineuron.png)


import pypyodbc 
import pandas as pd

conn = pypyodbc.connect("Driver=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.8.so.1.1;"
                        "Server=;"
                        "Database=;"
                        "uid=;pwd=",autocommit=True)

cursor = conn.cursor()

cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-0DMHFMS\SQLEXPRESS;"
                      "Database=AdventureWorks2017;"
                      "Trusted_Connection=yes;")



Driver=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.3.so.1.1


cursor = cnxn.cursor()

cursor.execute('select * from HumanResources.Department')

for row in cursor:
    print('row = %r' % (row,))
