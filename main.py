import urllib.request

from complete_function.search import search
from init_function.format_sentence import format_sentence
from init_function.insert_sentence import Init_Data
from init_function.read_files import find_txt_files


def print_hi(name):
    init_data = Init_Data()
    files = find_txt_files("C:\\Users\\user\\Downloads\\2021-archive\\python-3.8.4-docs-text")
    init_data.read_files(files)
    user_input = ""
    print("insert sentence:")
    while user_input != "q":
        user_input = input()
        search(user_input)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/