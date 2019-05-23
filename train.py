import sys
import string


def train(arguments):

    with sys.stdin if arguments['text_file'] is None else open(arguments['text_file'], 'r') as text_file:

        lowercase_letter = string.ascii_lowercase
        uppercase_letter = string.ascii_uppercase

        model = [0] * len(lowercase_letter)

        for line in text_file:
            for symbol in line:
                if symbol in lowercase_letter:
                    model[lowercase_letter.find(symbol)] += 1
                elif symbol in uppercase_letter:
                    model[uppercase_letter.find(symbol)] += 1

    with open(arguments['model_file'], 'w') as model_file:

        for letter_index in range(len(lowercase_letter)):
            if letter_index != len(lowercase_letter) - 1:
                model_file.write(str(model[letter_index]) + ',')
            else:
                model_file.write(str(model[letter_index]) + '\n')
