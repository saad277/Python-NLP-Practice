import spacy
from spacy.matcher import Matcher
nlp=spacy.load("en_core_web_sm")

matcher=Matcher(nlp.vocab)


#solarPower
pattern1=[{"LOWER":"solarpower"}]
#Solar-power
pattern2=[{"LOWER":"solar"},{"IS_PUNCT":True},{"LOWER","power"}]
#Solar power
pattern3=[{"LOWER":"solar","OP":"*"},{"LOWER":"power"}]


matcher.add("SolarPower",None,pattern3,pattern1);

doc=nlp(u"The Solar Power industry continues to grow a solarpower increases solar-power is")

found_matches=matcher(doc)

print(found_matches)

print("...........")


for match_id,start,end in found_matches:
    string_id=nlp.vocab.strings[match_id]   #get string representation
    span=doc[start:end]                         #get the matched span
    print(match_id,string_id,start,end,span.text)





