

import spacy

nlp=spacy.load("en_core_web_sm");

doc= nlp(u"Tesla is looking for buying U.S Startup for $6 million");   #U is unicode

print(doc[2])
