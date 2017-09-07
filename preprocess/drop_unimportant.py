def simple(data):
  before = data.columns.size
  data = data.drop(['MiscFeature', 'MiscVal', 'Utilities', 'RoofMatl', 'Fence'], axis=1)
  print("Dropped " + str(before - data.columns.size) + " unnecessary columns.")
  return data
