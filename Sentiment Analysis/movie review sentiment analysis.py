import numpy as np
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

df=pd.read_csv("./moviereviews.tsv",sep="\t");

print(df.head())


df.dropna(inplace=True);

blanks=[]


for i,lb,rv in df.itertuples():
    if type(rv)==str:
        if rv.isspace():
            blanks.append(i)


print(blanks)


df.drop(blanks,inplace=True)


df["label"].value_counts();


sid=SentimentIntensityAnalyzer();

df["scores"]=df["review"].apply(lambda review:sid.polarity_scores(review))

df["compound"]=df["scores"].apply(lambda d:d["compound"])

df["comp_score"]=df["compound"].apply(lambda score:"pos" if score >=0 else "neg" )

print(df.head())

print(accuracy_score(df["label"],df["comp_score"]));


















