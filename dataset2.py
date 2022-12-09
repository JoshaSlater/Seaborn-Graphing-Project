import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.animation as animation
import bar_chart_race as bcr
df = pd.read_csv("movies.csv")


#print(year_genre_gross.head(10))


year_genre_gross2 = df[["genre","year","gross"]].dropna(axis=0)

Companies_gross = df[["company","year","gross"]].dropna(axis=0)

#print(year_genre_gross2["genre"].value_counts())



year_genre_gross2["sum_by_genre"] = year_genre_gross2.groupby(["year", "genre"]).transform("sum")
#print(year_genre_gross2.groupby(["year", "genre"]).first())
year_genre_gross2["sum_of_year"] = year_genre_gross2.groupby(["year"])["gross"].transform("sum")
year_genre_gross2["genre_percent_by_year"] = year_genre_gross2["sum_by_genre"] / year_genre_gross2["sum_of_year"]
#year_genre_gross2["sum"] = helper.transform("sum")
#print(helper.first())
#print(year_genre_gross2.head(60))
#print(year_genre_gross2.groupby(["sum"]).first())

pivoted_data = year_genre_gross2[["genre","year","genre_percent_by_year"]].pivot_table(index="genre",columns="year",values="genre_percent_by_year",fill_value=0)
#print(pivoted_data.head(20))
#sns.heatmap(data=pivoted_data,cbar_kws={'label': 'Percent of Total Box Office Sales (%)'}).set(title='Box Office Sales by Genre Each Year')

Companies_gross["sum_by_company"] = Companies_gross.groupby(["year", "company"])["gross"].transform("sum")

Companies_gross["sum_of_year"] = Companies_gross.groupby(["year"])["gross"].transform("sum")
Companies_gross["company_percent_by_year"] = Companies_gross["sum_by_company"] / Companies_gross["sum_of_year"]
#print(Companies_gross.head())

pivot2 = Companies_gross[["company","year","sum_by_company"]].pivot_table(index="year",columns="company",values="sum_by_company",fill_value=0)
print(pivot2["Universal Pictures"])
#bcr.bar_chart_race(df=pivot2,filename="l.mp4",n_bars=7,steps_per_period=4)

#ax = sns.lineplot(data=year_genre_gross2, x="year",y="genre_percent_by_year",hue="genre")
#ax.set(title="Box Office Sales by Genre Each Year",ylabel="Percent of total Gross BOC")
#sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
#plt.show()