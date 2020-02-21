import spacy
nlp=spacy.load("en_core_web_sm");
from spacy.matcher import PhraseMatcher


matcher=PhraseMatcher(nlp.vocab)


with open("./reaganomics.txt") as f:
    doc3=nlp(f.read())
    print(doc3)


phrase_list=["voodoo economics","supply-side economics","trick-down economics","free-market economics"]


phrase_patterns=[nlp(text) for text in phrase_list]

print(phrase_patterns)

matcher.add("EconMatcher",None,*phrase_patterns)


found_matches=matcher(doc3)


print(found_matches)
