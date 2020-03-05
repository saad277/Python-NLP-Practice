#python -m spacy download en_core_web_sm
#python -m spacy download en_core_web_md
#python -m spacy download en_core_web_lg

from scipy import spatial

import spacy

nlp=spacy.load("en_core_web_lg");

print(nlp(u"lion").vector.shape)
print(nlp(u"lion").vector) #checking word vector for lion


tokens=nlp(u"lion cat pet")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text,token2.text,token1.similarity(token2))

print("#############################")

tokens2=nlp(u"dog cat nargle")

for token in tokens2:
    print(token.text,token.has_vector,token.vector_norm,token.is_oov) #oov=out of vocabulary

#creating new vector with cosine similarity
    
def cosine_similarity(vec1,vec2):
    return 1-spatial.distance.cosine(vec1,vec2)

king=nlp.vocab["king"].vector
man=nlp.vocab["man"].vector
woman=nlp.vocab["woman"].vector

#king - man + woman ---> NEW_VECTOR similar QUEEN,Princess , Your Highness

new_vector=king-man+woman;

computed_similarities=[];

#FOR ALL WORDS IN MY

for word in nlp.vocab:
    if word.has_vector:
        if word.is_lower:
            if word.is_alpha:
                similarity=cosine_similarity(new_vector,word.vector)
                computed_similarities.append((word,similarity))



computed_similarities=sorted(computed_similarities,key=lambda item : -item[1])

arr=[t[0].text for t in computed_similarities[:10]]

print(arr)













    
