

import spacy
from spacy import displacy
nlp=spacy.load("en_core_web_sm");

doc=nlp(u"Apple is going to build a U.K factory for 6$ million")

a=displacy.render(doc,style="dep",options={"distance":110})


print(a)
