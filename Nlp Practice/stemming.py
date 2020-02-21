import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
p_stemmer=PorterStemmer();


words=["run","runner","ran","easily","fairly","fairness"];

for word in words:
    print(word + "----->"+p_stemmer.stem(word) )


print("................")
s_stemmer=SnowballStemmer(language="english")

for word in words:
    
    print(word +"------>"+s_stemmer.stem(word))



