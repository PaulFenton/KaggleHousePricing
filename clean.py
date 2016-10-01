import pandas as pd
import numpy as np

FILEPATH = 'C:/Users/paul/Desktop/Kaggle/Housing/'

MISSING_THRESHOLD = 0.75 #delete all data columns missing more than this number of entries


def housing_clean():
  print("Reading data...")
  train = pd.read_csv(FILEPATH + "train.csv")
  test = pd.read_csv(FILEPATH + "test.csv")
  test['SalePrice'] = np.nan  # create SalePrice column for test and fill with NA's
  combi = pd.concat([train, test])  # combine train and test data to ensure consistent cleaning / calculated columns

  #drop columns with more than threshold missing values
  droplist = list()
  for col in list(combi.columns):
    missing_proportion = 1 - (combi[col].count() / combi['Id'].count())
    if missing_proportion >= MISSING_THRESHOLD:
      print("Rejecting " + col)
      print(missing_proportion)
      droplist.append(col)

  #drop columns

  #clean up integer columns by replacing NA's with the median
  for col in list(combi.select_dtypes(include=['int64']).columns):
    combi[col] = combi[col].fillna(combi[col].median())

  #clean up float columns by replacing NA's with the average
  for col in list(combi.select_dtypes(include=['float64']).columns):
    combi[col] = combi[col].fillna(combi[col].mean())

  #clean up categorical variables by replacing NA's with new 'Missing' category
  for col in list(combi.select_dtypes(include=['object']).columns):
    combi[col] = combi[col].fillna('Missing')

  return combi

data = housing_clean()

