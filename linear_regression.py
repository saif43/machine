import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key = "c2KeqCdV1QsyAtKxpooU"
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df['Class'] = (df['Adj. Close'])
df = df[['Class','HL_PCT','PCT_change','Adj. Volume']]

print("*************** Main Dataset ***************\n")
print(df.head())

forecast_col        = 'Class'         
df.fillna(-99999,inplace=True)
forecast_out = int(math.ceil(0.01*len(df)))
df['Predict Class'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

print("\n*************** Main Dataset With  Predict Class ***************\n")
print(df.head())

X = np.array(df.drop(['class'],1))
y = np.array(df['class'])
X = preprocessing.scale(X)
y = np.array(df['class'])

print(len(X),len(y))
