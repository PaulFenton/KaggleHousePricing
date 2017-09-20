import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import ShuffleSplit

def report_error():
  RMSE = mean_squared_error(y, y_pred) ** 0.5


def plot_xgbregressor_importances(regr, num_importances):
  scores = regr.booster().get_fscore()
  scores_df = pd.DataFrame.from_dict(scores, orient='index')
  scores_df.columns = ['fscore']

  scores_sorted = scores_df.sort_values('fscore', ascending=False)
  scores_sorted['Index'] = scores_sorted.index
  sns.color_palette("Paired")
  sns.barplot(y="Index", x="fscore", data=scores_sorted.head(num_importances))
  plt.show()

def cross_validate_shufflesplit(x_train, x_test, y_train, model):
    ss = ShuffleSplit(n_splits=10, test_size=0.25, random_state=137)

    # perform the cross validation for each split
    for train_index , test_index in ss.split(x_train.index):
        #subset the training and test data
        sub_x_train = x_train[x_train.index.isin(train_index)]
        sub_y_train = y_train[y_train.index.isin(train_index)]
        sub_x_test = x_train[x_train.index.isin(test_index)]
        sub_y_test = y_train[y_train.index.isin(test_index)]

        print("Train shape:", sub_x_train.shape, "TEST shape:", sub_x_test.shape)
        model.fit(sub_x_train.drop('Id', axis=1), sub_y_train)
        print("The fitted xgboost model has RSME: " + str(
          mean_squared_error(sub_y_test, pd.Series(model.predict(sub_x_test.drop('Id', axis=1)))) ** 0.5))
    return
