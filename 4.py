import pandas as pd
import quandl, math
import numpy as np 
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key = "Pn68DezX2qc3gFwjyzoC"
df = quandl.get('WIKI/GOOGL')

print(df.head())

print('********************************************************************************')

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace = True)

forecast_out = int(math.ceil(.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

X = np.array(df.drop(['label'],1))
y = np.array(df['label'])

X = preprocessing.scale(X)
# X = X[:-forecast_out+1]
y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)

clf =LinearRegression(n_jobs=-1)
clf.fit(X_train,y_train)
accuracy =clf.score(X_test,y_test)

print('Linear regression: Accuracy of',forecast_out,'day ahead is ',accuracy)

clf =svm.SVR()
clf.fit(X_train,y_train)
accuracy =clf.score(X_test,y_test)
print('SVM: Accuracy of',forecast_out,'day ahead is ',accuracy)


clf =svm.SVR(kernel='poly')
clf.fit(X_train,y_train)
accuracy =clf.score(X_test,y_test)
print('Polynonial kernal: Accuracy of',forecast_out,'day ahead is ',accuracy)