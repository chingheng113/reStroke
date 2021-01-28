import distython
import numba
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler



@numba.njit()
def heom(x, y):
    results_array = np.zeros(x.shape)

    # # Get indices for missing values, if any
    # nan_x_ix = np.flatnonzero(np.logical_or(np.isin(x, self.nan_eqvs), np.isnan(x)))
    # nan_y_ix = np.flatnonzero(np.logical_or(np.isin(y, self.nan_eqvs), np.isnan(y)))
    # nan_ix = np.unique(np.concatenate((nan_x_ix, nan_y_ix)))
    # # Calculate the distance for missing values elements
    # results_array[nan_ix] = 1

    results_array[categorical_ix] = np.not_equal(x[categorical_ix], y[categorical_ix]) * 1  # use "* 1" to convert it into int
    results_array[numerical_ix] = np.abs(x[numerical_ix] - y[numerical_ix]) / norm_range[numerical_ix]
    return np.sum(np.square(results_array))





tidy_data = pd.read_csv('tidy.csv')
X_data = tidy_data.drop(['CHT_No', 'reStroke'], axis=1)
X_data = X_data.drop(['Adm_AF_0otEKG', 'EKG_AF', 'Adm_AntiCO'], axis=1) # highly related to AF
y_data = tidy_data[['reStroke']]

# remove constant features
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0)
selector.fit(X_data)
X_data = X_data[X_data.columns[selector.get_support(indices=True)]]


categorical_ix = np.array([0, 2, 3, 4, 5, 6, 7, 8, 34, 35, 36, 41, 42, 43, 44, 46, 47, 48, 49, 51])
categorical_columns = X_data.columns[categorical_ix].values
numerical_columns = np.setdiff1d(X_data.columns, categorical_columns)
numerical_ix = np.array([X_data.columns.get_loc(c) for c in numerical_columns])

X_data[numerical_columns] = StandardScaler().fit_transform(X_data[numerical_columns])
norm_range = np.array(np.nanmax(X_data.values, axis=0) - np.nanmin(X_data.values, axis=0))


heom_metric = distython.HEOM(X_data, categorical_ix, nan_equivalents=[np.nan])

a = X_data.values[1,:]
b = X_data.values[2,:]
c = heom(a, b)
d = heom_metric.heom(a, b)
print('done')
