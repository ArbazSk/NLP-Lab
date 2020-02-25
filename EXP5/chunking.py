import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize

train_txt = "Shooting is a very popular sport. Hunters use guns to shoot animals. Terrorist also use them to kill."
sample = "Sharpshooter Mark shoots a dangerous animal with a gun."

PunktSentenceTokenizer(train_text=train_txt)
tokenized = sent_tokenize(sample)

def process():
    try:
        for i in tokenized:
            words = word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunk_gram = r"""chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunk_parser = nltk.RegexpParser(chunk_gram)
            chunked = chunk_parser.parse(tagged)
            chunked.draw()

    except Exception as e:
        print(e)

process()
