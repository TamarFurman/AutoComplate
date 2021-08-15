import pickle

from data.words_data import Words_Data
from init_function.format_sentence import format_sentence


def search(sentence):
    # db_file = open(sentence[0], 'rb')
    # word_trie = pickle.load(db_file)
    words_data = Words_Data()
    word_trie = words_data.get_word(sentence[0].lower())
    print(word_trie)
    print(word_trie.search(format_sentence(sentence)))
