from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

#============================
# Prepare Data
#============================

projectsData = pd.read_csv("./small_data/projects-1.2.0-2018-03-12.csv", usecols=['Name', 'SourceRank', 'Dependent Repositories Count'], low_memory=False)
#projectsData = pd.read_csv("./small_data/repositories-1.2.0-2018-03-12.csv", usecols=['Name with Owner', 'Mirror URL', 'Pages enabled'], low_memory=False)
#print(projectsData['Size'])
#print(projectsData['Pages enabled'])
data = []
kData = []
kDataX = []
kDataY = []
for row in projectsData.iterrows():
    if row[1][0]:
        if row[1][1] > 0:
            if row[1][2] > 0:
                # Name, x, y, cluster 
                data.append((row[1][0], [row[1][1], row[1][2]], 0))
    else:
        pass
for x in data:
    kData.append(x[1])
    kDataX.append(x[1][0])
    kDataY.append(x[1][1])

#============================
# Start Clustering
#============================

db = DBSCAN(min_samples=10, n_jobs=-1).fit(kData)
labels = db.labels_
clusters = len(set(labels)) - (1 if -1 in labels else 0)
for i in labels:
    print(i)
#print(labels)
print(clusters)
#plt.scatter(kDataX, kDataY)
#plt.show()
