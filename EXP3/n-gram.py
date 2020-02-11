import nltk
from nltk import ngrams,bigrams,trigrams
from nltk.tokenize import word_tokenize
import pandas

def simple_working():
    with open('sample.txt','r') as file:
        data = file.read().replace('\n',' ')
        print(data,'\n')

    delimiters = ['(',')','!',';',',','@','"','[',']','/','\\','1']

    for i in delimiters:
        data = data.replace(i,' ')

    data = word_tokenize(data)

    bigrams = list(bigrams(data))
    print("bigram:::{}".format(bigrams))

    trigrams = list(trigrams(data))
    print("trigram:::{}".format(trigrams))

    ngrams = list(ngrams(data,5))
    print("ngram:::{}".format(ngrams))


def n_gram():
    with open('sample.txt','r') as file:
        data = file.read().replace('\n',' ')
        print(data,'\n')

    delimiters = ['(',')','!',';',',','@','"','[',']','/','\\','1']

    for i in delimiters:
        data = data.replace(i,' ')

    data = word_tokenize(data)


    num = input("Enter n:")

    ngram = list(ngrams(data,int(num)))
    print("ngram:::{}".format(ngram))


if __name__ == "__main__":
    n_gram()