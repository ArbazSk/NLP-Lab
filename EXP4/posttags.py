import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
# nltk.download('averaged_perceptron_tagger')

stop_words = set(stopwords.words('english'))
stop_words.add(';')
stop_words.add(':')
stop_words.add('.')
stop_words.add(',')

with open('sample.txt','r') as file:
    data = file.read().replace('\n',' ')

token = sent_tokenize(data)

for i in token:
    wordlist = nltk.word_tokenize(i)
    wordlist = [w for w in wordlist if not w in stop_words]

    tagged = nltk.pos_tag(wordlist)

    print(tagged)