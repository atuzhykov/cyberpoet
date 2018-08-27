import random
from collections import defaultdict
import re

def gettext(filename):
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        document = re.findall(r'(?u)\w+|\'+|\.', data)

    return document


def generate(datasource):
    document = gettext(datasource)
    trigrams = zip(document,document[1:],document[2:])
    transitions = defaultdict(list)
    starts = []
    for prev,current,next in trigrams:
        if prev == ".":
            starts.append(current)
        transitions[(prev,current)].append(next)

    current = random.choice(starts)
    prev = "."
    result = [current]
    while True:
        next_word_candidates = transitions[(prev, current)]
        next_word = random.choice(next_word_candidates)
        prev, current = current, next_word
        result.append(current)

        if current == ".": return " ".join(result)


print(generate('Andrukhovych.txt'))