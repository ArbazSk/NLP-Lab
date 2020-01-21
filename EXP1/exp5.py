import nltk
from nltk .tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
data = "I am feeling happy ."
word_tokens=word_tokenize(data)
ps=PorterStemmer()
for w in word_tokens:
    print(w, ":",ps.stem(w))
