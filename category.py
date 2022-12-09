import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("reviews+sentiment.csv")

category_revenue = df[["Imdb_genre","Box Office Collection"]].dropna(axis=0).reset_index(drop=True)

comedy=category_revenue[category_revenue["Imdb_genre"].str.contains("Comedy")==True]
thriller=category_revenue[category_revenue["Imdb_genre"].str.contains("Thriller")==True]
adventure=category_revenue[category_revenue["Imdb_genre"].str.contains("Adventure")==True]
drama=category_revenue[category_revenue["Imdb_genre"].str.contains("Drama")==True]
sci_fi=category_revenue[category_revenue["Imdb_genre"].str.contains("Sci-Fi")==True]
horror=category_revenue[category_revenue["Imdb_genre"].str.contains("Horror")==True]
#print(comedy.describe())
#print(thriller.describe())
#print(adventure.describe())
#print(drama.describe())
#print(sci_fi.describe())
#print(horror.describe())



sns.violinplot(x="Imdb_genre", y="Box Office Collection", data=category_revenue,cut=0).set(
    title ="Revenue by Genre")
plt.show()