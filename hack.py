import string


def hack_caesar(text, model):

    lowercase_letter = string.ascii_lowercase

    counter = {i: 0 for i in lowercase_letter}

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
