import pandas as pd
import numpy as np
import matplotlib as plt

dependenciesData = pd.read_csv("./data/dependencies-1.2.0-2018-03-12.csv", low_memory=False)
projectsData = pd.read_csv("./data/projects-1.2.0-2018-03-12.csv", low_memory=False)
projectsReposData = pd.read_csv("./data/projects_with_repository_fields-1.2.0-2018-03-12.csv", low_memory=False)
reposData = pd.read_csv("./data/repositories-1.2.0-2018-03-12.csv", low_memory=False)
reposDependenciesData = pd.read_csv("./data/repository_dependencies-1.2.0-2018-03-12.csv", low_memory=False)

print(dependenciesData.head(3))
