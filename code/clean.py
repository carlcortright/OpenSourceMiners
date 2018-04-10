# 
# Cleans each of the main datasets.
# 
import os.path as path
import pandas as pd
import sys

# Open the file to be cleaned
fpath = sys.argv[1]
if(path.isfile(fpath)):
    f = pd.read_csv(fpath)
else:
    print("ERROR: %s is an invalid file path" % fpath)
    exit(1)

print(f.head())