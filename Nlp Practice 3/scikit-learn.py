import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

df=pd.read_csv("./smsspamcollection.tsv",encoding='latin1',sep="\t")


#print(df["length"].unique())


#X is feature data
x=df[["length","punct"]]


#Y is our label 
y=df["label"]


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

#print(y_test);

lr_model=LogisticRegression(solver="lbfgs");

lr_model.fit(x_train,y_train);

predictions=lr_model.predict(x_test);


#print(predictions)

print(metrics.confusion_matrix(y_test,predictions))

dfc=pd.DataFrame(metrics.confusion_matrix(y_test,predictions),index=["ham","spam"],columns=["ham","spam"])

print(dfc)

print(metrics.accuracy_score(y_test,predictions))

############################

nb_model=MultinomialNB();

nb_model.fit(x_train,y_train);

predictions=nb_model.predict(x_test)

print(metrics.confusion_matrix(y_test,predictions))

#############################

svc_model=SVC(gamma="auto")

svc_model.fit(x_train,y_train);

predictions=svc_model.predict(x_test);

print(metrics.confusion_matrix(y_test,predictions))


















