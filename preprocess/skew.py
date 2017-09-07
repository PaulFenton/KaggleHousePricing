from scipy.stats import skew
import pandas as pd
import numpy as np

class Skew:
  skewed_feats = pd.Series
  def __init__(self):
    return

  def get_deskewed(self, data):
    #first deskew the target data
    #print("de-skewing SalePrice")
    #data['SalePrice'] = np.log1p(data['SalePrice'])

    numerical = data.select_dtypes(include=['int64', 'float64'])

    self.skewed_feats = numerical.apply(lambda x: skew(x.dropna()))  # compute skewness
    self.skewed_feats = self.skewed_feats[self.skewed_feats > 0.75]
    self.skewed_feats = self.skewed_feats.index

    print("de-skewing " + str(self.skewed_feats.size) + " continuous features")
    #numerical[self.skewed_feats] = np.log1p(numerical[self.skewed_feats])
    data[self.skewed_feats] = np.log1p(data[self.skewed_feats])
    return data

  def get_skewed(self, data):
    # first deskew the target data
    #print("re-skewing SalePrice")
    #data = np.expm1(data)

    print("re-skewing " + str(self.skewed_feats.size) + " features")
    data[self.skewed_feats] = np.expm1(data[self.skewed_feats])
    return data
