from nltk.corpus import wordnet
antonyms=[]
for syn in wordnet.synsets('right'):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
print(antonyms)

