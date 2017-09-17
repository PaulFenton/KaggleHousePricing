from sklearn.model_selection import train_test_split
import preprocess.prepare_housing_data as pre
import model_factory.build
import pandas as pd
import explore.importances

from sklearn.metrics import mean_squared_error

import math
import seaborn as sns
import matplotlib.pyplot as plt

PLOT = True

# prepare the data
housing = pre.housing_data()
x_train, x_test, y_train = housing.get_preprocessed_data(PLOT)

# build the xgboost model with tuned parameters learning rate and max depth
model = model_factory.build.xgboost_regressor()
model.fit(x_train.drop('Id', axis=1), y_train)
if PLOT:
    explore.importances.plot_xgbregressor_importances(model, 20)

# predict y_test from x_test0
y_test = pd.Series(model.predict(x_test.drop('Id', axis=1)))

# inverse transform of the deskew
x_train_final, x_test_final , y_train_final, y_test_final = housing.get_preprocessed_skewed_data(x_train, x_test, y_train, y_test)

# print out the submission dataframe to .csv
final_df = pd.DataFrame(y_test_final, columns=['SalePrice'])
output = pd.concat([x_test_final['Id'], final_df], axis=1)
output.to_csv('./submissions/predictions.csv', columns=['Id', 'SalePrice'], index=False)
