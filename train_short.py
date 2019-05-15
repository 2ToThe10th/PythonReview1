import sys
import collections as cl
import string


def train_short(arguments):
    if arguments['N'] <= 0:
        raise ValueError('Incorrect N: N must be positive')

    with sys.stdin if arguments['text_file'] is None else open(arguments['text_file'], 'r') as text_file:

        lowercase_letter = string.ascii_lowercase
        uppercase_letter = string.ascii_uppercase

        short_model = cl.Counter()

        for line in text_file:
            for i in line.split(' '):
                normalize_word = []
                for j in i:
                    if j in lowercase_letter:
                        normalize_word.append(j)
                    elif j in uppercase_letter:
                        normalize_word.append(lowercase_letter[uppercase_letter.find(j)])
                if normalize_word:
                    normalize_word = ''.join(normalize_word)
                    short_model[normalize_word] += 1

    with sys.stdin if arguments['model_file'] is None else open(arguments['model_file'], 'r') as model_file:

        for i, j in short_model.items():
            if j >= arguments['N']:
                model_file.write(i + ':' + str(j) + ',')
