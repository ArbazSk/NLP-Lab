from spellchecker import SpellChecker

spell = SpellChecker()
input_word = input("Enter the Word:")
input_list =[w for w in input_word.split(" ")]
# print(input_list)
# find those words that may be misspelled

misspelled = spell.unknown(input_list)
print(misspelled)

for word in misspelled:
    # Get the one `most likely` answer
    print("The Nearest word to {0} is:".format(word))
    print(spell.correction(word))

    # Get a list of `likely` options
    # print(spell.candidates(word))