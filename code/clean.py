# 
# Cleans each of the main datasets.
# 
import os.path as path
import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import missingno as msno
import sys

# Open the file to be cleaned
fpath = sys.argv[1]
if(path.isfile(fpath)):
    f = pd.read_csv(fpath, low_memory=False)
else:
    print("ERROR: %s is an invalid file path" % fpath)
    exit(1)

plt = msno.matrix(f.sample(1000))
fig = plt.get_figure()
fig.savefig("missing_projects_data.png")

plt = msno.heatmap(f)
fig = plt.get_figure()
fig.savefig("project_collissions.png")