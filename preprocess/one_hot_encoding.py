import pandas as pd

def encode(data):
  cols = data.select_dtypes(include=['object'])
  oldColCount = data.columns.size

  # perform the one-hot encoding with pandas
  data = pd.get_dummies(data, columns = cols, drop_first=False)

  print("Replaced " + str(cols.columns.size) + " categorical variables with " + str(data.columns.size - oldColCount + cols.columns.size) + " dummy variables")

  return data
