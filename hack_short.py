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
            for i in model_words.split(','):
                if i:
                    word_in_model, number_in_model = i.split(':')
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
                for j in word_in_line:
                    if j in lowercase_letter:
                        normalize_word.append(j)
                    elif j in uppercase_letter:
                        normalize_word.append(lowercase_letter[uppercase_letter.find(j)])
                if normalize_word:
                    normalize_word = ''.join(normalize_word)
                    plus_index = [((len(lowercase_letter)
                                    + lowercase_letter.find(normalize_word[i + 1])
                                    - lowercase_letter.find(normalize_word[i]))
                                   % len(lowercase_letter)) for i in range(len(normalize_word) - 1)]

                    possible_words = []
                    counter = []

                    for i in lowercase_letter:
                        may_be_word = [i]
                        j = lowercase_letter.find(i)
                        for plus in plus_index:
                            j += plus
                            j %= len(lowercase_letter)
                            may_be_word.append(lowercase_letter[j])
                        may_be_word = ''.join(may_be_word)
                        if word.get(may_be_word):
                            possible_words.append((len(lowercase_letter)
                                                   + lowercase_letter.find(normalize_word[0])
                                                   - lowercase_letter.find(i))
                                                  % len(lowercase_letter))
                            counter.append(word[may_be_word])

                    index = 0

                    for i in possible_words:
                        possible_key[i] += counter[index]
                        index += 1
        maxx_value = -1
        maxx_index = -1

        index = 0

        for i in possible_key:
            if i > maxx_value:
                maxx_value = i
                maxx_index = index
            index += 1

    with sys.stdout if arguments['output_file'] is None else open(arguments['output_file'], 'w') as output_file:

        for line in input_text:
            output_file.write(decode.decode_caesar(line, maxx_index, 0)[0])
            output_file.flush()
