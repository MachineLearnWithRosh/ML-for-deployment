# ML-for-deployment
This repository is all about of deployment of Machine Learning model

This assignments has been done under the guidance of <b>iNeuron</b>. [click here to visit](https://ineuron.ai/)
![alt text](https://github.com/MachineLearnWithRosh/ML-for-deployment/blob/master/Images/ineuron.png)

import pypyodbc 
import pandas as pd

conn = pypyodbc.connect("Driver=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.8.so.1.1;"
                        "Server=aextestandlearn.database.windows.net;"
                        "Database=aextestandlearn;"
                        "uid=satstndlrnetld;pwd=Welcome@200",autocommit=True)

cursor = conn.cursor()
