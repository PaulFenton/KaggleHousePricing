from sklearn.model_selection import train_test_split
import preprocess.prepare_housing_data as pre
import model_factory.xgboost
import pandas as pd
from sklearn.metrics import mean_squared_error

import math
import seaborn as sns
import matplotlib.pyplot as plt

# 1 to 100 random number sequence from RANDOM.ORG for repeatable splits in train_test_split
RAND_SEEDS = [76,	37,	5,	35,	17,	24,	96,	10,	91,	46,	67,	100,	80,	31,	2,	11,	19,	32,	47,	8,
              60,	73,	94,	6,	49,	70,	89,	87,	66,	97,	98,	64,	29,	39,	83,	30,	15,	72,	25,	27,
              59,	21,	82,	16,	78,	55,	93,	42,	13,	44,	85,	71,	36,	14,	92,	4,	28,	41,	77,	81,
              33,	75,	38,	40,	86,	18,	50,	69,	22,	56,	74,	12,	95,	63,	26,	43,	61,	1,	65,	34,
              23,	62,	84,	9,	3,	52,	48,	79,	99,	90,	53,	57,	58,	45,	68,	20,	7,	54,	88,	51]

TEST_FRACTION = 0.3

housing = pre.housing_data()
x_train, x_test, y_train = housing.get_preprocessed_data()

#scoring
means = pd.Series()
stds = pd.Series()
xaxis = pd.Series()
data = pd.DataFrame(columns=['frac', 'err'])
for n in range(0, 1):
    scores = pd.Series()
    #learning_rate = 0.01 + n*0.02
    #xaxis.set_value(n, learning_rate)
    #print("evaluating learning_rate=" + str(learning_rate))
    for i in range(0, 10):
        #subset the training data for this iteration's training and testing
        print("seed " + str(RAND_SEEDS[i]))
        sub_x_train, sub_x_test, sub_y_train, sub_y_test = train_test_split(x_train, y_train,
                                                                            test_size=TEST_FRACTION,
                                                                            random_state=RAND_SEEDS[i])

        #train the model
        model = model_factory.xgboost.xgboost_model(0.05, 8)
        model.build(sub_x_train, sub_y_train, plot=False)

        #evaluate the model
        predictions = pd.Series(model.predict(sub_x_test))

        #score the model and save the result
        err = mean_squared_error(sub_y_test, predictions)
        scores.set_value(i, err)
        newrowid = len(data)
        data.set_value(newrowid, 'frac', n)
        data.set_value(newrowid, 'err', err)

    # calculate the average score
    print("The average score for n=" + str(n) + " was: " + str(scores.mean()))
    means.set_value(n, scores.mean())
    print("The standard deviation for n=" + str(n) + " was: " + str(scores.std()))
    stds.set_value(n, scores.std())
