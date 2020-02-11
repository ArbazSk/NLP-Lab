import nltk
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize

print("Lancaster Stemmer :")
pst=LancasterStemmer()

text="I am doing and waiting like energetic faculties"
text1=word_tokenize(text)

for word in text1:
    print(pst.stem(word))
    print()

