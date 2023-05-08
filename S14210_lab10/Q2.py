import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

# Question 1

iris_data = datasets.load_iris()

print(iris_data)

labels = iris_data.target
print('Data labels\n', labels, '\n')

# Standardizing the iris data

features = iris_data.data
scalar1 = StandardScaler().fit(features)

# Transform the iris data

featured_sd = scalar1.transform(features)
print('Standardized data set\n', featured_sd, '\n')

# Dummy data for iris (fom home garden)

test_data_plant1 = [[4.6, 3.0, 1.5, 0.2]]
test_data_plant1_2 = [[4.6, 3.0, 1.5, 0.2], [6.2, 3.0, 4.1, 1.2]]

# Standardizing the test data

scalar1 = StandardScaler().fit(test_data_plant1)
scalar2 = StandardScaler().fit(test_data_plant1_2)

test_data_plant1_sd = scalar1.transform(test_data_plant1)
test_data_plant1_2_sd = scalar2.transform(test_data_plant1_2)

print("Standardized data for plant 1 : \n", test_data_plant1_sd, '\n')
print("Standardized data for plant 1 & 2:\n", test_data_plant1_2_sd, '\n')

# To select first two columns (sepal data)
# ------------------------------------ Using sepal data --------------------------------------------

sepal_data = featured_sd[:, [0, 1]]

print('Sepal data (Sepal length and sepal width\n)', sepal_data, '\n')

from sklearn.neighbors import NearestNeighbors



# ************************************ 2 - nearest neighbours *********************************************

# n_neighbours = (k number)
nn = NearestNeighbors(n_neighbors=2).fit(sepal_data)

# splicing sample data
test_sepal_data = test_data_plant1_sd[:, [0, 1]]

# indices = most suitable 2 nearest neighbors for the new flower from the
# previous dataset

distance, indices = nn.kneighbors(test_sepal_data)

print("Plant 1 : \n",
      "Indices : ", indices[0][0], ',', indices[0][1], '\n',
      "labels : ", labels[indices[0][0]], ",", labels[indices[0][1]], '\n',
      "Species : ", iris_data.target_names[labels[indices[0][0]]], ",", iris_data.target_names[labels[indices[0][1]]],'\n')


# ************************************ 5 - nearest neighbours *********************************************

print('************************************ 5 - nearest neighbours *********************************************')
nn = NearestNeighbors(n_neighbors=5).fit(sepal_data)

test_sepal_data_2 = test_data_plant1_2_sd[:, [0, 1]]
distance, indices = nn.kneighbors(test_sepal_data_2)



print("Plant 1 : \n",
      "Indices : ",
      indices[0][0], ',',
      indices[0][1], ',',
      indices[0][2], ',',
      indices[0][3], ',',
      indices[0][4],'\n',
      "labels : ",
      labels[indices[0][0]], ",",
      labels[indices[0][1]],",",
      labels[indices[0][2]],",",
      labels[indices[0][3]],",",
      labels[indices[0][4]], '\n',
      "Species : ",
      iris_data.target_names[labels[indices[0][0]]], ",",
      iris_data.target_names[labels[indices[0][1]]], ",",
      iris_data.target_names[labels[indices[0][2]]], ",",
      iris_data.target_names[labels[indices[0][3]]], ",",
      iris_data.target_names[labels[indices[0][4]]], ",",'\n')

print("Plant 2 : \n",
      "Indices : ",
      indices[1][0], ',',
      indices[1][1], ',',
      indices[1][2], ',',
      indices[1][3], ',',
      indices[1][4],'\n',
      "labels : ",
      labels[indices[1][0]], ",",
      labels[indices[1][1]],",",
      labels[indices[1][2]],",",
      labels[indices[1][3]],",",
      labels[indices[1][4]], '\n',
      "Species : ",
      iris_data.target_names[labels[indices[1][0]]], ",",
      iris_data.target_names[labels[indices[1][1]]], ",",
      iris_data.target_names[labels[indices[1][2]]], ",",
      iris_data.target_names[labels[indices[1][3]]], ",",
      iris_data.target_names[labels[indices[1][4]]], ",",'\n')


