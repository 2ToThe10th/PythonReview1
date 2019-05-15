import sys
import string


def train(arguments):

    with sys.stdin if arguments['text_file'] is None else open(arguments['text_file'], 'r') as text_file:

        lowercase_letter = string.ascii_lowercase
        uppercase_letter = string.ascii_uppercase

        model = [0] * len(lowercase_letter)

        for line in text_file:
            for i in line:
                if i in lowercase_letter:
                    model[lowercase_letter.find(i)] += 1
                elif i in uppercase_letter:
                    model[uppercase_letter.find(i)] += 1

    with open(arguments['model_file'], 'w') as model_file:

        for i in range(len(lowercase_letter)):
            if i != len(lowercase_letter) - 1:
                model_file.write(str(model[i]) + ',')
            else:
                model_file.write(str(model[i]) + '\n')
