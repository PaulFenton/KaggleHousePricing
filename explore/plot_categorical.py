import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt

def countplot_subplots(data):
    # warn about numerical columns
    data = subset_categorical(data)

    # determine sizing for plot
    tiledimension = math.ceil(math.sqrt(data.columns.size))
    sns.set(style="white", palette="muted", color_codes=True)
    f, axes = plt.subplots(tiledimension, tiledimension, figsize=(7,7), sharex=False)
    sns.despine(left=True)

    # build each plot
    for i in range(0, tiledimension):
        for j in range(0, tiledimension):
            column_ind = i*tiledimension + j
            if column_ind < data.columns.size:
                sns.countplot(data[data.columns[column_ind]], ax=axes[i, j])
            #rotate the labels
            for tick in axes[i, j].get_xticklabels():
                tick.set_rotation(45)


    plt.setp(axes, yticks=[])
    plt.tight_layout()
    plt.show()
    return

def violin_subplots(data, target_column):
    HORIZONTAL_TILES = 4
    VERTICAL_TILES = 2
    if target_column not in data:
        print("Target column " + target_column + " not in dataset")
        return
    #subset dataset based on existance of target data
    targetnulls = data[target_column].isnull().sum()
    if targetnulls > 0:
        print("Subsetting the data with target nulls (removing " + str(targetnulls) + " values)")
        data = data[data[target_column].isnull() == False]
    targetdata = data[target_column]
    # warn about numerical columns
    data = subset_categorical(data)
    print("Plotting " + str(data.columns.size) + " features..")

    # determine sizing for plot
    imax = VERTICAL_TILES
    jmax = HORIZONTAL_TILES
    numplots = math.ceil(data.columns.size / (VERTICAL_TILES * HORIZONTAL_TILES))

    # build each plot
    for plotnum in range(0, numplots):
        sns.set(style="white", palette="muted", color_codes=True)
        f, axes = plt.subplots(imax, jmax, figsize=(7, 7), sharex=False)
        sns.despine(left=True)
        for i in range(0, imax):
            for j in range(0, jmax):
                column_ind = plotnum*imax*jmax + i*jmax + j
                if column_ind < data.columns.size:
                    sns.violinplot(data.columns[column_ind], targetdata, data=data, ax=axes[i, j])
                #rotate the labels
                for tick in axes[i, j].get_xticklabels():
                    tick.set_rotation(45)
        plt.setp(axes, yticks=[])
        plt.tight_layout()
        #plt.figure()

    plt.show()
    return

def subset_categorical(data):
    if data.select_dtypes(include=['object']).columns.size != data.columns.size:
      print("Error: Numeric columns found in dataset. Running on categorical subset")
      data = data.select_dtypes(include=['object'])
    return data

def plot_feature(data, feature, target):
  train = data[data[target].notnull()]
  sns.swarmplot(x=feature, y=target, data=train)
  sns.boxplot(x=feature, y=target, data=train)
  plt.figure()
  sns.countplot(data[feature])
  plt.show()
  return


