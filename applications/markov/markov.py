import random
import re

# TODO: analyze which words can follow other words
# Your code here
markov_cache = {}
start_cache = {}
end_cache = {}


def is_end_word(word):
    if (word[-1] in ['.', '?', '!']):
        # or (word[-2] + word[-1] in ['."', '?"', '!"']):
        if word not in end_cache:
            end_cache[word] = word
        return True
    else:
        return False


def is_start_word(word):
    if re.match(r'^[A-Z]', word):
        # or re.match(r'^"A-Z', word):

        if word not in start_cache:
            start_cache[word] = word
        return True
    else:
        return False


def analyze(txt):
    word_list = txt.split(" ")

    i = 0
    while i < len(word_list) - 1:
        word = word_list[i]
        next_word = word_list[i + 1]
        if word not in markov_cache:
            is_end_word(word)
            is_start_word(word)
            markov_cache[word] = [next_word]
            i += 1
        else:
            is_end_word(word)
            is_start_word(word)
            markov_cache[word].append(next_word)
            i += 1

# TODO: construct 5 random sentences
# Your code here


def generate_sentence():
    start_list = list(start_cache.items())

    last_start_index = len(start_list) - 1
    start_word = start_list[random.randint(0, last_start_index)][0]

    sentence = start_word

    current_word = start_word
    generating = True

    while generating:
        next_word = markov_cache[current_word][random.randint(0, len(markov_cache[current_word]) - 1)]

        sentence = sentence + " " + next_word
        current_word = next_word

        if is_end_word(next_word):
            generating = None

    return sentence


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    analyze(words)
    sentences: list = []
    run_count: int = 0
    while run_count <= 4:
        sentences.append(generate_sentence())
        run_count += 1
    for sentence in sentences:
        print(sentence + "\n")

