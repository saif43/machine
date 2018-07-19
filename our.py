import numpy as np
import pandas as pd
fields = ['no','income','age','education','marital','usage']

df = pd.read_csv('our.csv', skipinitialspace=True, usecols=fields)
# print(df.keys())
# print(df.no)
# print(df.no.size)
print(df.age.unique())
print('--------------------------------')

# print(df.groupby('age').count())
# print(df.groupby(['income', 'usage']).count())
a = df.groupby(['age'])['age'].count()
print(a)
print('--------------------------------')
print(df.groupby(['age','usage'])['age'].count())