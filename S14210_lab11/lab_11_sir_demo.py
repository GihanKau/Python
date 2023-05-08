from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

# different attributes of the dataset

cancer.keys()
cancer.target
cancer.feature_names

# ---------------------------------

# to get the size of the dataset
print(cancer['data'].shape)

# to define x and y variables

X = cancer['data']
y = cancer['target']

# validate data (categorical names into numerical data)

# split the data into training and test data

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# transform data

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(cancer['data']) # or scaler = StandardScaler().fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# run the neural network

from sklearn.neural_network import MLPClassifier

# three hidden layers, 20 neurons per each

mpl = MLPClassifier(hidden_layer_sizes=(20, 20, 20), max_iter= 1000)

# training the dataset
mpl.fit(X_train, y_train)

# predict teh data

predictions = mpl.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
