import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import sep
import scipy.stats
import spacy
import re
import nltk
from nltk.corpus import stopwords
import en_vectors_web_lg
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("IMDB Dataset.csv")
movies_df = pd.read_csv("BoxOfficeCollections.csv").dropna(axis=0).reset_index(drop=True)
box_reviews = movies_df[["Consensus"]].iloc[:,0]
#print(type(box_reviews.iloc[0,0]))
reviews = df[["review"]].iloc[:10000,0]
sentiment = df[["sentiment"]].iloc[:10000,0]

def clean_review(text):
    clean_text = re.sub(r'<br\s?\/>|<br>', '', text) 
    clean_text = re.sub(r'\.', '', clean_text) 
    clean_text = re.sub(r'[^a-zA-Z\']', ' ', clean_text)
    clean_text = clean_text.lower()
   
    return clean_text

reviews = reviews.apply(lambda x : clean_review(x))
box_reviews = box_reviews.apply(lambda x : clean_review(x))
stopwords = set(stopwords.words("english"))
reviews = reviews.apply(lambda x : " ".join(word for word in x.split() if word not in stopwords))
box_reviews = box_reviews.apply(lambda x : " ".join(word for word in x.split() if word not in stopwords))
#print(df.iloc[1,0])
nlp = en_vectors_web_lg.load()
doc = nlp.pipe(reviews)
doc2 = nlp.pipe(box_reviews)
reviews_vector = np.array([review.vector for review in doc])
box_reviews_vector = np.array([review.vector for review in doc2])

X = reviews_vector[:len(reviews)]
y = sentiment

X_train,X_val, y_train, y_val = train_test_split(X,y, stratify=y, test_size=0.3, random_state=1)
model = LogisticRegression(C=10,max_iter=1000).fit(X_train, y_train)
y_pred = model.predict(box_reviews_vector)

movies_df.insert(7,"sentiments", y_pred)
#movies_df.to_csv("reviews+sentiment.csv",mode="a",index=True,header=True)
#print("Data appended succesfully :D")
fig, axes = plt.subplots(1,2)
fig.suptitle("Graphs")
sns.catplot(ax=axes[0],x="sentiments",y="Box Office Collection",data=movies_df)

sns.barplot(ax=axes[1],x="sentiments",y="Box Office Collection",data=movies_df)
plt.show()
