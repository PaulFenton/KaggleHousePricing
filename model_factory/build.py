
# gradient boosting machine with simple trees (xgboost) -------------

import xgboost as xgb

def xgboost_regressor():
    model = xgb.XGBRegressor(
      colsample_bytree=0.2,
      gamma=0.0,
      learning_rate=0.02,
      max_depth=3,
      min_child_weight=1.5,
      n_estimators=7200,
      reg_alpha=0.9,
      reg_lambda=0.6,
      subsample=0.2,
      seed=42,
      silent=1)
    return model


# General Linear Model ---------------------------------------------

from sklearn.linear_model import LinearRegression

def general_linear_model():
    model = LinearRegression(fit_intercept=false)
    return model
