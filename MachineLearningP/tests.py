# from django.test import TestCase
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create your tests here.
# con = sqlite3.connect("data/portal_mammals.sqlite")
# df = pd.read_sql_query("SELECT * from surveys", con)

con = sqlite3.connect('dataset.db')
cur = con.cursor()
# table = """"""
# cur.execute(table)

cur.execute("SELECT col10, col11, col12 FROM dataset")

rows = cur.fetchall()
x10 = [row[0] for row in rows]
u = np.arange(len(x10))
print(x10[0:5])

# for row in rows:
    # print(row[0], row[1], row[2])
    
    
con.close()