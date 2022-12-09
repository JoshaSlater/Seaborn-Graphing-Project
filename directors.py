import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import sep
import scipy.stats

df = pd.read_csv("reviews+sentiment.csv")

directors_revenue = df[["Director","Box Office Collection"]].dropna(axis=0).reset_index(drop=True)

dict = directors_revenue.groupby(['Director']).count().to_dict()

revenue_dict = {}
test = directors_revenue.to_numpy(copy=True)

for i in test:
    if i[0] in revenue_dict:
        revenue_dict[i[0]] += i[1]
    else:
        revenue_dict[i[0]] = i[1]

directors_revenue_count = pd.DataFrame.from_dict({"Director" : revenue_dict.keys(), "Revenue" : revenue_dict.values()})
directors_revenue_count = directors_revenue_count[directors_revenue_count["Revenue"] > 750000000.0]

for x in dict["Box Office Collection"]:
    if x[0] in directors_revenue_count["Director"]:
        directors_revenue_count.insert(directors_revenue_count[x[0]], "Count",x[1])





#sns.countplot(x="Director", data = directors_revenue)
#sns.stripplot(x="Director",y="Box Office Collection",data=directors_revenue).set(
    #xlabel="Directors",ylabel="Revenue ($Millions)",title="Director vs Revenue")
rc = {'figure.figsize':(8,5),
      'axes.facecolor':'white',
      'axes.grid' : True,
      'grid.color': '.8',
      'font.family':'Times New Roman',
      'font.size' : 15}

plt.rcParams.update(rc)
sns.set(font_scale=0.4)
sns.barplot(data=directors_revenue_count, x="Director",y="Revenue").set(
    title ="Top Directors with Most Gross Revenue")

plt.xticks(rotation=70)

plt.show()