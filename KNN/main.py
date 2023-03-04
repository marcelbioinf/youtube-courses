import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv('./car.data', sep=',')

le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data['buying']))
maint = le.fit_transform(list(data['maint']))
door = le.fit_transform(list(data['door']))
persons = le.fit_transform(list(data['persons']))
lug_boot = le.fit_transform(list(data['lug_boot']))
safety = le.fit_transform(list(data['safety']))
cls = le.fit_transform(list(data['class']))

predict = 'class'

X = list(zip(buying, maint, door, persons, lug_boot, safety))
Y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)
print(accuracy)

predicted = model.predict(x_test)

for x in range(len(predicted)):
    print(f'predicted: {predicted[x]}  Data {x_test[x]}  Actual {y_test[x]}')
    n = model.kneighbors([x_test[x]], 5, True)  #zwraca dystanse między sasiadami i ich numery wierchołków
    print("N: ", n)