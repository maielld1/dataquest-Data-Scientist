## 2. The dataset ##

import pandas as pd

votes=pd.read_csv("114_congress.csv")

## 3. Exploring the data ##

import numpy as np
print(votes['party'].value_counts())

print(np.mean(votes))

## 4. Distance between Senators ##

from sklearn.metrics.pairwise import euclidean_distances

print(euclidean_distances(votes.iloc[0,3:].reshape(1, -1), votes.iloc[1,3:].reshape(1, -1)))

distance = (euclidean_distances(votes.iloc[0,3:].reshape(1, -1), votes.iloc[2,3:].reshape(1, -1)))

## 5. Initial clustering ##

import pandas as pd
from sklearn.cluster import KMeans

kmeans_model = KMeans(n_clusters=2, random_state=1)
senator_distances = kmeans_model.fit_transform(votes.iloc[:, 3:])

## 6. Exploring the clusters ##

labels = kmeans_model.labels_
print(pd.crosstab(labels, votes['party']))

## 7. Exploring Senators in the wrong cluster ##

democratic_outliers = votes[(labels == 1) & (votes["party"] != "D")]

## 8. Plotting out the clusters ##

plt.scatter(senator_distances[:,0], senator_distances[:,1], c=labels)
plt.show()

## 9. Finding the most extreme ##

import numpy as np
extremism = np.sum((senator_distances**3), axis=1)
votes['extremism']=extremism
votes.sort_values('extremism',ascending=False, inplace=True)
print(votes.head(10))