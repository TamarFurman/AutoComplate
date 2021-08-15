import itertools
import os
from data.sentence import Sentence
from data.sentences_dict import SentencesCollection
from data.words_data import Words_Data
from init_function.format_sentence import format_sentence


class Init_Data:
    __index_char = itertools.count(start=97)
    __char = ""

    @staticmethod
    def insert_sentence(sentence: str, page: str, line: int) -> None:
        word_data = Words_Data()
        s = Sentence(sentence, page, line)
        format = format_sentence(sentence)
        SentencesCollection.get_instance().add(format, s)
        # add to words
        for i in range(len(sentence)):
            if sentence[i] != " ":
                word_data.add_sentence(sentence[i].lower(), format, i)

    @staticmethod
    def read_files(files: list) -> None:
        word_data = Words_Data()
        index = 0
        # for j in range(26):
        Init_Data.__char = chr(next(Init_Data.__index_char))
        for f in files:
            with open(f, encoding="utf8") as file:
                index += 1
                lines = file.readlines()
                for i in range(len(lines)):
                    # check if sentence is correct
                    Init_Data.insert_sentence(lines[i], os.path.basename(f)[-4], i)
            # word_data.save_word(Init_Data.__char)