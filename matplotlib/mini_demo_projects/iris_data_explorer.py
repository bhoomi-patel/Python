import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

# 1. load data
iris = datasets.load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['species']=pd.Categorical.from_codes(iris.target,iris.target_names)

# 2 scatter : sepal length vs width
fig , ax = plt.subplots(1,2,figsize=(12,5))
for species,color in zip(iris.target_names,['r','g','b']):
    subset = df[df['species']==species]
    ax[0].scatter(
        subset['sepal length (cm)'],
        subset['sepal width (cm)'],
        label = species,
        alpha = 0.7 , s=50 ,c=color
    )
ax[0].set_title("sepal:length vs width")
ax[0].set_xlabel("length(cm)")
ax[0].set_ylabel("width(cm)")
ax[0].legend()

# 3 boxplot petal length by species
df.boxplot(column = "petal length (cm)", by="species",ax=ax[1],grid=False,patch_artist = True, boxprops = dict(facecolor = 'lightyellow'))
ax[1].set_title("petal length distribution")
ax[1].set_ylabel("Length (cm)")
plt.suptitle("") # remove automatic title
plt.tight_layout()
plt.show()

# 4. pairwise matrix of histograms
pd.plotting.scatter_matrix(
    df.iloc[ :, :4],
    figsize=(8,8),
    diagonal='hist',
    color=['red','green','blue'][0] , alpha=0.5
)
plt.suptitle("pairwise feature relationships")
plt.show()