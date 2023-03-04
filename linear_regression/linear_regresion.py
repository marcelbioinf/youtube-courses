import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt
import pickle
from sklearn.utils import shuffle
from matplotlib import style

data = pd.read_csv("./student/student-mat.csv", sep=';')
data = data[['age', 'G2', 'G3', 'studytime', 'absences', 'failures']]

predict = 'G3'
X = np.array(data.drop(columns=[predict]))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

''' we can comment it because we need to do the training only once, and then its saved with pickle
best = 0
for _ in range(40):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)
    print(accuracy)

    if accuracy > best:
        best = accuracy
        with open("studentmodel.pickle", "wb") as f:  #this saves our model into specific file
            pickle.dump(linear, f)
'''

pickle_in = open("studentmodel.pickle", 'rb')
linear = pickle.load(pickle_in)

print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

p = 'G2'
style.use("ggplot")
plt.scatter(data[p], data['G3'])
plt.xlabel(p)
plt.ylabel('Final grade')
plt.show()