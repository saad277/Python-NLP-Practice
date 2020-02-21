import spacy

nlp=spacy.load("en_core_web_sm")


print(nlp.Defaults.stop_words)



#to check stop word


print(nlp.vocab["is"].is_stop)
