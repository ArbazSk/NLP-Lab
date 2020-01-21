# import nltk
# nltk.download('wordnet')

from nltk.corpus import wordnet
synonyms=[]
for syn in wordnet.synsets('fortunate'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

