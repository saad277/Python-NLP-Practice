import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn import metrics

df=pd.read_csv("./smsspamcollection.tsv",sep="\t")

print(df.head())

x=df["message"]

y=df["label"]



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)


count_vectorizer=CountVectorizer()

#Fit vectorizer to data (build a vocab , count number of words)

x_train_counts=count_vectorizer.fit_transform(x_train)

#print(x_train_counts)

tfidf_transformer=TfidfTransformer();

x_train_tfidf=tfidf_transformer.fit_transform(x_train_counts)

#print(x_train_tfidf.shape)

Tvectorizer=TfidfVectorizer();

x_train_tfidf2=Tvectorizer.fit_transform(x_train)

#print(x_train_tfidf2.shape)


clf=LinearSVC()

clf.fit(x_train_tfidf2,y_train)

text_clf=Pipeline([("tfidf",TfidfVectorizer()),("clf",LinearSVC())])


text_clf.fit(x_train,y_train)

predictions=text_clf.predict(x_test)

print(metrics.accuracy_score(y_test,predictions))

print(text_clf.predict(["Congrats you won free tickets "]))







