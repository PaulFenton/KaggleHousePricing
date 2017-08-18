import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from sklearn.preprocessing.data import StandardScaler
from sklearn.ensemble.forest import RandomForestRegressor
from numpy import float32
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor

# load the data
test_dataset=pd.read_csv('../competition/test.csv')
train_dataset=pd.read_csv('../competition/train.csv')

# designate the dataset subsets
X_train=train_dataset.iloc[:,1:-1].values
Y_train=train_dataset.iloc[:,80:81].values
X_test=test_dataset.iloc[:,1:].values
X=pd.concat([DataFrame(X_train),DataFrame(X_test)])

X=X.iloc[:,:].values

# remove missing values... ? what do the last 3 lines do?
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer.fit(X_train[:,2:3])
X_train[:,2:3]=imputer.transform(X_train[:,2:3])
X_test[:,2:3]=imputer.transform(X_test[:,2:3])
X[:,2:3]=imputer.transform(X[:,2:3])

X_train[:,58:59]=DataFrame(X_train[:,58:59]).fillna( value=0)
X_train=DataFrame(X_train).fillna( value='0')
X_test[:,58:59]=DataFrame(X_test[:,58:59]).fillna( value=0)
X_test=DataFrame(X_test).fillna( value='0')
X[:,58:59]=DataFrame(X[:,58:59]).fillna( value=0)
X=DataFrame(X).fillna( value='0')

X_train=DataFrame(X_train)

X_train=X_train.iloc[:,:].values
X_test=X_test.iloc[:,:].values
X=X.iloc[:,:].values

# turn the categorical variables into one-hot vectors
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
l=[1,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20,21,22,23,24,26,27,28,29,30,31,32,34,38,39,40,41,52,54,56,57,58,59,62,63,64,71,72,73,76,77,78]
for i in l:
    #print(i)
    labelencoder=LabelEncoder()
    X_train[:,i]=labelencoder.fit_transform(X_train[:,i])
    labelencoder=LabelEncoder()
    X_test[:,i]=labelencoder.fit_transform(X_test[:,i])
    X[:,i]=labelencoder.fit_transform(X[:,i])

Xt=DataFrame(X_test)

Xt=DataFrame(X_train)

onehotencoder=OneHotEncoder(categorical_features=l)
Xt=onehotencoder.fit_transform(X_train).toarray()
X_train=DataFrame(data=Xt,copy=True)
onehotencoder=OneHotEncoder(categorical_features=l)
Xc=onehotencoder.fit_transform(X_test).toarray()
X_test=DataFrame(data=Xc,copy=True)
Xc=onehotencoder.fit_transform(X).toarray()
X=DataFrame(data=Xc,copy=True)
# Apply Backward Elimination
#Apply Feature Scaling
stdScalar=StandardScaler()
X_train=stdScalar.fit_transform(X_train)
stdScalar=StandardScaler()
X_test=stdScalar.fit_transform(X_test)
X_train=DataFrame(data=X_train,copy=True)
X_test=DataFrame(data=X_test,copy=True)
X=stdScalar.fit_transform(X)
X=DataFrame(data=X,copy=True)
X_train=X.iloc[:1460,:].values
X_test=X.iloc[1460:,:].values

reg=GradientBoostingRegressor(n_estimators= 500,max_depth= 4,min_samples_split=2,
          learning_rate= 0.01,loss= 'ls')
reg.fit(X_train,DataFrame(Y_train).values.ravel())

from sklearn.metrics import mean_squared_error
from math import sqrt,log10

rms = sqrt(mean_squared_error((Y_train), (reg.predict(X_train))))
a=DataFrame()
a['Id']=test_dataset.index
a['Id']=test_dataset.iloc[:,0:1].values
a['SalePrice']=Series(np.array(reg.predict(X_test)),index=test_dataset.index)
a.to_csv('../submissions/predictions.csv',index=False)
#print(a)
