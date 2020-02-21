

import spacy

nlp=spacy.load("en_core_web_sm");

doc=nlp(u"The quick brown fox jumped over the lazy dog's back")

print(doc[4].pos_)
print(doc[4].tag_)          #VBD is past tense

for token in doc:
    print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")



print("####################################################################################");


doc1=nlp(u"I read a book on nlp ")

token=doc1[1]


print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")

print("####################################################################################")
doc2=nlp(u"I play cricket and go to field ")

token2=doc2[1]

print(f"{token2.text:{10}} {token2.pos_:{10}} {token2.tag_:{10}} {spacy.explain(token2.tag_)}")

#count part of speech


pos_counts = doc2.count_by(spacy.attrs.POS)

print(pos_counts)


















