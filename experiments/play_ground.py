import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from util import JIM_HEOM
import umap



tidy_data = pd.read_csv('vitalsing_data.csv')
print(tidy_data.shape)
X_data = tidy_data.drop(['ID', 'CHT_NO', 'admin_date', 'discharge_date',
                         'AllMortality', 'CVDeath  ', 'Death Date', 'SurvivalWeeks'], axis=1)
y_data = tidy_data[['SurvivalWeeks']]
y_data = (y_data < 24).astype(int)
categorical_ix = [0, 2, 3, 4, 5, 6, 7, 8]

# tidy_data = pd.read_csv('tidy.csv')
# tidy_data = tidy_data.append(tidy_data, ignore_index=True)
# tidy_data = tidy_data.append(tidy_data, ignore_index=True)
# tidy_data = tidy_data.append(tidy_data, ignore_index=True)
# print(tidy_data.shape)
# X_data = tidy_data.drop(['CHT_No', 'reStroke'], axis=1)
# y_data = tidy_data[['reStroke']]
# categorical_ix = [0, 2, 3, 4, 5, 6, 7, 8, 34, 35, 36, 37, 38, 43, 44, 45,46, 48, 49, 50, 51, 52, 53, 55]

categorical_columns = X_data.columns[categorical_ix].values
numerical_columns = np.setdiff1d(X_data.columns, categorical_columns)


X_data[numerical_columns] = StandardScaler().fit_transform(X_data[numerical_columns])
# one-hot
X_data_one_hot = pd.get_dummies(X_data, columns=categorical_columns)

heom_metric = JIM_HEOM.JHEOM(X_data, categorical_ix,)


print(heom_metric)


reducer = umap.UMAP(metric='cosine', random_state=369)

umap_heom_embedding = reducer.fit_transform(X_data)

plt.clf()
plt.scatter(
    umap_heom_embedding[:, 0],
    umap_heom_embedding[:, 1],
    c=y_data.values.astype(int), s=1, cmap='Spectral')
plt.gca().set_aspect('equal', 'datalim')

plt.show()
print(umap_heom_embedding)