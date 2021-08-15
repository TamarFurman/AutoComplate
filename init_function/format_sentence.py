import re


def format_sentence(sentence):
    final = "".join([re.sub(r"[^a-zA-Z]+", ' ', k) for k in sentence])
    comma_sen = " ".join(final.lower().split(","))
    return " ".join(comma_sen.split())
