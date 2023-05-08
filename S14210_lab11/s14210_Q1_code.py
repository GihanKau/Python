'''
Author  : B.M.G.G.K. Rajapaksha
Date    : 27/12/21
Topic   : Use scikit-learn package to implement an Artificial Neural Network (ANN)
          using iris data
Input   : iris dataset as iris.csv format

Output  : Trained ANN for predict species

'''
import random

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt

# Question 1)

# I.I

iris_data = pd.read_csv('iris.csv')
flower_data = iris_data.iloc[:, [0, 1, 2, 3]]
species_labels = iris_data.iloc[:, [4]]
# flower_data = iris_data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
# species_labels = iris_data[['variety']]

X = flower_data
y = species_labels

# I.II
# Output the categorical values
print('Categorical y values : \n', y, '\n')

# To select unique categorical values from the y

# numerical labels for y
le = preprocessing.LabelEncoder()
num_y_labels = le.fit(y).transform(y)

# print numerical y labels
print('Numerical y values : \n', num_y_labels, '\n')

# unique = dataframe.col_name.unique()
unique_cat_labels = y.variety.unique()
unique_num_labels = pd.unique(num_y_labels)

print('Unique categorical y variables : \n', unique_cat_labels, '\n')
print('Unique numerical y variables : \n', unique_num_labels, '\n')

# I.III

# to maintain same dataset while running
import numpy as np
np.random.seed(30)

# Split the X and y dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, num_y_labels, test_size=0.2)


# I.IV
# Standardizing the X and y variables

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(flower_data)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# II
# ---------------------------------------- KNN ----------------------------------------

# ------------------------------- 3 layers, 10 neurons for each -------------------------------

# Multilayer perceptron classifier
from sklearn.neural_network import MLPClassifier

# Three hidden layers, 10 neurons per each

mlpc = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)

# Train the algorithm
mlpc.fit(X_train, y_train)

# Predictions for test data
predictions = mlpc.predict(X_test)

# III
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Confusion matrix
cm = confusion_matrix(y_test, predictions)
print('Confusion matrix : \n', cm, '\n')

# Confusion matrix plot
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=unique_cat_labels)
disp.plot()
plt.show()

# Classification report
target_names = ['Setosa 0', 'Versicolor 1', 'Virginica 2']
print('Classification report : \n', classification_report(y_test, predictions, target_names=target_names))


# IV
# ----------------------------------------- Student dataset -------------------------------------------

# new plant data
plant_data = [[5.9, 3.0, 7.0, 5.0], [4.6, 3.0, 1.5, 0.2], [6.2, 3.0, 4.1, 1.2]]

# Standardize new plant data

plant_data_sd = scaler.transform(plant_data)

predictions = mlpc.predict(plant_data_sd)

print('Predicted labels for new 3 plants : \n',
      'Plant 1 = ', predictions[0], '\n',
      'Plant 2 = ', predictions[1], '\n',
      'Plant 3 = ', predictions[2], '\n',)

print('Predicted species for new 3 plants : \n',
      'Plant 1 = ', le.inverse_transform(predictions)[0], '\n',
      'Plant 2 = ', le.inverse_transform(predictions)[1], '\n',
      'Plant 3 = ', le.inverse_transform(predictions)[2], '\n',)

# V
# ------------------------------- 3 layers, 2 neurons for each -------------------------------

# Multilayer perceptron classifier
from sklearn.neural_network import MLPClassifier

# three hidden layers, 2 neurons per each

mlpc = MLPClassifier(hidden_layer_sizes=(2, 2, 2), max_iter=1000)

# Train the algorithm
mlpc.fit(X_train, y_train)

# Predictions for test data
predictions = mlpc.predict(X_test)

# III
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Confusion matrix
cm = confusion_matrix(y_test, predictions)
print('Confusion matrix : \n', cm, '\n')

# Confusion matrix plot
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=unique_cat_labels)
disp.plot()
plt.show()

# Classification report
target_names = ['Setosa 0', 'Versicolor 1', 'Virginica 2']
print('Classification report : \n', classification_report(y_test, predictions, target_names=target_names))
