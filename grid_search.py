from sklearn.model_selection import train_test_split
import preprocess.prepare_housing_data as pre
import model_factory.build
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV

import math
import seaborn as sns
import matplotlib.pyplot as plt

# prepare the data
housing = pre.housing_data()
x_train, x_test, y_train = housing.get_preprocessed_data()

# build the xgboost model with tuned parameters learning rate and max depth
model = model_factory.build.xgboost_regressor()

# set the hyperparameters to be explored

# test 1: best was 'learning_rate': 0.05, 'max_depth': 3, 'n_estimators': 2000
#n_estimators = [100, 500, 1000, 1500, 2000]
#max_depth = [3 , 5, 7, 9]
#learning_rate = [0.01, 0.05, 0.1, 0.15, 0.2]

# test 2: Best: -0.013534 using {'learning_rate': 0.03, 'max_depth': 2, 'n_estimators': 5000}
#n_estimators = [2000, 2500, 3000, 5000]
#max_depth = [2, 3, 4]
#learning_rate = [0.03, 0.05, 0.07]

# test 3 Best: -0.012892 using {'learning_rate': 0.02, 'max_depth': 3, 'n_estimators': 7000}
n_estimators = [4000, 5000, 6000, 7000]
max_depth = [1, 2, 3]
learning_rate = [0.02, 0.03, 0.04]

param_grid = dict(n_estimators=n_estimators, max_depth=max_depth, learning_rate=learning_rate)
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=7)
grid_search = GridSearchCV(model, param_grid, scoring="neg_mean_squared_error", n_jobs=1, cv=kfold, verbose=1)
grid_result = grid_search.fit(x_train.drop('Id', axis=1), y_train)

print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
	print("%f (%f) with: %r" % (mean, stdev, param))
