import numpy as np
import pandas as pd
#Import science.csv to a pandas DataFrame
science_data = pd.read_csv("science.csv")
print(science_data)
#Split the input (X) and target (y) using train_test_split
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
X = load_iris().data
y = load_iris().target
print(train_test_split(X, y))

#Train the model on the training data



#Score the model based on the testing data

