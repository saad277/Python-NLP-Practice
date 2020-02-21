import spacy

nlp=spacy.load("en_core_web_sm");

doc1=nlp(u"Iam a runner running in a race because I love to run since I ran")

for token in doc1:
    print(token.text,"\t",token.pos_,"\t",token.lemma,"\t",token.lemma_)
    
