from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import json
pd.set_option("display.max_rows", 999)
def kmeans(dataSet, name, col1, col2, saveName):
    #============================
    # Prepare Data
    #============================

    projectsData = pd.read_csv(dataSet, usecols=[name, col1, col2], low_memory=False, nrows=500)
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

    kmeans = KMeans(n_clusters=6, random_state=0, n_jobs=-1).fit(kData)
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
    #print(kmeans.labels_[0])
    jdata = {}
    nodes = []
    links = []
    index = 0
    for i in projectsData[name]:
        if len(kmeans.labels_) > index:
            x = {}
            x["id"] = str(i)
            x["group"] = int(kmeans.labels_[index]) + 1
            nodes.append(x)
            y = {}
            y["source"] = str(i)
            y["target"] = str(int(kmeans.labels_[index]) + 1)
            y["value"] = 1
            links.append(y)

        else:
            pass
        index = index + 1  

    a = {}
    b = {}
    c = {}
    d = {}
    e = {}
    f = {}
    a["id"] = "1"
    a["group"] = 1
    b["id"] = "2"
    b["group"] = 2
    c["id"] = "3"
    c["group"] = 3
    d["id"] = "4"
    d["group"] = 4
    e["id"] = "5"
    e["group"] = 5
    f["id"] = "6"
    f["group"] = 6
    nodes.append(a)
    nodes.append(b)
    nodes.append(c)
    nodes.append(d)
    nodes.append(e)
    nodes.append(f)
    count1 = 0
    for i in kmeans.cluster_centers_:
        count1 = count1 + 1
        count2 = count1
        for j in kmeans.cluster_centers_[count1:]:
            if count2 < 6:
                count2 = count2 + 1
                y = {}
                y["source"] = str(count1)
                y["target"] = str(count2)
                y["value"] = 3
                links.append(y)
            else:
                pass
    jdata["nodes"] = nodes
    jdata["links"] = links
    #print(json.dumps(jdata))
    with open(saveName, 'w') as outfile:
        json.dump(jdata, outfile)
    print(kmeans.cluster_centers_)
    #plt.scatter(kDataX, kDataY)
    #plt.show()

def main():
    print("Starting KMeans Clustering ON Repositories")
    klusters = ['Stars Count','Forks Count','Open Issues Count','Watchers Count','Contributors Count','SourceRank']
    count = 0
    for i in klusters:
        count = count + 1
        for j in klusters[count:]:
            print("Clustering on " + i + " and " + j + ":")
            save = "./../website/assets/data/" + i.replace(" ","_") + "vs" + j.replace(" ","_") + ".json"
            kmeans("./small_data/repositories-1.2.0-2018-03-12.csv", "Name with Owner", i , j, save )
    '''
    print("Starting KMeans Clustering ON Projects")
    klusters = ['Stars Count','Forks Count','Open Issues Count','Watchers Count','Contributors Count','SourceRank']
    count = 0
    for i in klusters:
        count = count + 1
        for j in klusters[count:]:
            print("Clustering on " + i + " and " + j + ":")
            kmeans("./small_data/projects-1.2.0-2018-03-12.csv", "Name with Owner", i , j, "Test")
    '''

if __name__ == "__main__":
    main()
