
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error

class xgboost_model:
  def __init__(self):
    self.regr = xgb.XGBRegressor(
                 colsample_bytree=0.2,
                 gamma=0.0,
                 learning_rate=0.01,
                 max_depth=4,
                 min_child_weight=1.5,
                 n_estimators=7200,
                 reg_alpha=0.9,
                 reg_lambda=0.6,
                 subsample=0.2,
                 seed=42,
                 silent=1)
    return

  def build(self, train):
    # build the model
    #label_df = pd.DataFrame(index = train.index, columns=['SalePrice'])
    self.regr.fit(train.drop(['SalePrice'], axis=1), train['SalePrice'])
    # print out some stats based on model prediction of the training data
    train_pred = self.regr.predict(train.drop(['SalePrice'], axis=1))
    print("xgboost score in training set: ", np.sqrt(mean_squared_error(train['SalePrice'], train_pred)))

    return

  def predict(self, test):
    predictions = self.regr.predict(test)
    return predictions
