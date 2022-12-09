import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import sep
import scipy.stats

df = pd.read_csv("reviews+sentiment.csv")

rotten_revenue = df[["Score","Box Office Collection"]].dropna(axis=0).reset_index(drop=True)

rotten_revenue_correlation = scipy.stats.pearsonr(rotten_revenue["Score"], rotten_revenue["Box Office Collection"])[0]
print(rotten_revenue_correlation)
rotten_revenue.describe()


fig, axes = plt.subplots(1,3)
fig.suptitle("Graphs")

sns.regplot(ax=axes[0],data=rotten_revenue,x="Score",y="Box Office Collection").set(xlabel = "Rotten Tomato Score",
ylabel = "Revenue ($Millions)", title= "Tomato vs Revenue")

sns.stripplot(ax=axes[1],x="sentiments",y="Box Office Collection",data=df).set(xlabel="Review Sentiments",ylabel="",title="Sentiment vs Revenue")

sns.barplot(ax=axes[2],x="sentiments",y="Box Office Collection",data=df).set(xlabel="Review Sentiments",ylabel="",title="Sentiment vs Revenue")

plt.show()
#print(rotten_revenue.head())