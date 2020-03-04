

import spacy
from spacy import displacy
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

nlp=spacy.load("en_core_web_sm");


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text+"-"+ent.label_+"-"+str(spacy.explain(ent.label)))
    else:
        print("No entity found");



doc=nlp(u"Our company created a brand new vacuum cleaner ."
        u"This new vacuum-cleaner is the best in show ")


show_ents(doc)


matcher=PhraseMatcher(nlp.vocab)

phrase_list=["vacuum cleaner","vacuum-cleaner"]

phrase_patterns=[nlp(text) for text in phrase_list]

matcher.add("newproduct",None,*phrase_patterns)

found_matches=matcher(doc)

print(found_matches)


PROD=doc.vocab.strings[u"PRODUCT"];

new_ents=[Span(doc,match[1],match[2],label=PROD) for match in found_matches]

doc.ents=list(doc.ents)+ new_ents

show_ents(doc)










