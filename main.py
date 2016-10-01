
import pandas as pd
import numpy as np
import clean
import features

#Preprocessing
data = clean.housing_clean()

#Feature Engineering
calculated_features = features.extract(data)
augmented = pd.concat([data,calculated_features], axis=1)

#Model Building

modelA = xgboost(SalesPrice~.,augmented)
modelB = testtest(SalesPrice~.,augmented)

#Tuning

#Cross Validation

#Test Prediction




