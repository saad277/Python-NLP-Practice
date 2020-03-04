

import spacy
from spacy import displacy

nlp=spacy.load("en_core_web_sm");

doc=nlp(u"The quick brown fox jumped over the lazy dog's back")

displacy.render(doc,style="dep")
















