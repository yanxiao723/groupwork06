# -*- coding: utf-8 -*-
"""

@author: Longbin Chen
__StudentID__ = 320180939591
__Group__ = 6

"""

import pandas as pd

data = pd.read_csv('author_log1.csv',index_col=0)
#read CSV
print('Metadataset:\n',data)

data.info()
#View the basic information of the data

NAN = (data.isnull()).sum()
print('NaN values in per column:\n',NAN)
#find NAN value in per column

print('NaN value:\n',data[data.isnull().values])


data_1 = data.dropna().reset_index(drop=True)
print('Metadatasets after deleting NaN values:\n',data_1)
#delete Nan value and reset the indexs
data_1.info()

print('data_1:\n',data_1.describe())

#do the same works to other csv
print('------------------------------------------------------')

data1 = pd.read_csv('data_log',index_col=0)
#read CSV
print('Metadataset:\n',data1)

data1.info()
#View the basic information of the data

NAN = (data1.isnull()).sum()
print('NaN values in per column:\n',NAN)
#find NAN value in per column

print('NaN value:\n',data1[data1.isnull().values])


data_2 = data1.dropna().reset_index(drop=True)
print('Metadatasets after deleting NaN values:\n',data_2)
#delete Nan value and reset the indexs
data_2.info()

print('data_1:\n',data_2.describe())

print('------------------------------------------------------')

data2 = pd.read_csv('log.csv',index_col=0)
#read CSV
print('Metadataset:\n',data2)

data2.info()
#View the basic information of the data

NAN = (data2.isnull()).sum()
print('NaN values in per column:\n',NAN)
#find NAN value in per column

print('NaN value:\n',data2[data2.isnull().values])


data_3 = data2.dropna().reset_index(drop=True)
print('Metadatasets after deleting NaN values:\n',data_3)
#delete Nan value and reset the indexs
data_3.info()

print('data_1:\n',data_3.describe())