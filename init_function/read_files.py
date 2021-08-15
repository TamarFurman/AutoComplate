import os
# from init_function.insert_sentence import insert_sentence
from init_function.insert_sentence import Init_Data


def find_txt_files(path: str) -> list:
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))
    print(len(files))
    return files
