class Sentence:
    def __init__(self, sentence: str, page: str, line: int) -> None:
        self.__line = line
        self.__page = page
        self.__sentence = sentence

    def get_line(self):
        return self.__line

    def get_page(self):
        return self.__page

    def get_sentence(self):
        return self.__sentence

