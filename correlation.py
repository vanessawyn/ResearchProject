import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import matplotlib


dframe = pd.read_csv('correlation/innerjoindata.csv') #Reading the new csv file
dframe.columns = dframe.columns.str.strip()
dframe.drop(dframe.columns[[2,3,5,7,8,9,12,14]], axis=1,inplace=True)
dframe.set_index('sa2_name_2016',inplace=True) #Setting the index to SA2 name
dframe.columns = ['Walkability Index','No Vehicle','Jobless Family','Overweight','Obesity','Mental Issue']

dframe.to_csv("./newJoin.csv")

dframe.corr()

#print dframe.corr(method='pearson')

r = DataFrame(dframe.corr()['Walkability Index'])
#print r_r2
r.columns = ['Correlation']
#print r_r2

r.to_csv("./correlation.csv")









