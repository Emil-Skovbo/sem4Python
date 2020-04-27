import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

titanic_data = pd.read_csv("train.csv")
print(titanic_data)
titanic_data.drop(['PassengerId','Name','Ticket','Cabin'],'columns',inplace=True)
titanic_data.head()
print(titanic_data)


from sklearn import preprocessing
# Convert gender to 0 or 1
label_enc = preprocessing.LabelEncoder()
titanic_data['Sex'] = label_enc.fit_transform(titanic_data['Sex'].astype(str))
titanic_data.head()
print(titanic_data)

# One-hot encoding of 'Embarked' with pd.get_dummies
titanic_data = pd.get_dummies(titanic_data,columns=['Embarked'])
titanic_data.head()
print(titanic_data)

# Find missing values in the data and drop those rows:
print('rows before drop n/a',len(titanic_data))
missing = titanic_data[titanic_data.isnull().any(axis=1)]
titanic_data = titanic_data.dropna()
print('rows after',len(titanic_data))
print(titanic_data)

# what is the best bandwidth to use for our dataset?
# The smaller values of bandwith result in tall skinny kernels & larger values result in short fat kernels.
from sklearn.cluster import estimate_bandwidth
print(estimate_bandwidth(titanic_data))
#30.44675914497196

#8 Fit data to a meanshift model
from sklearn.cluster import MeanShift
analyzer = MeanShift(bandwidth=30) 
print(analyzer.fit(titanic_data))

#9 How many clusters do we get
labels = analyzer.labels_
print(labels)
print('\n\n',np.unique(labels))
# We get 5 diffretn clusters: [0 1 2 3 4]

#We will add a new column in dataset which shows the cluster the data of a particular row belongs to.
titanic_data['cluster_group'] = np.nan
data_length = len(titanic_data)
for i in range(data_length): # loop 714 rows
    titanic_data.iloc[i,titanic_data.columns.get_loc('cluster_group')] = labels[i] #set the cluster label on each row

titanic_data.head()
print(titanic_data)

#11 Get mean values of each cluster group
print(titanic_data.describe())


#12 Add a column with the size of each cluster group
#Grouping passengers by Cluster
titanic_cluster_data = titanic_data.groupby(['cluster_group']).mean()
#Count of passengers in each cluster
titanic_cluster_data['Counts'] = pd.Series(titanic_data.groupby(['cluster_group']).size())
print(titanic_cluster_data)

#13 Write out conclusion from the aggregated data.

#Conclusion
#Cluster 0
#Have 558 passengers
#Survival rate is 33%(very low) means most of them didn't survive
#They belong to the lower classes 2nd and 3rd class mostly and are mostly male .
#The average fare paid is $15
#Cluster 1
#Have 108 passengers
#Survival rate is 61% means a little more than half of them survived
#They are mostly from 1st and 2nd class
#The average fare paid is $65
#Cluster 2 i.e the 3rd Cluster
#Have 30 passengers
#Survival rate is 73% means most of them survived
#They are mostly from 1st class
#The average fare paid is $131 (high fare)
#Cluster 3 i.e the 4th Cluster
#Have 15 passengers
#Survival rate is 73% means most of them survived
#They are mostly from 1st class and are mostly female
#The average fare paid is $239 (which is far higher than the 1st cluster average fare)
#The last cluster has just 3 datapoints so it is not that significant hence we can ignore for data analysis