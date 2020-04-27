import numpy as np
import pandas as pd
#Given the below dictionarys find out where each of the 4 people find the cheapest shopping according to their needs.
shoppers = {
'Paula':{'Is':4,'Juice':2,'Kakao':3,'Lagkager':2},
'Peter':{'Is':2,'Juice':5,'Kakao':0, 'Lagkager':4},
'Pandora':{'Is':5,'Juice':3, 'Kakao':4, 'Lagkager':5},
'Pietro':{'Is':1,'Juice':8, 'Kakao':9, 'Lagkager':1}
}
shop_prices = {
    'Netto': {'Is':10.50,'Juice':2.25,'Kakao':4.50,'Lagkager':33.50},
    'Fakta': {'Is':4.00,'Juice':4.50,'Kakao':6.25,'Lagkager':20.00}
}
customers = pd.DataFrame(shoppers).T
prices = pd.DataFrame(shop_prices)
#print(customers)
#print(prices)
bestprice = customers.dot(prices)
#print(bestprice)

#Use the CountVectorizer from sklearn.feature_extraction to read the book data/moby_dick.txt
#How many times does the word 'wood' appear?
from sklearn.feature_extraction.text import CountVectorizer
import os
import re
with open('./moby_dick.txt', encoding="utf-8") as f:
    corpus = [f.read()]
vectorizer = CountVectorizer()

fit = vectorizer.fit_transform(corpus)
res = fit.todense() # returns a numpy array of same shape"
document_idx = vectorizer.vocabulary_['wood']
document_count = sum(res[:,document_idx]) # sum all row cells where column == index
print('wood occurs {} times in the text'.format(document_count))
#Use the load_digits function from the sklearn.datasets package to load a sklearn dataset
#The package contains .data of 8x8 images. Extract the first image in an 8x8 array
#Use the plt.imshow function to plot the image



#Are there a linear relationship here in this csv data:
#1 save data in a file: car_sales.csv
import csv
import platform
filename = "car_sales.csv"
with open(filename, 'w', newline="") as file_object:
    output_writer = csv.writer(file_object)
    output_writer.writerow(["year","GDPtrillion","4wheeler_car_sale"])
    output_writer.writerow(["2011","6.2","26.3"])
    output_writer.writerow(["2012","6.5","26.65"])
    output_writer.writerow(["2013","5.48","25.03"])
    output_writer.writerow(["2014","6.54","26.01"])
    output_writer.writerow(["2015","7.18","27.9"])
    output_writer.writerow(["2016","7.93","30.47"])

#2 plot car sales as a function to GDP (is there a linear relationship?)
import matplotlib.pyplot as plt
data = pd.read_csv("car_sales.csv")
print(data)
data.plot(x=1,y=2)
plt.show()

#3 fit data to a klearn linear regression model
import sklearn.linear_model


xs = data['GDPtrillion']
ys = data['4wheeler_car_sale']

xs_reshape = np.array(xs).reshape(-1, 1)
print(xs.shape)
print(xs_reshape.shape)

model = sklearn.linear_model.LinearRegression()
model.fit(xs_reshape, ys)

print(model.intercept_)
#4 predict sales if GDP hits 9 trillion lakhs
predicted = model.predict(xs_reshape)
spending10000 = model.predict([[9000000000000]])
print(spending10000[0])
print('GDP hits 9 trillion lakhs means {} 4wheeler cars will be sold'.format(spending10000[0]))