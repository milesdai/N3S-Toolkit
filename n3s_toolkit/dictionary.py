# Language Dictionaries - not Python dictionaries
import pkg_resources

def load_english_dict():
    dictionary = list()
    dict_path = pkg_resources.resource_filename('n3s_toolkit', 'assets/words_english.txt')
    with open(dict_path, 'r') as f:
        dictionary = f.read()
    return dictionary.split('\n') 