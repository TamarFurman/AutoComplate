from data.sentence import Sentence


class SentencesCollection:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if SentencesCollection.__instance == None:
            SentencesCollection()
        return SentencesCollection.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if SentencesCollection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SentencesCollection.__instance = self
            self.sentences = dict()

    def add(self, key,sentence: Sentence):
        self.sentences[key] = sentence
