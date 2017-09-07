import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt

def plot(data):
  # fail if there are columns of the wrong data type
  if(data.select_dtypes(include=['float64','int64']).columns.size != data.columns.size):
    print("Error: Non-numeric columns found in dataset.")
    return

  # determine sizing for plot
  tiledimension = math.ceil(math.sqrt(data.columns.size))
  sns.set(style="white", palette="muted", color_codes=True)
  f, axes = plt.subplots(tiledimension, tiledimension, figsize=(7,7), sharex=False)
  sns.despine(left=True)

  # build each plot
  for i in range(0, tiledimension):
    for j in range(0, tiledimension):
      column_ind = i*tiledimension + j
      if(column_ind < data.columns.size):
        sns.distplot(data.iloc[:,column_ind], color="m", ax=axes[i, j])

  plt.setp(axes, yticks=[])
  plt.tight_layout()
  plt.show()
  return
