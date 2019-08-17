# English Dictionaries - not Python dictionaries

def load_english_dictionary():
    dictionary = list()
    with open('assets/words_english.txt', 'r') as f:
        dictionary = f.read()
    return dictionary.split('\n') 