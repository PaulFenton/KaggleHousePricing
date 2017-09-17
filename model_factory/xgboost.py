import numpy as np
import pandas as pd
import xgboost as xgb
from xgboost import plot_tree
from xgboost import plot_importance
import math
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

PLOT_IMPORTANCE = True
NUM_IMPORTANCES = 20

class xgboost_model:
  def __init__(self, learning_rate, depth):
    self.regr = xgb.XGBRegressor(
                 colsample_bytree=0.2,
                 gamma=0.0,
                 learning_rate=learning_rate,
                 max_depth=3,
                 min_child_weight=1.5,
                 n_estimators=7200,
                 reg_alpha=0.9,
                 reg_lambda=0.6,
                 subsample=0.2,
                 seed=42,
                 silent=1)
    return

  def fit(self, x_train, y_train, plot=False):
    # build the model
    #label_df = pd.DataFrame(index = train.index, columns=['SalePrice'])
    self.regr.fit(x_train.drop('Id', axis=1), y_train)

    if plot:
        print("xgboost score in training set: ", np.sqrt(mean_squared_error(y_train, train_pred)))
        scores = self.regr.booster().get_fscore()
        scores_df = pd.DataFrame.from_dict(scores, orient='index')
        scores_df.columns = ['fscore']

        scores_sorted = scores_df.sort_values('fscore', ascending=False)
        scores_sorted['Index'] = scores_sorted.index
        sns.color_palette("Paired")
        sns.barplot(y="Index", x="fscore", data=scores_sorted.head(NUM_IMPORTANCES))
        plt.show()
    return

  def predict(self, x_test):
    predictions = self.regr.predict(x_test.drop('Id', axis=1))
    return predictions

  def get_model(self):
      return self.regr

  def feat_imp(self, df, model, n_features):

      d = dict(zip(df.columns, model.booster().get_score(importance_type='weight')))
      ss = sorted(d, key=d.get, reverse=True)
      top_names = ss[0:n_features]

      plt.figure(figsize=(15,15))
      plt.title("Feature importances")
      plt.bar(range(n_features), [d[i] for i in top_names], color="r", align="center")
      plt.xlim(-1, n_features)
      plt.xticks(range(n_features), top_names, rotation='vertical')
      return
