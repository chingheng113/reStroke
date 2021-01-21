import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import distython
from tsnecuda import TSNE


tidy_data = pd.read_csv('vitalsing_data.csv')
print(tidy_data.shape)
X_data = tidy_data.drop(['ID', 'CHT_NO', 'admin_date', 'discharge_date',
                         'AllMortality', 'CVDeath  ', 'Death Date', 'SurvivalWeeks'], axis=1)
y_data = tidy_data[['SurvivalWeeks']]
y_data = (y_data < 24).astype(int)
categorical_ix = [0, 2, 3, 4, 5, 6, 7, 8]

categorical_columns = X_data.columns[categorical_ix].values
numerical_columns = np.setdiff1d(X_data.columns, categorical_columns)


X_data[numerical_columns] = StandardScaler().fit_transform(X_data[numerical_columns])
# one-hot
X_data_one_hot = pd.get_dummies(X_data, columns=categorical_columns)

heom_metric = distython.HEOM(X_data, categorical_ix,)

tsne_embedding = TSNE(n_components=2, perplexity=15, learning_rate=10).fit_transform(X_data_one_hot)

plt.scatter(
    tsne_embedding[:, 0],
    tsne_embedding[:, 1],
    c=y_data.values.astype(int), s=1, cmap='Spectral')
plt.gca().set_aspect('equal', 'datalim')

plt.savefig(os.path.join('..', 'result', 'tsne_vitalsign.png'))