import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt

import preprocess.fill_missing_data
import preprocess.drop_unimportant
import preprocess.remap_categories
import preprocess.one_hot_encoding
import preprocess.skew
import model_factory.xgboost
import explore.plot_histograms

PLOT_SKEW = False
PLOT_PREDICTIONS = False

class housing_data:

    def __init__(self):
      self.skew = preprocess.skew.Skew()
      return

    def get_preprocessed_data(self):

      # train = pd.read_csv("C:/Users/paul/Desktop/Kaggle/KaggleHousePricingNew/competition/train.csv");
      # test = pd.read_csv("C:/Users/paul/Desktop/Kaggle/KaggleHousePricingNew/competition/train.csv");
      train = pd.read_csv("./competition/train.csv")
      test = pd.read_csv("./competition/test.csv")

      x_train = train.drop(['SalePrice'], axis=1)
      y_train = train['SalePrice']
      #x_test = test.drop(['SalePrice'], axis=1)
      x_test = test

      # put together the data for common preprocessing
      x_combi = pd.concat([x_train, x_test])

      # remove missing values for each

      x_combi = preprocess.fill_missing_data.fill(x_combi)
      print("combi has " + str(x_combi.columns.size) + " columns")
      # convert incorrectly typed categorical variables
      x_combi = preprocess.remap_categories.remap(x_combi)
      x_combi = preprocess.drop_unimportant.simple(x_combi)
      print("combi has " + str(x_combi.columns.size) + " columns")

      # log transform the numerical features (and salesprice)
      if PLOT_SKEW:
        explore.plot_histograms.plot(x_combi.select_dtypes(include=['int64', 'float64']))
      print("combi has " + str(x_combi.columns.size) + " columns")

      x_combi, y_train = self.skew.get_deskewed(x_combi, y_train)
      print("combi has " + str(x_combi.columns.size) + " columns")
      if PLOT_SKEW:
        explore.plot_histograms.plot(x_combi.select_dtypes(include=['int64', 'float64']))

      print("combi has " + str(x_combi.columns.size) + " columns")
      # use one-hot encoding for the remaining categorical variables
      x_combi = preprocess.one_hot_encoding.encode(x_combi)
      print("combi has " + str(x_combi.columns.size) + " columns")

      #complete pre-processing, splitting back x_combi
      splitind = y_train.count()

      x_train = x_combi[: splitind]
      x_test = x_combi[splitind :]

      return x_train, x_test, y_train

    def get_preprocessed_skewed_data(self, x_train, x_test, y_train, y_test):
      # put together the data for common preprocessing
      x_combi = pd.concat([x_train, x_test])
      splitind = y_train.count()
      y_combi = pd.concat([y_train, y_test])

      # re-skew the data
      x_combi, y_combi = self.skew.get_skewed(x_combi, y_combi)

      # complete pre-processing, splitting back x_combi
      x_train = x_combi[: splitind]
      x_test = x_combi[splitind :]
      y_train = y_combi[: splitind]
      y_test = y_combi[splitind :]

      return x_train, x_test, y_train, y_test
