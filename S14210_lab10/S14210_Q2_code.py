'''
Author  : B.M.G.G.K. Rajapaksha
Date    : 20/12/21
Topic   : Train the KNN algorithm using the iris data set using
Input   : iris dataset in the sklearn package

Output  : 1. Indices, data values, labels species of each neighbors
          2. Predicted species of each test plants.

'''
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np

# Question 2)
# I.
# Load data
iris_data = datasets.load_iris()

# Extract the data
labels = iris_data.target
data = iris_data.data

# Standardizing the data
scaler = StandardScaler().fit(data)

# Transform the iris data
data_sd = scaler.transform(data)

# make arrays of plant 1 test data
test_data_plant1 = [[4.6, 3.0, 1.5, 0.2]]

# Standardizing the test data
test_data_plant1_sd = scaler.transform(test_data_plant1)


# make arrays of both plant 1 and 2 test data
test_data_plant1_2 = np.array([[4.6, 3.0, 1.5, 0.2], [6.2, 3.0, 4.1, 1.2]])

# Standardizing all test data

test_data_plant1_2_sd = scaler.transform(test_data_plant1_2)


# II.I

print('------------------------------------ Using sepal data --------------------------------------------')

from sklearn.neighbors import KNeighborsClassifier

sepal_data = data_sd[:, [0, 1]]

print('###### 2 nearest neighbors ######\n')

knn = KNeighborsClassifier(n_neighbors=2).fit(sepal_data, labels)
distance, indices = knn.kneighbors(test_data_plant1_sd[:, [0, 1]])
print(indices)

species = iris_data['target_names']

print("Indices : ", indices, '\n')
print("Data values : ", data[labels[indices]], '\n')
print("Species : ", species[labels[indices]], '\n')
print("Labels : ", labels[indices], '\n')

# II.II
print('###### 5 nearest neighbors ######\n')

knn = KNeighborsClassifier(n_neighbors=5).fit(sepal_data, labels)
distance, indices = knn.kneighbors(test_data_plant1_2_sd[:, [0, 1]])


pred_label = knn.predict(test_data_plant1_2_sd[:, [0, 1]])


print("Plant 1 Details : \n",  'Predicted species label for plant 1 : \n', pred_label[0], '\n\n',
                                'Predicted species for plant 1 : \n', species[pred_label][0], '\n\n')

print("Plant 2 Details : \n",   'Predicted species label for plant 1 : \n', pred_label[1], '\n\n',
                                'Predicted species for plant 1 : \n', species[pred_label][1], '\n\n')

print('Probabilities : \n')

pred_prob = knn.fit(sepal_data, iris_data['target']).predict_proba(test_data_plant1_2_sd[:, [0, 1]])
df_pred_prob = pd.DataFrame(pred_prob, columns=[species], index=["Plant 1", "Plant 2"])

print(df_pred_prob, '\n')

# III.I
print('------------------------------------ Using petal data --------------------------------------------')


petal_data = data_sd[:, [2, 3]]

print('###### 2 nearest neighbors ######\n')

knn = KNeighborsClassifier(n_neighbors=2).fit(petal_data, labels)
distance, indices = knn.kneighbors(test_data_plant1_sd[:, [2, 3]])

print("Indices : ", indices, '\n')
print("Data values : ", data[labels[indices]], '\n')
print("Species : ", species[labels[indices]], '\n')
print("Labels : ", labels[indices], '\n')


# III.II

print('###### 5 nearest neighbors ######\n')

knn = KNeighborsClassifier(n_neighbors=5).fit(petal_data, labels)
distance, indices = knn.kneighbors(test_data_plant1_2_sd[:, [2, 3]])


pred_label = knn.predict(test_data_plant1_2_sd[:, [2, 3]])


print("Plant 1 Details : \n",   'Predicted species label for plant 1 : \n', pred_label[0], '\n\n',
                                'Predicted species for plant 1 : \n', species[pred_label][0], '\n\n')


print("Plant 2 Details : \n",   'Predicted species label for plant 1 : \n', pred_label[1], '\n\n',
                                'Predicted species for plant 1 : \n', species[pred_label][1], '\n\n')

print('Probabilities : \n')

pred_prob = knn.fit(petal_data, iris_data['target']).predict_proba(test_data_plant1_2_sd[:, [2, 3]])
df_pred_prob = pd.DataFrame(pred_prob, columns=[species], index=["Plant 1", "Plant 2"])

print(df_pred_prob, '\n')

# IV.I

print('------------------------------------ Using all data --------------------------------------------')

from sklearn.neighbors import KNeighborsClassifier

all_data = data_sd

print('###### 2 nearest neighbors ######\n')

knn = KNeighborsClassifier(n_neighbors=2).fit(all_data, labels)
distance, indices = knn.kneighbors(test_data_plant1_sd)


print("Indices : ", indices, '\n')
print("Data values : ", data[labels[indices]], '\n')
print("Species : ", species[labels[indices]], '\n')
print("Labels : ", labels[indices], '\n')

# IV.II

print('###### 5 nearest neighbors ######\n')

knn = KNeighborsClassifier(n_neighbors=5).fit(all_data, labels)
distance, indices = knn.kneighbors(test_data_plant1_2_sd)

pred_label = knn.predict(test_data_plant1_2_sd)

print("Plant 1 Details : \n",   'Predicted species label for plant 1 : \n', pred_label[0], '\n\n',
                                'Predicted species for plant 1 : \n', species[pred_label][0], '\n\n')

print("Plant 2 Details : \n",   'Predicted species label for plant 1 : \n', pred_label[1], '\n\n',
                                'Predicted species for plant 1 : \n', species[pred_label][1], '\n\n')



print('Probabilities : \n')

pred_prob = knn.fit(all_data, iris_data['target']).predict_proba(test_data_plant1_2_sd)
df_pred_prob = pd.DataFrame(pred_prob, columns=[iris_data['target_names']], index=["Plant 1", "Plant 2"])

print(df_pred_prob, '\n')

# END