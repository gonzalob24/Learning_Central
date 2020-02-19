# -*- coding: utf-8 -*-

"""
Part 1: Working with data
"""


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html

import sys
import json

"""
Reading a writing files
"""

dframe = pd.read_csv("myfile.csv")

# does not include a header ans the columns are also indexed by numbers
dframe2 = pd.read_csv("myfile.csv", header=None)

# another way to import csv files using read_table
dframe3 = pd.read_table("myfile.csv", sep=",", header=None)

# I can also indicate the number of rows to read,
pd.read_csv("myfile.csv", header=None, nrows=2)

# export/output file
dframe2.to_csv('output_file.csv')
dframe.to_csv(sys.stdout)
dframe.to_csv(sys.stdout, sep="_")

# write only a specific subset of columns
dframe2.to_csv(sys.stdout, columns=[0,1,2])

url = 'https://docs.python.org/2/library/csv.html'


"""
JSON
"""

json_obj = """
{   "zoo_animal": "Lion",
    "food": ["Meat", "Veggies", "Honey"],
    "fur": "Golden",
    "clothes": null, 
    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
}
"""

data = json.loads(json_obj)

# convert back tp json
json.dumps(data)

dframe = DataFrame(data['diet'])

"""
HTML
"""
url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'

dframe_list = pd.io.html.read_html(url)
dframe = dframe_list[0]
dframe.columns.values


"""
Excel Files
"""

xls_file = pd.ExcelFile("excel_test.xlsx")
dframe = xls_file.parse('Sheet1')




































