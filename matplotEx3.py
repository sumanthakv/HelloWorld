import matplotlib.pyplot  as plt
import numpy as np
import xlrd as xl
path="Z:\py_lib\skvs\sk.xlsx"
file=open(path,'r+')
file=xl.open_workbook("Z:\py_lib\skvs\sk.xlsx")
print(file.sheet_names())
file.