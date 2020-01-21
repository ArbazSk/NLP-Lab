from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()
print("Lemmatization on word")
print("rocks : " + lemma.lemmatize("rocks"))
print("Anaconda : " + lemma.lemmatize("anaconda"))

print("Lemmatization on lists of word")
words = ['bats', 'sports', 'equipments','computer']
for word in words:
    print(word + " : " + lemma.lemmatize(word))


print("Lemmatization on Sentence")
from nltk.tokenize import word_tokenize
text = "The striped bats are hanging on their feet for best view of the inverted worlds."

token = word_tokenize(text)

lemma_output = ' '.join([lemma.lemmatize(word) for word in token])
print(lemma_output)