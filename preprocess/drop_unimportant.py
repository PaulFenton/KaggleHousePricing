import pandas as pd

def simple(data):
  before = data.columns.size
  data = data.drop(['MiscFeature', 'MiscVal', 'Utilities', 'RoofMatl', 'Fence'], axis=1)
  print("Dropped " + str(before - data.columns.size) + " unnecessary columns.")
  return data

def remove_outliers(x_train, y_train):

  #combine
  combi = pd.concat([x_train, y_train], axis=1)

  #remove houses with SF > 4000 within the training data set
  before = combi['Id'].count()
  combi = combi.loc[(combi['GrLivArea'] < 4000) | (combi['SalePrice'] > 700000), :]
  after = combi['Id'].count()
  print("Removed " + str(before - after) + " outliers")

  #split up data
  x_train = combi.drop('SalePrice', axis=1)
  y_train = combi['SalePrice']

  return x_train, y_train
