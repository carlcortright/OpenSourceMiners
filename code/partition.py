import pandas as pd
import sys, os, re

def miniturize(fpath):
    # Open the file to be cleaned
    if(os.path.isfile(fpath)):
        f = pd.read_csv(fpath, low_memory=False)
    else:
        print("ERROR: %s is an invalid file path" % fpath)
        exit(1)

# Get all of the paths to the data
paths = [f for f in os.listdir("./data/") if re.match("*+.csv", f)]

print(paths)