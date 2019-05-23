import sys
import string
import decode


def hack_short(arguments):
    lowercase_letter = string.ascii_lowercase
    uppercase_letter = string.ascii_uppercase

    with open(arguments['model_file']) as model_file:

        model_words = model_file.readline()

        word = {}
        try:
            for words_number in model_words.split(','):
                if words_number:
                    word_in_model, number_in_model = words_number.split(':')
                    number_in_model = int(number_in_model)
                    word[word_in_model] = number_in_model
        except Exception:
            raise ValueError('Bad model file')

    with sys.stdin if arguments['input_file'] is None else open(arguments['input_file'], 'r') as text_file:

        input_text = []

        possible_key = [0] * len(lowercase_letter)

        for line in text_file:
            input_text.append(line)
            for word_in_line in line.split(' '):
                normalize_word = []
                for symbol in word_in_line:
                    if symbol in lowercase_letter:
                        normalize_word.append(symbol)
                    elif symbol in uppercase_letter:
                        normalize_word.append(lowercase_letter[uppercase_letter.find(symbol)])
                if normalize_word:
                    normalize_word = ''.join(normalize_word)
                    plus_index = [((len(lowercase_letter)
                                    + lowercase_letter.find(normalize_word[index + 1])
                                    - lowercase_letter.find(normalize_word[index]))
                                   % len(lowercase_letter)) for index in range(len(normalize_word) - 1)]

                    possible_words = []
                    counter = []

                    for letter in lowercase_letter:
                        may_be_word = [letter]
                        letter_index = lowercase_letter.find(letter)
                        for plus in plus_index:
                            letter_index += plus
                            letter_index %= len(lowercase_letter)
                            may_be_word.append(lowercase_letter[j])
                        may_be_word = ''.join(may_be_word)
                        if word.get(may_be_word):
                            possible_words.append((len(lowercase_letter)
                                                   + lowercase_letter.find(normalize_word[0])
                                                   - lowercase_letter.find(letter))
                                                  % len(lowercase_letter))
                            counter.append(word[may_be_word])

                    index = 0

                    for word in possible_words:
                        possible_key[word] += counter[index]
                        index += 1
        maxx_value = -1
        maxx_index = -1

        index = 0

        for key in possible_key:
            if key > maxx_value:
                maxx_value = key
                maxx_index = index
            index += 1

    with sys.stdout if arguments['output_file'] is None else open(arguments['output_file'], 'w') as output_file:

        for line in input_text:
            output_file.write(decode.decode_caesar(line, maxx_index, 0)[0])
            output_file.flush()
