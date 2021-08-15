import pickle
from data.word_trie import Word_Trie


class Words_Data:
    words = dict()
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Words_Data.__instance:
            Words_Data.__instance = object.__new__(cls)
        return Words_Data.__instance

    def add_word(self, word):
        if not isinstance(word, str):
            raise ValueError("word has to be string.")
        if word not in Words_Data.words:
            Words_Data.words[word] = Word_Trie()
        else:
            return "word is exist"

    def add_sentence(self, word, sentence, index):
        if not isinstance(word, str):
            raise ValueError("word has to be string.")
        if word not in Words_Data.words:
            Words_Data.words[word] = Word_Trie()
            Words_Data.words[word].insert(sentence[index:index+20], sentence)
        else:
            Words_Data.words[word].insert(sentence[index:index+20], sentence)

    def get_word(self, word):
        if word not in Words_Data.words:
            return "word isn't exist"
        else:
            return Words_Data.words[word]

    def save_word(self, char):
        if char not in Words_Data.words:
            return "word isn't exist"
        else:
            file = open(f'{char}','wb')
            pickle.dump(Words_Data.words[char], file)
            file.close()
