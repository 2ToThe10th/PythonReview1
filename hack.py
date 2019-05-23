import sys
import string
import decode

ALLOWABLE_ERROR = 0.2


def hack_caesar(text, model):
    lowercase_letter = string.ascii_lowercase

    counter = {index: 0 for index in lowercase_letter}

    for letter in text:
        counter[letter] += 1

    max_match_index = -1
    max_plus_index = -1

    for plus_index in range(len(counter)):
        match_index = 0
        for index in range(len(counter)):
            match_index += model[index] \
                           * counter[lowercase_letter[(index + plus_index) % len(lowercase_letter)]]

        if match_index > max_match_index:
            max_match_index = match_index
            max_plus_index = plus_index

    return max_plus_index


def hack(arguments):
    if arguments['cipher'] == 'vigenere':
        vigenere_hack(arguments)

    if arguments['cipher'] == 'caesar':
        caesar_hack(arguments)


def vigenere_hack(arguments):
    with sys.stdin if arguments['input_file'] is None else open(arguments['input_file'], 'r') as input_file:

        input_text = []

        lowercase_letter = string.ascii_lowercase

        full_input_text = []

        for line in input_file:
            full_input_text.append(line)
            for symbol in line:
                if symbol.islower():
                    input_text.append(symbol)
                elif symbol.isupper():
                    input_text.append(symbol.lower())

    string_input_text = ''.join(input_text)

    with open(arguments['model_file'], 'r') as model_file:

        try:
            train_model = [int(count_of_letters_in_model) for count_of_letters_in_model in model_file.readline().split(',')]
        except Exception:
            raise TypeError('Wrong model_file')

        if len(train_model) != len(lowercase_letter):
            raise ValueError('Wrong model_file')

    match_index_in_model = 0
    count_of_letters_in_model = 0

    for count_of_letter_in_train_file in train_model:
        match_index_in_model += max(0, count_of_letter_in_train_file * (count_of_letter_in_train_file - 1))
        count_of_letters_in_model += count_of_letter_in_train_file

    match_index_in_model /= max(1, count_of_letters_in_model * (count_of_letters_in_model - 1))

    len_of_key = 0

    for len_of_key in range(1, len(input_text)):
        all_match_index = []

        for first_element in range(len_of_key):
            model_of_hack = {index: 0 for index in lowercase_letter}

            for index in range(first_element, len(string_input_text), len_of_key):
                model_of_hack[string_input_text[index]] += 1

            match_index_in_input = 0
            count_of_letters_in_input = 0

            for count_of_letter_in_input_file in model_of_hack.values():
                match_index_in_input += max(0, count_of_letter_in_input_file * (count_of_letter_in_input_file - 1))
                count_of_letters_in_input += count_of_letter_in_input_file

            match_index_in_input /= max(1, count_of_letters_in_input
                                        * (count_of_letters_in_input - 1))

            all_match_index.append(match_index_in_input)

        if all(symbol_index > match_index_in_model * (1 - ALLOWABLE_ERROR) for symbol_index in all_match_index):
            break

    list_key = []

    for first_element in range(len_of_key):
        list_key.append(lowercase_letter[hack_caesar(
            string_input_text[first_element::len_of_key], train_model)])

    key = ''.join(list_key)

    with sys.stdout if arguments['output_file'] is None else open(arguments['output_file'], 'w') as output_file:

        key_index = 0

        for line in full_input_text:
            return_value = decode.decode_vigenere(line, key, key_index)
            output_file.write(return_value[0])
            key_index = return_value[1]
            output_file.flush()


def caesar_hack(arguments):
    with sys.stdin if arguments['input_file'] is None else open(arguments['input_file'], 'r') as input_file:

        input_text = []

        lowercase_letter = string.ascii_lowercase
        uppercase_letter = string.ascii_uppercase

        full_input_text = []

        for line in input_file:
            full_input_text.append(line)
            for symbol in line:
                if symbol in lowercase_letter:
                    input_text.append(symbol)
                elif symbol in uppercase_letter:
                    input_text.append(lowercase_letter[uppercase_letter.find(symbol)])

    string_input_text = ''.join(input_text)

    with open(arguments['model_file'], 'r') as model_file:

        try:
            train_model = [int(count_of_letters_in_model) for count_of_letters_in_model in model_file.readline().split(',')]
        except Exception:
            raise TypeError('Wrong model_file')

        if len(train_model) != len(lowercase_letter):
            raise ValueError('Wrong model_file')

    key = hack_caesar(string_input_text, train_model)

    with sys.stdout if arguments['output_file'] is None else open(arguments['output_file'], 'w') as output_file:

        key_index = 0

        for line in full_input_text:
            return_value = decode.decode_caesar(line, key, key_index)
            output_file.write(return_value[0])
            key_index = return_value[1]
            output_file.flush()
