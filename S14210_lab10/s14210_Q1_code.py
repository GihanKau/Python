'''
Author  : B.M.G.G.K. Rajapaksha
Date    : 20/12/21
Topic   : Train the K-mean algorithm using iris dataset
Input   : iris dataset as iris.csv format

Output  : Trained algorithm with species predictions

'''

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Question 1)

# I

iris_data = pd.read_csv('iris.csv')
sepal_data = iris_data[['sepal.length', 'sepal.width']]
petal_data = iris_data[['petal.length', 'petal.width']]

# II
# Train the model

kmeans = KMeans(n_clusters=3).fit(sepal_data)
centroids = kmeans.cluster_centers_

centroid_df = pd.DataFrame(centroids, columns=["Sepal Length", "sepal width"])
print('Centroids :\n', centroid_df, '\n')

print('--------------------- K - mean algorithm using sepal length and sepal width ---------------------')

# III

new_data = np.array([[4.6, 3.0, 1.5, 0.2], [6.2, 3.0, 4.1, 1.2]])

pred_sepal = kmeans.predict(new_data[:, [0, 1]])

print('Predicted labels for sepal data : \n', 'Plant1 : ', pred_sepal[0], '\n'
                                               'Plant2 : ', pred_sepal[1], '\n')

# IV
# plot the original dataset

plt.scatter(iris_data['sepal.length'], iris_data['sepal.width'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)

for i, label in enumerate(kmeans.labels_):
    plt.annotate(label, (iris_data['sepal.length'][i], iris_data['sepal.width'][i]))

for i, label in enumerate(iris_data['v_short']):
    plt.annotate(label, (iris_data['sepal.length'][i], iris_data['sepal.width'][i]),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=3', color='red'),
                 textcoords='offset points', ha='center', va='bottom')

# plot the centroids in red color
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)

# plot the predicted values in black color
plt.scatter(new_data[:, 0], new_data[:, 1], c='black', s=50)

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Trained model for Sepal length and Sepal width')

plt.show()


print('--------------------- K - mean algorithm using petal length and petal width ---------------------')

# V
# Train the model

kmeans = KMeans(n_clusters=3).fit(petal_data)
centroids = kmeans.cluster_centers_


pred_petal = kmeans.predict(new_data[:, [2, 3]])

print('Predicted labels for sepal data : \n', 'Plant1 : ', pred_petal[0], '\n'
                                               'Plant2 : ', pred_petal[1], '\n')

# VI
# plot the original dataset

plt.scatter(iris_data['petal.length'], iris_data['petal.width'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)

for i, label in enumerate(kmeans.labels_):
    plt.annotate(label, (iris_data['petal.length'][i], iris_data['petal.width'][i]))

for i, label in enumerate(iris_data['v_short']):
    plt.annotate(label, (iris_data['petal.length'][i], iris_data['petal.width'][i]),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=3', color='red'),
                 textcoords='offset points', ha='center', va='bottom',)

# plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
# plot the predicted values
plt.scatter(new_data[:, 2], new_data[:, 3], c='black', s=50)

plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.title('Trained model for Petal length and Petal width')
plt.show()

# END