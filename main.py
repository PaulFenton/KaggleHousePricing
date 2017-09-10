from sklearn.model_selection import train_test_split
import preprocess.prepare_housing_data as pre
import model_factory.xgboost
import pandas as pd
from sklearn.metrics import mean_squared_error


housing = pre.housing_data()
x_train, x_test, y_train = housing.get_preprocessed_data()

print(str(type(x_train)) + str(type(x_test)) + str(type(y_train)))

#scoring

# for n in range(1, 10):
#     scores = []
#     for i in range(0, 100):
#         #subset the training data for this iteration's training and testing
#         sub_x_train, sub_x_test, sub_y_train, sub_y_test = train_test_split(x_train, y_train, test_size=0.3)
#
#         #train the model
#         model = model_factory.xgboost.xgboost_model(n)
#         model.build(sub_x_train, sub_y_train)
#
#         #evaluate the model
#         predictions = model.predict(sub_x_test)
#
#         #score the model and save the result
#         err = mean_squared_error(sub_y_test, predictions)
#         scores.append(err)
#
#     print("Scores: " + str(scores))
#     # calculate the average score
#     print("The average score for n=" + str(n) + " was: " + str(sum(scores)/len(scores)))


# build the xgboost model
model = model_factory.xgboost.xgboost_model(8)
model.build(x_train, y_train)

# predict y_test from x_test0
y_test = pd.Series(model.predict(x_test))

# inverse transform of the deskew
print(str(type(x_train)) + str(type(x_test)) + str(type(y_train)) + str(type(y_test)))
x_train_final, x_test_final , y_train_final, y_test_final = housing.get_preprocessed_skewed_data(x_train, x_test, y_train, y_test)

# print out the submission dataframe to .csv
final_df = pd.DataFrame(y_test_final, columns=['SalePrice'])
output = pd.concat([x_test_final['Id'], final_df], axis=1)
output.to_csv('./submissions/predictions.csv', columns=['Id', 'SalePrice'], index=False)
