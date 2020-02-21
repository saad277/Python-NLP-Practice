

import spacy
from spacy import displacy
from spacy.tokens import Span

nlp=spacy.load("en_core_web_sm");


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text+"-"+ent.label_+"-"+str(spacy.explain(ent.label)))
    else:
        print("No entity found");



doc=nlp(u"Hi How are you ? ")


show_ents(doc)




doc2=nlp(u"May I go to Washington,DC next May to see the Washington Monument   ")




show_ents(doc2)

print("___________________________")

#Add your own entity

doc3=nlp(u"Tesla to build a UK factory for 6 million")

show_ents(doc3)

#Gonna add tesla as ORG

print("___________________________")

ORG=doc.vocab.strings[u"ORG"];




new_ents=Span(doc3,0,1,label=ORG)

doc3.ents=list(doc3.ents)+[new_ents]
show_ents(doc3)















