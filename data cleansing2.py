import pandas as pd

data = pd.read_excel('data.xlsx')
print('Metadataset:\n',data)

data.info()

data_du = (data.duplicated()).sum()
print('Duplicated data:\n',str(data_du))

NAN = (data.isnull()).sum()
print('NaN values in per column:\n',NAN)


print('NaN value:\n',data[data.isnull().values])


data_1 = data.dropna().reset_index(drop=True)
print('Metadatasets after deleting NaN values:\n',data_1)
data_1.info()

print('data_1:\n',data_1.describe())