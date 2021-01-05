import pandas as pd
import numpy as np
import distython
import os
import seaborn as sns
import matplotlib.pyplot as plt


tidy_data = pd.read_csv('tidy.csv')
X_data = tidy_data.drop(['CHT_No', 'reStroke'], axis=1)
y_data = tidy_data[['reStroke']]
categorical_ix = [0, 2, 3, 4, 5, 6, 7, 8, 34, 35, 36, 37, 38, 43, 44, 45,46, 48, 49, 50, 51, 52, 53, 55]
categorical_columns = X_data.columns[categorical_ix].values
numerical_columns =  np.setdiff1d(X_data.columns, categorical_columns)

from sklearn.preprocessing import StandardScaler, OneHotEncoder

X_data[numerical_columns] = StandardScaler().fit_transform(X_data[numerical_columns])
df = pd.get_dummies(X_data, columns=categorical_columns)
df_2 = pd.get_dummies(X_data, columns=categorical_columns, drop_first=True)
df_2.to_csv()
print('done')