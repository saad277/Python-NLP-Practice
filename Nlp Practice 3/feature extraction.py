
vocab={}

i=1


with open("1.txt") as f:
    x=f.read().lower().split()
    print(x)


for word in x:
    if word in vocab:
        continue

    else:
        vocab[word]=i
        i=i+1;


print(vocab)

print("############################")
vocab2={}

j=1


with open("2.txt") as f:
    y=f.read().lower().split()
    print(x)


for word2 in y:
    if word2 in vocab2:
        continue

    else:
        vocab2[word2]=j
        j=j+1;


print(vocab2)


print("############################")
#Creating Empty Vector 1

one=["1.txt"]+[0]*len(vocab)

print(one)


with open("1.txt") as f:
    z=f.read().lower().split();

for word in z:
    one[vocab[word]]+=1



print(one)



print("############################")


#Creating Empty Vector 1

two=["2.txt"]+[0]*len(vocab2)

print(two)


with open("2.txt") as f:
    c=f.read().lower().split();

for word in c:
    two[vocab2[word]]+=1



print(two)