# Probability of plants

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
print('Probabilities \n')
pred_prob1 = knn.fit(sepal_data, iris_data['target']).predict_proba(test_sepal_data_2)
df_pred_prob1 = pd.DataFrame(pred_prob1, columns=[iris_data['target_names']], index=["Plant 1", "Plant 2"])

print(df_pred_prob1, '\n')


# ------------------------------------ Using petal data --------------------------------------------

petal_data = featured_sd[:, [2, 3]]

print('Sepal data (Sepal length and sepal width\n)', petal_data, '\n')


# ************************************ 2 - nearest neighbours *********************************************

# n_neighbours = (k number)
nn = NearestNeighbors(n_neighbors=2).fit(petal_data)

# splicing sample data
test_petal_data = test_data_plant1_2_sd[:, [2, 3]]
print(test_petal_data)

# indices = most suitable 2 nearest neighbors for the new flower from the
# previous dataset

distance, indices = nn.kneighbors(test_sepal_data)

print("Plant 1 : \n",
      "Indices : ", indices[0][0], ',', indices[0][1], '\n',
      "labels : ", labels[indices[0][0]], ",", labels[indices[0][1]], '\n',
      "Species : ", iris_data.target_names[labels[indices[0][0]]], ",", iris_data.target_names[labels[indices[0][1]]],'\n')






# ************************************ 5 - nearest neighbours *********************************************

print('************************************ 5 - nearest neighbours *********************************************')
nn = NearestNeighbors(n_neighbors=5).fit(petal_data)

distance, indices = nn.kneighbors(test_petal_data)


print("Plant 1 : \n",
      "Indices : ",
      indices[0][0], ',',
      indices[0][1], ',',
      indices[0][2], ',',
      indices[0][3], ',',
      indices[0][4],'\n',
      "labels : ",
      labels[indices[0][0]], ",",
      labels[indices[0][1]],",",
      labels[indices[0][2]],",",
      labels[indices[0][3]],",",
      labels[indices[0][4]], '\n',
      "Species : ",
      iris_data.target_names[labels[indices[0][0]]], ",",
      iris_data.target_names[labels[indices[0][1]]], ",",
      iris_data.target_names[labels[indices[0][2]]], ",",
      iris_data.target_names[labels[indices[0][3]]], ",",
      iris_data.target_names[labels[indices[0][4]]], ",",'\n')

print("Plant 2 : \n",
      "Indices : ",
      indices[1][0], ',',
      indices[1][1], ',',
      indices[1][2], ',',
      indices[1][3], ',',
      indices[1][4],'\n',
      "labels : ",
      labels[indices[1][0]], ",",
      labels[indices[1][1]],",",
      labels[indices[1][2]],",",
      labels[indices[1][3]],",",
      labels[indices[1][4]], '\n',
      "Species : ",
      iris_data.target_names[labels[indices[1][0]]], ",",
      iris_data.target_names[labels[indices[1][1]]], ",",
      iris_data.target_names[labels[indices[1][2]]], ",",
      iris_data.target_names[labels[indices[1][3]]], ",",
      iris_data.target_names[labels[indices[1][4]]], ",",'\n')


# Probability of plants

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
print('Probabilities \n')
pred_prob1 = knn.fit(sepal_data, iris_data['target']).predict_proba(test_petal_data)
df_pred_prob1 = pd.DataFrame(pred_prob1, columns=[iris_data['target_names']], index=["Plant 1", "Plant 2"])

print(df_pred_prob1, '\n')


# ************************************************************************************************************
# ************************************************************************************************************
# By using all flower values
# ************************************************************************************************************
# ************************************************************************************************************