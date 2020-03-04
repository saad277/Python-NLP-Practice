

import spacy
from spacy.pipeline import SentenceSegmenter

nlp=spacy.load("en_core_web_sm");

doc=nlp(u"This is the first sentence.This is another.This is the last sentence")

for sent in doc.sents:
    print(sent)

print("..................")
print(list(doc.sents)[0])

print("..................")

doc1=nlp(u"'Management is doing the right things ;leadership is doing the right things.' -Peter Ducker ")

for sent in doc1.sents:
    print(sent)

print("..................")

#Add a segmentation Rule 


def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if(token.text==";"):
            doc[token.i+1].is_sent_start=True

    return doc


nlp.add_pipe(set_custom_boundaries,before="parser");

print(nlp.pipe_names)
    
print("..................")

doc4=nlp(u"'Management is doing the right things ;leadership is doing the right things.' -Peter Ducker ")

for sent in doc4.sents:
    print(sent)

#Change segmentation rule
    
print("..................")

doc5=nlp(u"This is a sentence.This is another.\n\nThis is a \n Third Sentence")

for sent in doc5.sents:
    print(sent)


def split_on_newlines(doc):
    start=0;
    seen_newline=False;

    for word in doc:
        if(seen_newline):
            yield doc[start:word.i]
            start=word.i
            seen_newline=False

        elif word.text.startswith("\n"):
            seen_newline=True


    yeild doc[start:]







