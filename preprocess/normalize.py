class Normalize:

  def __init__(self):
    from sklearn.preprocessing import StandardScaler
    self.scaler = StandardScaler()
    return

  def get_normalized(self, data):
    if(data.select_dtypes(include=['float64','int64','uint8']).columns.size != data.columns.size):
      print("Normalization Error: Non-numeric types in dataset")
      return
    self.scaler.fit(data)
    return self.scaler.transform(data)

  def get_denormalized(self, data):
    return self.scaler.inverse_transform(data)


