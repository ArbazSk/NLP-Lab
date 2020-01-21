from nltk.stem import PorterStemmer

ps = PorterStemmer()

p = ps.stem("Vegetable")
print("After Stemming", p)


#Stemming on a list of words

words = ["give", "giving", "given", "gave"]

print("Stemming of list of words:")
for word in words:
    print(word + " : " + ps.stem(word))

print("\nStemming a sentence")

from nltk.tokenize import word_tokenize

text = '''In Brazil they drive on the right-hand side of the road. Brazil has a large coastline on the eastern side of South America.
            Brazil is rich in  natural resources.'''

text1 = word_tokenize(text)            

for word in text1:
    print(ps.stem(word))