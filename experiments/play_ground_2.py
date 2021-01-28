import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import umap
import numba
import distython


@numba.njit()
def heom(x, y):
    results_array = np.zeros(x.shape)
    results_array[categorical_ix] = np.not_equal(x[categorical_ix], y[categorical_ix]) * 1  # use "* 1" to convert it into int
    # results_array[numerical_ix] = np.abs(x[numerical_ix] - y[numerical_ix]) / norm_range[numerical_ix]
    results_array[numerical_ix] = np.dot(x[numerical_ix], y[numerical_ix]) / (np.linalg.norm(x[numerical_ix]) * np.linalg.norm(y[numerical_ix]))
    return np.sum(np.square(results_array))


tidy_data = pd.read_csv('vitalsing_data.csv')
print(tidy_data.shape)
X_data = tidy_data.drop(['ID', 'CHT_NO', 'admin_date', 'discharge_date',
                         'AllMortality', 'CVDeath  ', 'Death Date', 'SurvivalWeeks'], axis=1)
y_data = tidy_data[['SurvivalWeeks']]
y_data = (y_data < 24).astype(int)

# remove constant features
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0)
selector.fit(X_data)
X_data = X_data[X_data.columns[selector.get_support(indices=True)]]


categorical_ix = np.array([0, 2, 3, 4, 5, 6, 7, 8])
categorical_columns = X_data.columns[categorical_ix].values
numerical_columns = np.setdiff1d(X_data.columns, categorical_columns)
numerical_ix = np.array([X_data.columns.get_loc(c) for c in numerical_columns])

X_data[numerical_columns] = StandardScaler().fit_transform(X_data[numerical_columns])
norm_range = np.array(np.nanmax(X_data.values, axis=0) - np.nanmin(X_data.values, axis=0))


reducer = umap.UMAP(metric=heom, random_state=369)

umap_heom_embedding = reducer.fit_transform(X_data)

plt.clf()
plt.scatter(
    umap_heom_embedding[:, 0],
    umap_heom_embedding[:, 1],
    c=y_data.values.astype(int), s=1, cmap='Spectral')
plt.gca().set_aspect('equal', 'datalim')

plt.show()
print(umap_heom_embedding)
