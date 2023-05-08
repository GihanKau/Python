''' in this practical, we are going to study
                  1. K - mean algorithm
                  2. K - nearest neighbor algorithm (KNN)
'''

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Question I
iris_data = pd.read_csv('iris.csv')
print(iris_data)

#print(iris_data.iloc[:, 0:2])
#print(iris_data.iloc[:, 0:1])

# Question II

# Train the model

kmeans = KMeans(n_clusters=3).fit(iris_data.iloc[:, 0:2])
centroids = kmeans.cluster_centers_

print('Centroids :\n', centroids)

print(kmeans.labels_)

# Question III

new_data = np.array([[4.6, 3.0], [6.2, 3.0]])
print(new_data)
predv = kmeans.predict(new_data)

print(predv)

# Question IV

# plot the original dataset
plt.scatter(iris_data['sepal.length'], iris_data['sepal.width'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)

for i, label in enumerate(kmeans.labels_):
    plt.annotate(label, (iris_data['sepal.length'][i], iris_data['sepal.width'][i]))

for i, label in enumerate(iris_data['v_short']):
    plt.annotate(label, (iris_data['sepal.length'][i], iris_data['sepal.width'][i]), arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=3', color='red'),
                 textcoords='offset points', ha='center', va='bottom')

# plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
# plot the predicted values
plt.scatter(new_data[:, 0], new_data[:, 1], c='black', s=50)

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Trained model for Sepal length and Sepal width')

plt.show()


# ********************* K - mean algo using petal length and petal width *********************

# Question V

# Train the model

kmeans = KMeans(n_clusters=3).fit(iris_data.iloc[:, 2:4])
centroids = kmeans.cluster_centers_


print('Centroids :\n', centroids)

# print(kmeans.labels_)

new_data = np.array([[1.5, 0.2], [4.1, 1.2]])
print(new_data)
predv = kmeans.predict(new_data)

print(predv)

# plot the original dataset
plt.scatter(iris_data['petal.length'], iris_data['petal.width'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)

for i, label in enumerate(kmeans.labels_):
    plt.annotate(label, (iris_data['petal.length'][i], iris_data['petal.width'][i]))

for i, label in enumerate(iris_data['v_short']):
    plt.annotate(label, (iris_data['petal.length'][i], iris_data['petal.width'][i]), arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=3', color='red'),
                 textcoords='offset points', ha='center', va='bottom',)

# plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
# plot the predicted values
plt.scatter(new_data[:, 0], new_data[:, 1], c='black', s=50)

plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.title('Trained model for Sepal length and Sepal width')
plt.show()


# from sklearn import datasets
# iris = datasets.load_iris()
# print(iris)
# labels = iris.target
# print(labels)
#
# features = iris.data
# print(features)
#
# # fro standardized data
#
# from sklearn.preprocessing import StandardScaler
#
# scalar = StandardScaler().fit(features)
# print(scalar)
#
# # to transform data
#
# featured_sd=scalar.transform(features)
# print(featured_sd)
#
# # Dummy data for iris (fom home garden)
#
# test_data = [[5.9, 3.0, 5.1, 0.2]]
#
# # Normalize test data
# test_sd=scalar.transform(test_data)
# print(test_data)
#
# # to select first two columns (sepal data)
#
# sepal_data = featured_sd[:, [0, 1]]
# print(sepal_data)
#
# from sklearn.neighbors import NearestNeighbors
#
# # n_neighbours = ( k number)
# nn = NearestNeighbors(n_neighbors=2).fit(sepal_data)
#
# # splicing sample data
#
# testsepal_data = test_sd[:, [0, 1]]
#
# # indices = most suitable 2 nearest neighbors for the new flower from the
# # previous dataset
# distance, indices = nn.kneighbors(testsepal_data)
#
# print(indices)
#
#
#
