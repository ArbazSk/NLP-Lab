import nltk
from nltk .tokenize import sent_tokenize, word_tokenize
data = "Greeting of the day. Hope you have a great day."
print("line tokenization:\n")
print(sent_tokenize(data))
print("\nWord Tokenization:\n")
print(word_tokenize(data))
