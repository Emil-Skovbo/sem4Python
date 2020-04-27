import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report
# Import dataset
balance_data = pd.read_csv("balance-scale.data",sep= ',', header = None) 
# Split dataset (input variables and target) Hint: first column is the target
print(balance_data)
X = balance_data.values[:, 1:5] 
y = balance_data.values[:, 0] 
# Split dataset into training data and test data using train_test_split()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3) 
#Create a model (DecisionTreeClassifier(criterion = "gini", random_state=100,max_depth=3, min_samples_leaf=5)
model = DecisionTreeClassifier(criterion = "gini", random_state=100,max_depth=3, min_samples_leaf=5)
#Fit model with training data
model.fit(X_train, y_train)
# Make predictions on test data (using predicted_y = prediction(X_test, model))
y_predicted = model.predict(X_test)
#Calculate model accuracy with cal_accuracy(y_test, predicted_y)
print("accuracy = {}".format(accuracy_score(y_test,y_predicted)))
# en af resultaterne er accuracy = 0.7287234042553191

#Import data using sklearn.datasets.load_diabetes
from sklearn.datasets import load_diabetes
load_diabetes = load_diabetes()
X = load_diabetes().data
Y = load_diabetes().target
print(X)
print(Y)
#SVG
from graphviz import Source
from sklearn.tree import export_graphviz
from IPython.display import SVG
graph = Source( export_graphviz(model, out_file=None, feature_names=balance_data.feature_names))
SVG(graph.pipe(format='svg'))
