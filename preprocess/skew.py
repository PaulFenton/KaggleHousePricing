from scipy.stats import skew
import pandas as pd
import numpy as np
SKEW_THRESHOLD = 0.75

class Skew:
  skewed_feats = pd.Series
  skewed_labels = False
  def __init__(self):
    return

  def get_deskewed(self, x_data, y_data):
    #first deskew the target data
    #print("de-skewing SalePrice")
    #data['SalePrice'] = np.log1p(data['SalePrice'])


    # deskew x_data
    self.skewed_feats = x_data.select_dtypes(include=['int64', 'float64']).apply(lambda x: skew(x.dropna()))  # compute skewness
    self.skewed_feats = self.skewed_feats[self.skewed_feats > SKEW_THRESHOLD]
    self.skewed_feats = self.skewed_feats.index
    print("de-skewing " + str(self.skewed_feats.size) + " continuous features")
    #numerical[self.skewed_feats] = np.log1p(numerical[self.skewed_feats])
    x_data[self.skewed_feats] = np.log1p(x_data[self.skewed_feats])

    # deskew y_data
    skew_amount = skew(y_data)
    if skew_amount > SKEW_THRESHOLD:
        self.skewed_labels = True
        print("de-skewing y labels")
        y_data = np.log1p(y_data)

    return x_data, y_data

  def get_skewed(self, x_data, y_data):
    # first deskew the target data
    #print("re-skewing SalePrice")
    #data = np.expm1(data)

    # re-skew x data
    print("re-skewing " + str(self.skewed_feats.size) + " features")
    x_data[self.skewed_feats] = np.expm1(x_data[self.skewed_feats])

    # re-skew y data
    if self.skewed_labels:
        print("re-skewing y labels")
        y_data = np.expm1(y_data)

    return x_data, y_data
