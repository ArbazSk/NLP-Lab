from nltk.stem import LancasterStemmer

ls = LancasterStemmer()

words = ["give", "giving", "given", "gave"]

for word in words:
    print(word + " : " + ls.stem(word))

