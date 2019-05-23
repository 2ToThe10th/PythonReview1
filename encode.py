import string


def encode_caesar(text, key, index):
    return encode_vigenere(text, string.ascii_lowercase[key], index)


def encode_vigenere(text, key, index):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase

    encoded_text = []

    for symbol in text:
        if index == len(key):
            index = 0

        if symbol in lowercase_letters:
            encoded_text.append(
                lowercase_letters[(lowercase_letters.find(symbol) + lowercase_letters.find(key[index]))
                                  % len(lowercase_letters)])
            index += 1
        elif symbol in uppercase_letters:
            encoded_text.append(
                uppercase_letters[(uppercase_letters.find(symbol) + lowercase_letters.find(key[index]))
                                  % len(uppercase_letters)])
            index += 1
        else:
            encoded_text.append(symbol)

    return tuple([''.join(encoded_text), index])
