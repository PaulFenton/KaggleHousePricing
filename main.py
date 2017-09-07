import pandas as pd
import preprocess.fill_missing_data
import preprocess.remap_categories
import preprocess.skew
import preprocess.one_hot_encoding
import preprocess.normalize
import preprocess.drop_unimportant
import model.xgboost
import explore.plot_histograms

import math
import seaborn as sns
import matplotlib.pyplot as plt

PLOT_SKEW = False
PLOT_PREDICTIONS = True

#train = pd.read_csv("C:/Users/paul/Desktop/Kaggle/KaggleHousePricingNew/competition/train.csv");
#test = pd.read_csv("C:/Users/paul/Desktop/Kaggle/KaggleHousePricingNew/competition/train.csv");
train = pd.read_csv("./competition/train.csv")
test = pd.read_csv("./competition/test.csv")
combi = pd.concat([train, test])

# remove missing values for each

combi = preprocess.fill_missing_data.fill(combi)
print("combi has " + str(combi.columns.size) + " columns")
# convert incorrectly typed categorical variables
combi = preprocess.remap_categories.remap(combi)
combi = preprocess.drop_unimportant.simple(combi)
print("combi has " + str(combi.columns.size) + " columns")

# log transform the numerical features (and salesprice)
if PLOT_SKEW:
    explore.plot_histograms.plot(combi[combi['SalePrice'].notnull()].select_dtypes(include=['int64', 'float64']))
print("combi has " + str(combi.columns.size) + " columns")
skew = preprocess.skew.Skew()
combi = skew.get_deskewed(combi)
print("combi has " + str(combi.columns.size) + " columns")
if PLOT_SKEW:
    explore.plot_histograms.plot(combi[combi['SalePrice'].notnull()].select_dtypes(include=['int64', 'float64']))

print("combi has " + str(combi.columns.size) + " columns")
# use one-hot encoding for the remaining categorical variables
combi = preprocess.one_hot_encoding.encode(combi)
print("combi has " + str(combi.columns.size) + " columns")
# apply normalization/scaling
#scaler = preprocess.normalize.Normalize()
#combi = scaler.get_normalized(combi)

# fit model
train_transformed = combi[combi['SalePrice'].notnull()]
test_transformed = combi[combi['SalePrice'].isnull()]
model = model.xgboost.xgboost_model()
model.build(train_transformed)
print("combi has " + str(combi.columns.size) + " columns")
# make test predictions
test_transformed['SalePrice'] = model.predict(test_transformed)

# descale / denormalize
#descaled = scaler.get_denormalized(predictions)

# inverse log transform
train_final = skew.get_skewed(train_transformed)
test_final = skew.get_skewed(test_transformed)

# plot the predictions if requested
if PLOT_PREDICTIONS:
    print("coming soon")
    sns.distplot(train_final['SalePrice'])
    sns.distplot(test_final['SalePrice'], color='g')
    plt.show()

# output results
test_final.to_csv('./submissions/predictions.csv', columns=['Id', 'SalePrice'])
