from sklearn.datasets import load_iris


iris = load_iris()
#print(dir(iris.data))
print(f"IRIS Data :{iris.data}")

numSamples, numFeatures = iris.data.shape

print(numSamples)
print(numFeatures)
print(f"\nList Target Name :{list(iris.target_names)}\n")
print(f"Targets          :{iris.target}")

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)

import xgboost as xgb

train = xgb.DMatrix(X_train, label=y_train)
test = xgb.DMatrix(X_test, label=y_test)

param = {
    'max_depth': 4,
    'eta': 0.3,
    'objective': 'multi:softmax',
    'num_class': 3} 
epochs = 10 

model = xgb.train(param, train, epochs)

predictions = model.predict(test)
print(f"Predictions: {predictions}")

from sklearn.metrics import accuracy_score

accuracy_score(y_test, predictions)
print(f"Accuracy Score: {accuracy_score(y_test, predictions)}")
