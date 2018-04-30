from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import json
import gc
pd.set_option("display.max_rows", 999)
def dbscan(dataSet, name, col1, col2, saveName):
    #============================
    # Prepare Data
    #============================

    projectsData = pd.read_csv(dataSet, usecols=[name, col1, col2], low_memory=False)
    #projectsData = pd.read_csv(dataSet, low_memory=False)
    #print(projectsData.head())
    #print(projectsData[name])
    #print(projectsData[col1])
    #print(projectsData[col2])
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

    db = DBSCAN(min_samples=50, n_jobs=-1).fit(kData)
    labels = db.labels_
    clusters = len(set(labels)) - (1 if -1 in labels else 0)
    #print(labels)
    print(clusters)
    #plt.scatter(kDataX, kDataY)
    #plt.show()

def main():
    print("Starting DBSCAN Clustering ON Repositories where mininmum cluster size is 50")
    klusters = ['Stars Count','Forks Count','Open Issues Count','Contributors Count','SourceRank']
    count = 0
    for i in klusters:
        count = count + 1
        for j in klusters[count:]:
            print("Clustering on " + i + " and " + j + ":")
            dbscan("./small_data/repositories-1.2.0-2018-03-12.csv", "Name with Owner", i , j, "Test")
            gc.collect()
    '''
    i = klusters[0]
    j = klusters[3]
    print("Clustering on " + i + " and " + j + ":")
    dbscan("./small_data/repositories-1.2.0-2018-03-12.csv", "Name with Owner", i , j, "Test")
    '''

if __name__ == "__main__":
    main()
