import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix,classification_report ,accuracy_score


df=pd.read_csv("./moviereviews.tsv",sep="\t");

print(df.head())

#checking null values 
print(df.isnull().sum())

#removing null values

print(df.dropna(inplace=True))

print(df.isnull().sum())


blanks=[]

# (index,Label,review text )

for i,lb,rv in df.itertuples():
    if rv.isspace():
        blanks.append(i)



print(blanks)

#removing blank spaces
df.drop(blanks,inplace=True)


x=df["review"];

y=df["label"]


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

text_clf=Pipeline([("tfidf",TfidfVectorizer()),("clf",LinearSVC())])

text_clf.fit(x_train,y_train);


predictions=text_clf.predict(x_test)

print(confusion_matrix(y_test,predictions))

print(accuracy_score(y_test,predictions))




print(text_clf.predict(["Bad Movie "]));





