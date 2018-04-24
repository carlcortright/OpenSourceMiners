from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

#============================
# Prepare Data
#============================

#projectsData = pd.read_csv("./small_data/projects-1.2.0-2018-03-12.csv", usecols=['Name', 'SourceRank', 'Dependent Repositories Count'], low_memory=False)
projectsData = pd.read_csv("./small_data/repositories-1.2.0-2018-03-12.csv", usecols=['Name with Owner', 'Mirror URL', 'Pages enabled'], low_memory=False)
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

kmeans = KMeans(n_clusters=6, random_state=0).fit(kData)
count = [0,0,0,0,0,0]
for x in kmeans.labels_:
    if x == 0:
        count[0] = count[0] + 1
    elif x == 1:
        count[1] = count[1] + 1
    elif x == 2:
        count[2] = count[2] + 1
    elif x == 3:
        count[3] = count[3] + 1
    elif x == 4:
        count[4] = count[4] + 1
    elif x == 5:
        count[5] = count[5] + 1
print(count)
print(kmeans.labels_)
#print(kmeans.cluster_centers_)
plt.scatter(kDataX, kDataY)
plt.show()
