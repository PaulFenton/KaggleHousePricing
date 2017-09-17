import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def report_error():
    return


def plot_xgbregressor_importances(regr, num_importances):
  scores = regr.booster().get_fscore()
  scores_df = pd.DataFrame.from_dict(scores, orient='index')
  scores_df.columns = ['fscore']

  scores_sorted = scores_df.sort_values('fscore', ascending=False)
  scores_sorted['Index'] = scores_sorted.index
  sns.color_palette("Paired")
  sns.barplot(y="Index", x="fscore", data=scores_sorted.head(num_importances))
  plt.show()
