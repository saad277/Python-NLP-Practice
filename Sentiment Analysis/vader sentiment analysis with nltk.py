
#python -m nltk.downloader vader_lexicon


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

sid=SentimentIntensityAnalyzer();


a="This is a good movie";

ays=sid.polarity_scores(a)

print(ays)

b="Very bad movie a utter disgrace"

print(sid.polarity_scores(b))


df=pd.read_csv("amazonreviews.tsv",sep="\t")


#print(df.head())

print(df["label"].value_counts())

#removing null values

blanks=[]

for i,lb,rv in df.itertuples():
    # (index,label,review)
    if type(rv)==str:
        if rv.isspace():
            blanks.append(i)

#df.drop(blanks,inplace=True)

print(df.iloc[0]["review"]);

print(sid.polarity_scores(df.iloc[0]["review"]))

#adding sentiment scores to tsv file 

df["scores"]=df["review"].apply(lambda review: sid.polarity_scores(review))

#print(df.head())

#adding compound only

df["compound"]=df["scores"].apply(lambda d:d["compound"])


print(df.head())


df["comp_score"]=df["compound"].apply(lambda score: "pos" if score >= 0 else "neg")



print(accuracy_score(df["label"],df["comp_score"]))


























