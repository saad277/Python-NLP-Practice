import spacy

nlp=spacy.load("en_core_web_sm");

mystring=" 'We \'re moving to L.A.! ' "


doc=nlp(mystring);

for token in doc:
    print(token.text)



print("---------------------------------------------")

doc2=nlp(u"We're here to help! Send snail-mail,email support@oursite.com or visit us at http://www.oursite.com")           #u is unicode

print(len(doc2.vocab))

for token in doc2:
    print(token)


print("---------------------------------------------")

doc8=nlp(u"Apple to build a Hong Kong Factory for $6 Million");


for entity in doc8.ents:            #will get entities only
    print(entity)
    print(entity.label_)
    print(spacy.explain(entity.label_))

print("---------------------------------------------")

doc9=nlp(u"Autonomous cars shift insurance liability towards manufacturers");

for chunk in doc9.noun_chunks:
    print(chunk)
