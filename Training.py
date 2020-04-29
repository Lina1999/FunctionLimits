import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("3.csv", na_values='?')

dfTest = pd.read_csv("3Test.csv", na_values='?')

#Normalizing
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
df = min_max_scaler.fit_transform(df)
dfTest = min_max_scaler.transform(dfTest)

df = pd.DataFrame(data=df)
dfTest = pd.DataFrame(data=dfTest)

X = df.drop(df.columns[len(df.columns) - 1], axis = 1) 
y = df[[df.columns[len(df.columns) - 1]]]


from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import numpy as np

regr = RandomForestRegressor()
regr.fit(X, y)

X_test = dfTest.drop(dfTest.columns[len(dfTest.columns) - 1], axis = 1)

y_test = dfTest[[dfTest.columns[len(dfTest.columns) - 1]]] 

y_pred = regr.predict(X_test)

print("regressor R^2:", regr.score(X_test, y_test))
